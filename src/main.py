import time
import psycopg2
from control import DatabaseController
from interacoes import exibir_dialogo, exibir_dialogo_mercador, exibir_dialogo_contratante
import sys
import select
import time

class TerminalInterface:
    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.current_player_id = None

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar Novo Jogador")
            print("2. Listar Jogadores")
            print("3. Selecionar Jogador e Iniciar Jogo")
            print("4. Executar Script SQL")
            print("5. Sair")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.list_players()
            elif choice == "3":
                self.select_player_and_start_game()
            elif choice == "4":
                self.run_sql_script()
            elif choice == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def add_player(self):
        jogador_nome = input("Digite o nome do novo jogador: ").strip()
        if jogador_nome:
            self.db_controller.connect()
            self.db_controller.add_player(jogador_nome)
            self.db_controller.close()
        else:
            print("Nome do jogador não pode estar vazio.")

    def list_players(self):
        self.db_controller.connect()
        jogadores = self.db_controller.get_registered_players()
        jogadores_nome = self.db_controller.get_registered_players_1()
        self.db_controller.close()
        print(jogadores)
        if jogadores:
            print("\nJogadores Registrados:")
            for jogador in jogadores_nome:
                print(f"- {jogador}")
        else:
            print("Nenhum jogador registrado.")

    def list_connections(self):
        self.db_controller.connect()
        connections = self.db_controller.get_available_connections(self.current_player_id)
        self.db_controller.close()
        if connections:
            for connection in connections:
                print(f"-[{connection[0]}] {connection[1]}: {connection[2]}")
        else:
            print("Nenhuma conexão registrada.")

    def select_player_and_start_game(self):
        self.db_controller.connect()
        jogadores = self.db_controller.get_registered_players()

        if not jogadores:
            print("Nenhum jogador registrado para iniciar o jogo.")
            return

        print("\nEscolha um jogador para iniciar:")
        for index, jogador in enumerate(jogadores):
            print(f"{jogador}. {self.db_controller.get_player_id(jogador)}")

        print("")

        choice = input("Digite o número do jogador escolhido: ").strip()
        try:
            choice_index = int(choice)
            player = self.db_controller.get_player_id(choice_index)

            if player:
                self.current_player_id = choice_index
                print(f"Jogador {player} selecionado. Iniciando o jogo...")
                self.start_game()
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
        self.db_controller.close()

    def print_effect(self, text, delay=0.03):
            """Imprime o texto com efeito de digitação, podendo ser cancelado com Enter."""
            for char in text:
                if select.select([sys.stdin], [], [], 0)[0]:  # Se Enter for pressionado
                    sys.stdin.read(1)  # Limpa o buffer
                    sys.stdout.write(text[text.index(char):])  # Exibe o restante do texto imediatamente
                    sys.stdout.flush()
                    print()
                    return
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            print()

    def start_game(self):
        jogador_id = self.current_player_id
        texto = self.db_controller.get_dialogo()
        for i in texto:
            self.print_effect(i)
        self.player_movement()


    def player_movement(self):
        while True:
            self.db_controller.connect()
            sala_atual_id, sala_atual_nome = self.get_current_room_with_name()
            self.db_controller.close()

            print("\nMovimento do Jogador:")
            print(f"Você está na sala: {sala_atual_nome} (ID: {sala_atual_id})")
            print("1. Explorar Sala Atual")
            print("2. Mover para outra sala")
            print("3. Ver status do jogador")
            print("4. Ver inventário")
            print("5. Listar Missões")
            print("6. Sair do jogo")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                self.explore_current_room()
            elif choice == "2":
                self.list_connections()
                self.move_player()
            elif choice == "3":
                self.show_player_status()
            elif choice == "4":
                self.show_inventory()
            elif choice == "5":
                self.show_missions()
            elif choice == "6":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida, tente novamente.")
    
    
    def show_missions (self):
        self.db_controller.connect()
        missoes = self.db_controller.show_missoes()
        print("------Missões a serem realizadas------")
        for missao in missoes:
            print(missao[0])
        print("-------------------------------------")

    def explore_current_room(self):
        self.db_controller.connect()
        sala_atual = self.get_current_room()
        inimigos = self.db_controller.enemy(sala_atual)
        mercador = self.get_npc_in_room(sala_atual, "Mercador")
        contratante = self.get_npc_in_room(sala_atual, "Contratante")
        

        print("\nExplorando a sala atual...")
        if inimigos:
            print("Inimigos encontrados!")
            print("+-----------------+")
            for i in range(5):  # Altura da sala
                if i == 2:  # Centralizando os inimigos
                    inimigos_str = " ".join(["(o_o)" for _ in inimigos])
                    print(f"| {inimigos_str:<13} |")
                else:
                    print("|                 |")
            print("+-----------------+")
            self.handle_combat(inimigos)
            
        elif mercador:
            print("Você encontrou um mercador!")
            self.handle_merchant_interaction()
        elif contratante:
            print("Você encontrou um contratante!")
            self.handle_contractor_interaction()
        else:
            print("Nada de interessante na sala.")

        self.db_controller.close()

    def get_current_room(self):
        cursor = self.db_controller.conn.cursor()
        cursor.execute("SELECT id_sala FROM PC WHERE id_personagem = %s", (self.current_player_id,))
        sala_atual = cursor.fetchone()[0]
        cursor.close()
        return sala_atual

    def get_current_room_with_name(self):
        """Obtém o ID e o nome da sala atual do jogador."""
        cursor = self.db_controller.conn.cursor()
        cursor.execute(
            """
            SELECT s.id_sala, s.nome 
            FROM Sala s
            JOIN PC p ON s.id_sala = p.id_sala
            WHERE p.id_personagem = %s
            """,
            (self.current_player_id,),
        )
        sala_atual = cursor.fetchone()
        cursor.close()
        return sala_atual

    def get_npc_in_room(self, sala_id, npc_type):
        cursor = self.db_controller.conn.cursor()
        cursor.execute(
            "SELECT id_personagem FROM NPC WHERE id_personagem IN (SELECT id_personagem FROM Mercador WHERE id_sala = %s) AND tipo = %s",
            (sala_id, npc_type),
        )
        npc = cursor.fetchone()
        cursor.close()
        return npc

    

    def draw_battle_interface(self, player_hp, enemy_hp, enemy_name):
        print("=" * 40)
        print(f"{enemy_name} (HP: {enemy_hp})")
        print(" " * 20 + "VS")
        print(f"Jogador (HP: {player_hp})")
        print("=" * 40)

    def handle_combat(self, inimigos):
        for inimigo in inimigos:
            print(f"Você encontrou um inimigo: {inimigo['id_inimigo']}")
            print("1. Lutar")
            print("2. Fugir")
            choice = input("Escolha uma ação: ").strip()

            if choice == "1":
                self.fight_enemy(inimigo)
            elif choice == "2":
                print("Você fugiu do combate.")
                break
            else:
                print("Opção inválida.")

    def fight_enemy(self, inimigo):
        print("Iniciando combate...")
        self.db_controller.connect()
        player = self.db_controller.get_status(self.current_player_id)[0]
        player_hp = player[3]
        player_sala = player[5]
        enemy = self.db_controller.get_enemy_sala(self.db_controller.get_sala_by_name(player_sala))
        enemy_hp = enemy[3]
        enemy_name = inimigo['id_inimigo']
    
        while player_hp > 0 and enemy_hp > 0:
            self.draw_battle_interface(player_hp, enemy_hp, enemy_name)
            print("\nEscolha sua ação:")
            print("1. Atacar")
            print("2. Usar item")
            print("3. Fugir")

            choice = input("Escolha uma ação: ").strip()

            if choice == "1":
                dano = 10  # Exemplo de dano do jogador
                enemy_hp -= dano
                self.db_controller.att_status_instacia(enemy[0], enemy_hp)
                print(f"Você atacou e causou {dano} de dano. Vida do inimigo: {enemy_hp}")
                if enemy_hp <= 0:
                    self.db_controller.del_status_instacia()
                    cursor.execute("SELECT respawn_inimigo();")
                    print("Você derrotou o inimigo!")
                    break
                dano_inimigo = inimigo["atk"]
                player_hp -= dano_inimigo
                self.db_controller.att_status_player(self.current_player_id, player_hp)
                print(f"O inimigo atacou e causou {dano_inimigo} de dano. Sua vida: {player_hp}")
                if player_hp <= 0:
                    print("Você foi derrotado!")
                    break
            elif choice == "2":
                print("Você usou um item.")
                # Implementar lógica de itens
                pass
            elif choice == "3":
                print("Você fugiu do combate.")
                break
            else:
                print("Opção inválida.")
        self.db_controller.close()

    def handle_merchant_interaction(self):
        print("Interagindo com o mercador...")
        while True:
            print("\nMenu do Mercador:")
            print("1. Comprar item")
            print("2. Sair")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                print("Comprando item...")
                # Implementar lógica de compra
                pass
            elif choice == "2":
                print("Saindo do mercador...")
                break
            else:
                print("Opção inválida.")

    def show_inventory(self):
        """Exibe o inventário do jogador e permite usar itens."""
        self.db_controller.connect()
        cursor = self.db_controller.conn.cursor()
        cursor.execute(
            """
            SELECT i.id_instancia_item, item.nome, item.descricao 
            FROM Inventario i
            JOIN InstanciaItem ii ON i.id_instancia_item = ii.id_instancia_item
            JOIN Item item ON ii.id_item = item.id_item
            WHERE i.id_inventario = %s
            """,
            (self.current_player_id,),
        )
        inventario = cursor.fetchall()
        cursor.close()
        self.db_controller.close()

        if inventario:
            print("\nInventário:")
            for index, item in enumerate(inventario):
                print(f"[{index + 1}] {item[1]} - {item[2]}")

            choice = input("Escolha o número do item para usar ou pressione Enter para voltar: ").strip()
            if choice.isdigit():
                item_index = int(choice) - 1
                if 0 <= item_index < len(inventario):
                    item_id = inventario[item_index][0]
                    print(f"Você usou o item: {inventario[item_index][1]}")
                    self.use_item(item_id)
                else:
                    print("Opção inválida.")
        else:
            print("Seu inventário está vazio.")

    def use_item(self, item_id):
        """Usa um item e remove do inventário."""
        self.db_controller.connect()
        cursor = self.db_controller.conn.cursor()
        try:
            # Exemplo: Lógica para aplicar o efeito do item
            cursor.execute(
                """
                DELETE FROM Inventario WHERE id_instancia_item = %s AND id_inventario = %s
                """,
                (item_id, self.current_player_id),
            )
            self.db_controller.conn.commit()
            print("Item usado com sucesso!")
        except Exception as e:
            print(f"Erro ao usar item: {e}")
        finally:
            cursor.close()
            self.db_controller.close()

    def handle_contractor_interaction(self):
        print("Interagindo com o contratante...")
        # Lógica de interação com contratante aqui
        pass

    def handle_missions(self, missoes):
        print("Missões disponíveis:")
        for missao in missoes:
            print(f"- {missao[1]}")
        # Lógica para aceitar missões aqui
        pass

    def move_player(self):
        destino = input("Digite o número da sala para se mover: ").strip()
        if destino.isdigit():
            try:
                self.db_controller.connect()
                self.db_controller.move_player(self.current_player_id, int(destino))
                self.db_controller.close()
            except Exception as e:
                print(f"Erro ao mover jogador: {e}")
        else:
            print("Número da sala inválido.")

    def show_player_status(self):
        self.db_controller.connect()
        jogador_status = self.db_controller.get_status(self.current_player_id)
        self.db_controller.close()
        if jogador_status:
            jogador = jogador_status[0]
            print(f"[Status do jogador] \n Nome: {jogador[0]} \n Nível: {jogador[1]} \n XP: {jogador[2]} \n HP: {jogador[3]}/{jogador[4]} \n Sala atual: {jogador[5]}")
        else:
            print("Nenhuma conexão registrada.")

    def run_sql_script(self):
        script_path = input("Digite o caminho do script SQL a ser executado: ").strip()
        if script_path:
            self.db_controller.connect()
            self.db_controller.execute_sql_script(script_path)
            self.db_controller.close()
        else:
            print("Caminho do script não pode estar vazio.")


if __name__ == "__main__":
    db_controller = DatabaseController()
    terminal_interface = TerminalInterface(db_controller)
    terminal_interface.run()
