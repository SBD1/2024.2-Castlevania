import time
import psycopg2
from control import DatabaseController
from interacoes import exibir_dialogo, exibir_dialogo_mercador, exibir_dialogo_contratante
import sys

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
        self.db_controller.close()
        if jogadores:
            print("\nJogadores Registrados:")
            for jogador in jogadores:
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
        """Imprime o texto com efeito de digitação."""
        for char in text:
            for char1 in char:
                sys.stdout.write(char1)
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
            print("\nMovimento do Jogador:")
            print("1. Explorar Sala Atual")
            print("2. Mover para outra sala")
            print("3. Ver status do jogador")
            print("4. Sair do jogo")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                self.explore_current_room()
            elif choice == "2":
                self.list_connections()
                self.move_player()
            elif choice == "3":
                self.show_player_status()
            elif choice == "4":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def explore_current_room(self):
        self.db_controller.connect()
        sala_atual = self.get_current_room()
        inimigos = self.db_controller.enemy(sala_atual)
        mercador = self.get_npc_in_room(sala_atual, "Mercador")
        contratante = self.get_npc_in_room(sala_atual, "Contratante")
        missoes = self.get_missions_in_room(sala_atual)

        print("\nExplorando a sala atual...")
        if inimigos:
            print("Inimigos encontrados!")
            self.handle_combat(inimigos)
        elif mercador:
            print("Você encontrou um mercador!")
            self.handle_merchant_interaction()
        elif contratante:
            print("Você encontrou um contratante!")
            self.handle_contractor_interaction()
        elif missoes:
            print("Missões disponíveis!")
            self.handle_missions(missoes)
        else:
            print("Nada de interessante na sala.")

        self.db_controller.close()

    def get_current_room(self):
        cursor = self.db_controller.conn.cursor()
        cursor.execute("SELECT id_sala FROM PC WHERE id_personagem = %s", (self.current_player_id,))
        sala_atual = cursor.fetchone()[0]
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

    def get_missions_in_room(self, sala_id):
        cursor = self.db_controller.conn.cursor()
        cursor.execute(
            "SELECT id_missao, nome FROM Missao WHERE id_missao IN (SELECT id_missao FROM Contrato WHERE id_contratante IN (SELECT id_personagem FROM NPC WHERE id_personagem IN (SELECT id_personagem FROM Contratante WHERE id_sala = %s)))",
            (sala_id,),
        )
        missoes = cursor.fetchall()
        cursor.close()
        return missoes

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
        # Lógica de combate aqui
        pass

    def handle_merchant_interaction(self):
        print("Interagindo com o mercador...")
        # Lógica de negociação aqui
        pass

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