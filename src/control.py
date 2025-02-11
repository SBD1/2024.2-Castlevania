import psycopg2
import time
import sys

class DatabaseController:
    def __init__(self, dbname="mud_castlevania4", user="user", password="admin", host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.create_database(self.dbname)


    def create_database(self, dbname):
        """Cria um novo banco de dados."""
        conn = psycopg2.connect(
            dbname="postgres",
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        conn.autocommit = True  # Necessário para criar banco de dados
        cursor = conn.cursor()
        
        try:
            cursor.execute(f"CREATE DATABASE {dbname}")
            print(f"Banco de dados '{dbname}' criado com sucesso.")
        except psycopg2.errors.DuplicateDatabase:
            print(f"Banco de dados '{dbname}' já existe.")
        except Exception as e:
            print(f"Erro ao criar banco de dados '{dbname}': {e}")
        finally:
            cursor.close()
            conn.close()

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )

    def close(self):
        if self.conn:
            self.conn.close()
    
    def add_sala_principal(self):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Mundo (id_mundo, nome, data) VALUES (1, 'Mundo 1', '2024-01-01')")
        cursor.execute("INSERT INTO Regiao (id_regiao, id_regiao_conectada, id_mundo, nome, descricao, dificuldade) VALUES (1, NULL, 1, 'Jardim do castelo', 'Jardim do castelo do dracula.', 'Fácil')")
        cursor.execute("INSERT INTO Sala (id_sala, id_regiao, nome, descricao) VALUES (1, 1, 'Jardim do castelo', 'O início da aventura.')")
        self.conn.commit()
        cursor.close()

    def add_player(self, nome):
            cursor = self.conn.cursor()

            # Verifica se há personagens antes de acessar last[-1]
            cursor.execute("SELECT COUNT(*) FROM Personagem")
            count = cursor.fetchone()[0]

            if count == 0:
                self.add_sala_principal()

            # Insere o personagem e recupera o ID gerado
            cursor.execute(
                "INSERT INTO Personagem (nome, descricao, tipo) VALUES (%s, %s, %s) RETURNING id_personagem",
                (nome, "Um bravo lutador.", "PC")
            )
            id_personagem = cursor.fetchone()[0]  # Captura o ID gerado automaticamente pelo PostgreSQL

            # Agora inserimos na tabela PC, sem precisar calcular o ID manualmente
            cursor.execute(
                "INSERT INTO PC (id_personagem, hp, mp, xp, absorcao, atk, lvl, luck, combat_status, coins, id_sala) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (id_personagem, 1000, 500, 0, 50, 100, 1, 10, 'Normal', 100, 1)
            )

            self.conn.commit()
            cursor.close()


    def get_registered_players(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_personagem, nome FROM Personagem WHERE tipo = 'PC'")
        jogadores = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return jogadores
    
    def get_registered_players_1(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_personagem, nome FROM Personagem WHERE tipo = 'PC'")
        jogadores = [row[1] for row in cursor.fetchall()]
        cursor.close()
        return jogadores

    def get_player_id(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT nome FROM Personagem WHERE id_personagem = %s", (player_id,))
        player = cursor.fetchone()
        cursor.close()
        return player[0]
    
    def get_player_name(self, player_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_personagem FROM Personagem WHERE nome = %s", (player_name,))
        player = cursor.fetchone()
        cursor.close()
        return player[0]

    def get_enemy_sala(self, sala_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM instanciaInimigo WHERE id_sala = %s", (sala_id,))
        enemy = cursor.fetchone()
        cursor.close()
      
        return enemy
    
    def get_sala_by_name(self, sala_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_sala FROM Sala WHERE nome = %s", (sala_name,))
        enemy = cursor.fetchone()
        cursor.close()
        return enemy

    def att_status_player(self, player_id, value):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE PC SET hp = %s WHERE id_personagem = %s", (value, player_id,))
        cursor.close()
     
    
    def att_status_instacia(self, instacia_id,  value):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE instanciaInimigo SET vida_atual = %s WHERE id_instancia = %s", (value,instacia_id,))
        cursor.close()
         
    def del_status_instacia(self, instacia_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM instanciaInimigo WHERE id_instancia = %s", (instacia_id,))
       
        cursor.close()

    def get_dialogo(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT texto FROM HISTORIA")
        texto = cursor.fetchall()
        cursor.close()
        return texto
    
    def get_available_connections(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_sala_destino, direcao, descricao_conexao FROM Conexao WHERE id_sala_origem = (SELECT id_sala FROM PC WHERE id_personagem = %s)", (player_id,))
        connections = cursor.fetchall()
        cursor.close()
        return connections

    def move_player(self, player_id, destino):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE PC SET id_sala = %s WHERE id_personagem = %s", (destino, player_id))
        self.conn.commit()
        cursor.close()

    def enemy(self, id_sala):
        """Consulta os inimigos na sala especificada."""
        cursor = self.conn.cursor()
        try:
            # Consulta SQL para obter informações sobre os inimigos na sala
            cursor.execute("""
                SELECT 
                    i.id_personagem AS id_inimigo,
                    ii.vida_atual,
                    ii.absorcao,
                    ii.atk,
                    ii.habilidade,
                    ii.combat_status
                FROM InstanciaInimigo ii
                JOIN Inimigo i ON ii.id_inimigo = i.id_personagem
                WHERE ii.id_sala = %s;
            """, (id_sala,))

            # Recupera os resultados
            inimigos = cursor.fetchall()
            
            # Se não houver inimigos, retorna uma lista vazia
            if not inimigos:
                return []

            # Organiza os resultados em um formato de dicionário
            inimigos_data = [
                {
                    "id_inimigo": inimigo[0],
                    "vida_atual": inimigo[1],
                    "absorcao": inimigo[2],
                    "atk": inimigo[3],
                    "habilidade": inimigo[4],
                    "combat_status": inimigo[5]
                } for inimigo in inimigos
            ]
            return inimigos_data

        except Exception as e:
            print(f"Erro ao consultar inimigos: {e}")
            return []  # Retorna uma lista vazia em caso de erro
        finally:
            cursor.close()


    def get_status(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT p.nome, pc.lvl, pc.xp, pc.hp, pc.hp, s.nome FROM Personagem p JOIN PC pc ON p.id_personagem = pc.id_personagem JOIN Sala s ON pc.id_sala = s.id_sala WHERE p.id_personagem = %s", (player_id,))
        status = cursor.fetchall()
        cursor.close()
        return status

    def execute_sql_script(self, script_path):
        cursor = self.conn.cursor()
        with open(script_path, 'r') as file:
            cursor.execute(file.read())
        self.conn.commit()
        cursor.close()

    def criar_interacao_mercador(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Dialogo (id_personagem, texto) VALUES (%s, %s)", (2, 'Bem-vindo à minha loja! O que você deseja?'))
        self.conn.commit()
        

    def criar_interacao_contratante(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Dialogo (id_personagem, texto) VALUES (%s, %s)", (4, 'Preciso de sua ajuda para derrotar os inimigos!'))
        self.conn.commit()
        cursor.close()
    
    def show_missoes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT nome FROM Missao")
        missoes = cursor.fetchall()
        cursor.close()
        return missoes