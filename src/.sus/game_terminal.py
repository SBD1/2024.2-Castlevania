import psycopg2
from control import DatabaseController
from interacoes import exibir_dialogo, exibir_dialogo_mercador, exibir_dialogo_contratante

class GameTerminal:
    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.current_player_id = None

    def run(self):
        while True:
            print("\nMenu Principal:")
            print("1. Selecionar Jogador")
            print("2. Movimentar Jogador")
            print("3. Combate")
            print("4. Equipar ou Usar Item")
            print("5. Enfrentar o Boss")
            print("6. Sair do Jogo")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                self.select_player()
            elif choice == "2":
                self.move_player()
            elif choice == "3":
                self.combat()
            elif choice == "4":
                self.equip_or_use_item()
            elif choice == "5":
                self.boss_interaction()
            elif choice == "6":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def select_player(self):
        self.db_controller.connect()
        players = self.db_controller.get_registered_players()
        self.db_controller.close()

        if not players:
            print("Nenhum jogador registrado.")
            return

        print("\nJogadores Disponíveis:")
        for idx, player in enumerate(players):
            print(f"{idx + 1}. {player}")

        choice = input("Escolha o número do jogador: ").strip()

        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(players):
                self.current_player_id = choice_index + 1
                print(f"Jogador {players[choice_index]} selecionado.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    def move_player(self):
        if not self.current_player_id:
            print("Nenhum jogador selecionado.")
            return

        self.db_controller.connect()
        connections = self.db_controller.get_available_connections(self.current_player_id)
        self.db_controller.close()

        if not connections:
            print("Nenhuma conexão disponível.")
            return

        print("\nConexões Disponíveis:")
        for conn in connections:
            print(f"[{conn[0]}] {conn[1]}: {conn[2]}")

        choice = input("Escolha a direção para se mover: ").strip()

        try:
            destination_id = int(choice)
            self.db_controller.connect()
            self.db_controller.move_player(self.current_player_id, destination_id)
            self.db_controller.close()
            print("Movimento realizado com sucesso.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
        except Exception as e:
            print(f"Erro ao mover jogador: {e}")

    def combat(self):
        if not self.current_player_id:
            print("Nenhum jogador selecionado.")
            return

        print("Iniciando combate...")

        self.db_controller.connect()
        cursor = self.db_controller.conn.cursor()

        try:
            # Busca inimigos na sala atual
            cursor.execute("""
                SELECT ii.id_instancia, p.nome, ii.vida_atual, ii.atk
                FROM InstanciaInimigo ii
                JOIN Personagem p ON ii.id_inimigo = p.id_personagem
                WHERE ii.id_sala = (SELECT id_sala FROM PC WHERE id_personagem = %s)
            """, (self.current_player_id,))
            enemies = cursor.fetchall()

            if not enemies:
                print("Nenhum inimigo encontrado na sala.")
                return

            print("\nInimigos na sala:")
            for idx, enemy in enumerate(enemies):
                print(f"{idx + 1}. {enemy[1]} (HP: {enemy[2]}, ATK: {enemy[3]})")

            choice = input("Escolha o inimigo para atacar: ").strip()
            choice_index = int(choice) - 1

            if 0 <= choice_index < len(enemies):
                enemy = enemies[choice_index]
                print(f"Atacando {enemy[1]}...")

                # Lógica de combate simples
                cursor.execute("SELECT atk FROM PC WHERE id_personagem = %s", (self.current_player_id,))
                player_atk = cursor.fetchone()[0]

                enemy_hp = enemy[2] - player_atk
                if enemy_hp <= 0:
                    print(f"Você derrotou {enemy[1]}!")
                    cursor.execute("DELETE FROM InstanciaInimigo WHERE id_instancia = %s", (enemy[0],))
                else:
                    print(f"{enemy[1]} contra-ataca!")
                    cursor.execute("SELECT hp FROM PC WHERE id_personagem = %s", (self.current_player_id,))
                    player_hp = cursor.fetchone()[0]

                    player_hp -= enemy[3]
                    if player_hp <= 0:
                        print("Você foi derrotado!")
                        cursor.execute("UPDATE PC SET hp = 0 WHERE id_personagem = %s", (self.current_player_id,))
                    else:
                        cursor.execute("UPDATE PC SET hp = %s WHERE id_personagem = %s", (player_hp, self.current_player_id))
                        cursor.execute("UPDATE InstanciaInimigo SET vida_atual = %s WHERE id_instancia = %s", (enemy_hp, enemy[0]))

                self.db_controller.conn.commit()
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")
        except Exception as e:
            print(f"Erro no combate: {e}")
        finally:
            cursor.close()
            self.db_controller.close()

    def equip_or_use_item(self):
        if not self.current_player_id:
            print("Nenhum jogador selecionado.")
            return

        print("Equipar ou usar item...")

        self.db_controller.connect()
        cursor = self.db_controller.conn.cursor()

        try:
            # Exibe itens disponíveis no inventário
            cursor.execute("""
                SELECT ii.id_instancia_item, i.nome, i.descricao
                FROM Inventario inv
                JOIN InstanciaItem ii ON inv.id_instancia_item = ii.id_instancia_item
                JOIN Item i ON ii.id_item = i.id_item
                WHERE inv.id_inventario = %s
            """, (self.current_player_id,))
            items = cursor.fetchall()

            if not items:
                print("Nenhum item no inventário.")
                return

            print("\nItens no inventário:")
            for idx, item in enumerate(items):
                print(f"{idx + 1}. {item[1]} - {item[2]}")

            choice = input("Escolha um item para usar: ").strip()
            choice_index = int(choice) - 1

            if 0 <= choice_index < len(items):
                item = items[choice_index]
                print(f"Usando {item[1]}...")
                # Lógica para usar o item (exemplo: poção de cura)
                if "cura" in item[2].lower():
                    cursor.execute("UPDATE PC SET hp = LEAST(hp + 50, 1000) WHERE id_personagem = %s", (self.current_player_id,))
                    print(f"{item[1]} usado com sucesso!")
                    cursor.execute("DELETE FROM Inventario WHERE id_instancia_item = %s", (item[0],))
                else:
                    print(f"{item[1]} equipado com sucesso!")
                    # Adicionar lógica para equipar itens

                self.db_controller.conn.commit()
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")
        except Exception as e:
            print(f"Erro ao usar item: {e}")
        finally:
            cursor.close()
            self.db_controller.close()

    def boss_interaction(self):
        if not self.current_player_id:
            print("Nenhum jogador selecionado.")
            return

        print("Enfrentando o Boss...")

        self.db_controller.connect()
        cursor = self.db_controller.conn.cursor()

        try:
            # Busca o boss na sala atual
            cursor.execute("""
                SELECT p.nome, c.hp, c.atk
                FROM Chefe c
                JOIN Personagem p ON c.id_personagem = p.id_personagem
                WHERE c.id_sala = (SELECT id_sala FROM PC WHERE id_personagem = %s)
            """, (self.current_player_id,))
            boss = cursor.fetchone()

            if not boss:
                print("Nenhum Boss encontrado na sala.")
                return

            print(f"\nVocê encontrou o Boss: {boss[0]} (HP: {boss[1]}, ATK: {boss[2]})")
            print("Preparando para o combate...")

            # Lógica de combate com o Boss
            cursor.execute("SELECT atk, hp FROM PC WHERE id_personagem = %s", (self.current_player_id,))
            player_stats = cursor.fetchone()
            player_hp = player_stats[1]
            player_atk = player_stats[0]

            boss_hp = boss[1]
            while player_hp > 0 and boss_hp > 0:
                boss_hp -= player_atk
                if boss_hp <= 0:
                    print(f"Você derrotou o Boss {boss[0]}!")
                    break

                print(f"O Boss {boss[0]} contra-ataca!")
                player_hp -= boss[2]
                if player_hp <= 0:
                    print("Você foi derrotado pelo Boss!")
                    break

            cursor.execute("UPDATE PC SET hp = %s WHERE id_personagem = %s", (max(player_hp, 0), self.current_player_id))
            self.db_controller.conn.commit()
        except Exception as e:
            print(f"Erro ao enfrentar o Boss: {e}")
        finally:
            cursor.close()
            self.db_controller.close()


if __name__ == "__main__":
    db_controller = DatabaseController()
    game_terminal = GameTerminal(db_controller)
    game_terminal.run()