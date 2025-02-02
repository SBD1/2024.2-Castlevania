import psycopg2

class DatabaseController:
    def __init__(self, dbname="mud_castlevania", user="user", password="admin", host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.create_database(self.dbname)
        self.create_tables()

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
        cursor.execute("SELECT COUNT(*) FROM PERSONAGEM")
        count = cursor.fetchone()[0]

        # Se não houver nenhum personagem, cria a sala principal
        if count == 0:
            self.add_sala_principal()

        cursor.execute("INSERT INTO Personagem (nome, descricao, tipo) VALUES (%s, %s, %s) RETURNING id_personagem", (nome, "Um bravo lutador.", "PC"))
        id_personagem = cursor.fetchone()[0]
        cursor.execute("INSERT INTO PC (id_personagem, hp, mp, xp, absorcao, atk, lvl, luck, combat_status, coins, id_sala) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (id_personagem, 1000, 500, 0, 50, 100, 1, 10, 'Normal', 100, 1))
        self.conn.commit()
        cursor.close()

    def get_registered_players(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_personagem, nome FROM Personagem WHERE tipo = 'PC'")
        jogadores = [row for row in cursor.fetchall()]
        cursor.close()
        return jogadores
    
    def get_player_id(self, player_id):
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT nome FROM Personagem WHERE id_personagem = %s", (player_id,))
        player = cursor.fetchone()
        cursor.close()
        return player[0]

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
        print(player_id)
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
    
    def create_tables(self):
        """Cria as tabelas Personagem e PC se não existirem."""
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Personagem (
                    id_personagem SERIAL PRIMARY KEY NOT NULL,
                    nome VARCHAR(50) NOT NULL,
                    descricao VARCHAR(50) NOT NULL,
                    tipo VARCHAR(3) NOT NULL CHECK (tipo IN ('PC', 'NPC'))
                );
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS PC (
                    id_personagem SERIAL PRIMARY KEY REFERENCES Personagem(id_personagem),
                    hp INT NOT NULL CHECK (hp BETWEEN 0 AND 1000),
                    mp INT NOT NULL CHECK (mp BETWEEN 0 AND 1000),
                    xp INT NOT NULL CHECK (xp BETWEEN 0 AND 1000),
                    absorcao INT NOT NULL CHECK (absorcao BETWEEN 0 AND 1000),
                    atk INT NOT NULL CHECK (atk BETWEEN 0 AND 1000),
                    lvl INT NOT NULL CHECK (lvl BETWEEN 1 AND 1000),
                    luck INT NOT NULL CHECK (luck BETWEEN 0 AND 1000),
                    combat_status VARCHAR(10) CHECK (combat_status IN ('Confuso', 'Envenenado', 'Normal')),
                    coins INT NOT NULL CHECK (coins BETWEEN 0 AND 1000),
                    id_sala INT NOT NULL REFERENCES Sala(id_sala)
                );
            ''')
            
            conn.commit()
            print("Tabelas verificadas e criadas, se necessário.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")
        finally:
            cursor.close()
            conn.close()