import sqlite3

# Conexão com o banco de dados
def conectar_banco():
    return sqlite3.connect('rpg.db')  # Substitua pelo caminho correto do seu banco de dados

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Personagem (
        id_personagem INTEGER PRIMARY KEY,
        nome TEXT,
        hp INTEGER,
        mp INTEGER,
        xp INTEGER,
        coins INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sala (
        id_sala INTEGER PRIMARY KEY,
        nome TEXT,
        descricao TEXT,
        id_sala_conectada INTEGER,
        FOREIGN KEY (id_sala_conectada) REFERENCES Sala (id_sala)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PC (
        id_personagem INTEGER PRIMARY KEY,
        id_sala INTEGER,
        FOREIGN KEY (id_personagem) REFERENCES Personagem (id_personagem),
        FOREIGN KEY (id_sala) REFERENCES Sala (id_sala)
    );
    """)

    conn.commit()

    # Verifica se a tabela Sala está vazia e insere algumas salas básicas
    cursor.execute("SELECT COUNT(*) FROM Sala")
    if cursor.fetchone()[0] == 0:
        # Inserindo algumas salas padrão para testes
        cursor.execute("INSERT INTO Sala (id_sala, nome, descricao, id_sala_conectada) VALUES (0, 'Sala Inicial', 'A sala de início do jogo.', 1);")
        cursor.execute("INSERT INTO Sala (id_sala, nome, descricao, id_sala_conectada) VALUES (1, 'Arena', 'Uma arena para batalhas.', 0);")
        conn.commit()
    conn.close()

# Função para exibir o mapa (salas conectadas)
def exibir_mapa(cursor, id_sala_atual):
    print("\n=== MAPA ===")
    
    # Exibe a descrição da sala atual
    cursor.execute("SELECT nome, descricao FROM Sala WHERE id_sala = ?", (id_sala_atual,))
    sala_atual = cursor.fetchone()

    if sala_atual:
        print(f"Você está em: {sala_atual[0]} - {sala_atual[1]}")
    
    # Exibe as salas conectadas
    cursor.execute("SELECT s.id_sala, s.nome FROM Sala s JOIN Sala s2 ON s.id_sala = s2.id_sala_conectada WHERE s2.id_sala = ?", (id_sala_atual,))
    salas_conectadas = cursor.fetchall()

    if salas_conectadas:
        print("\nSalas conectadas:")
        for sala in salas_conectadas:
            print(f"[{sala[0]}] {sala[1]}")
    else:
        print("Não há salas conectadas.")

# Função para mover o personagem
def mover_personagem(cursor, conn, id_personagem, id_sala_destino):
    cursor.execute("SELECT id_sala FROM Sala WHERE id_sala = ?", (id_sala_destino,))
    sala_existe = cursor.fetchone()

    if not sala_existe:
        print("Sala inválida!")
        return

    cursor.execute("UPDATE PC SET id_sala = ? WHERE id_personagem = ?", (id_sala_destino, id_personagem))
    conn.commit()
    print("Você se moveu para a nova sala.")

# Menu principal
def menu_principal():
    criar_tabelas()  # Chama a função para criar as tabelas
    conn = conectar_banco()
    cursor = conn.cursor()

    id_personagem = 1  # ID do personagem jogável (definido para o exemplo)
    
    # Verifica se o personagem já existe, se não, cria
    cursor.execute("SELECT COUNT(*) FROM Personagem")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Personagem (nome, hp, mp, xp, coins) VALUES ('Jogador', 100, 50, 0, 0)")
        conn.commit()

    cursor.execute("SELECT id_sala FROM PC WHERE id_personagem = ?", (id_personagem,))
    id_sala_atual = cursor.fetchone()[0] if cursor.fetchone() else None

    if not id_sala_atual:
        cursor.execute("INSERT INTO PC (id_personagem, id_sala) VALUES (?, 1)", (id_personagem,))
        conn.commit()
        id_sala_atual = 1  # ID da sala inicial

    while True:
        print("\n=== MENU ===")
        print("1. Exibir Mapa")
        print("2. Mover Personagem")
        print("3. Exibir Status do Personagem")
        print("4. Abrir Baú")
        print("5. Iniciar Combate")
        print("6. Exibir Inventário")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Exibir o mapa
            exibir_mapa(cursor, id_sala_atual)

        elif opcao == "2":
            # Mover personagem
            id_sala_destino = input("Digite o ID da sala para onde deseja ir: ")
            mover_personagem(cursor, conn, id_personagem, int(id_sala_destino))

            # Atualiza a sala atual após mover
            cursor.execute("SELECT id_sala FROM PC WHERE id_personagem = ?", (id_personagem,))
            id_sala_atual = cursor.fetchone()[0]

        elif opcao == "3":
            # Exibir status do personagem
            print("Será implementado depois...")

        elif opcao == "4":
            # Abrir baú
            print("Será implementado depois...")

        elif opcao == "5":
            # Iniciar combate
            print("Será implementado depois...")

        elif opcao == "6":
            # Exibir inventário
            print("Será implementado depois...")

        elif opcao == "7":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida!")

    conn.close()

if __name__ == "__main__":
    menu_principal()
