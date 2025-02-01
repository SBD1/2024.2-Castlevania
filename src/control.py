import psycopg2

class DatabaseController:
    def __init__(self, dbname="mud_castlevania", user="user", password="admin", host="localhost", port="5432"):
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

    def add_player(self, nome):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Personagem (nome, descricao, tipo) VALUES (%s, %s, %s) RETURNING id_personagem", (nome, "Um bravo lutador.", "PC"))
        id_personagem = cursor.fetchone()[0]
        cursor.execute("INSERT INTO PC (id_personagem, hp, mp, xp, absorcao, atk, lvl, luck, combat_status, coins, id_sala) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (id_personagem, 1000, 500, 0, 50, 100, 1, 10, 'Normal', 100, 1))
        self.conn.commit()
        cursor.close()

    def get_registered_players(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT nome FROM Personagem WHERE tipo = 'PC'")
        jogadores = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return jogadores

    def get_available_connections(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_conexao, direcao, descricao_conexao FROM Conexao WHERE id_sala_origem = (SELECT id_sala FROM PC WHERE id_personagem = %s)", (player_id,))
        connections = cursor.fetchall()
        cursor.close()
        return connections

    def move_player(self, player_id, destino):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE PC SET id_sala = %s WHERE id_personagem = %s", (destino, player_id))
        self.conn.commit()
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
        cursor.execute("INSERT INTO Dialogo (id_personagem, texto) VALUES (%s, %s)", (player_id, "Bem-vindo à minha loja! O que você deseja?"))
        self.conn.commit()
        cursor.close()

    def criar_interacao_contratante(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Dialogo (id_personagem, texto) VALUES (%s, %s)", (player_id, "Preciso de sua ajuda para derrotar os inimigos!"))
        self.conn.commit()
        cursor.close()