import sqlite3

# Conexão com o banco de dados
def conectar_banco():
    return sqlite3.connect('rpg.db')  # Substitua pelo caminho correto do seu banco de dados

# Função para exibir o mapa (salas conectadas)
def exibir_mapa(cursor, id_sala_atual):
    print("\n=== MAPA ===")
    cursor.execute("SELECT nome, descricao FROM Sala WHERE id_sala = ?", (id_sala_atual,))
    sala_atual = cursor.fetchone()

    if sala_atual:
        print(f"Você está em: {sala_atual[0]} - {sala_atual[1]}")

    cursor.execute("SELECT id_sala, nome FROM Sala WHERE id_sala_conectada = ?", (id_sala_atual,))
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

# Função para exibir o status do personagem
def exibir_status(cursor, id_personagem):
    print("\n=== STATUS DO PERSONAGEM ===")
    cursor.execute("""
        SELECT p.nome, pc.hp, pc.mp, pc.xp, pc.coins, s.nome
        FROM PC pc
        JOIN Personagem p ON pc.id_personagem = p.id_personagem
        JOIN Sala s ON pc.id_sala = s.id_sala
        WHERE pc.id_personagem = ?
    """, (id_personagem,))
    personagem = cursor.fetchone()

    if personagem:
        print(f"Nome: {personagem[0]}")
        print(f"HP: {personagem[1]} | MP: {personagem[2]} | XP: {personagem[3]} | Coins: {personagem[4]}")
        print(f"Localização: {personagem[5]}")
    else:
        print("Personagem não encontrado!")

# Função para iniciar combate
def iniciar_combate(cursor, conn, id_personagem):
    cursor.execute("""
        SELECT ii.id_instancia, p.nome, ii.vida_atual, ii.atk
        FROM InstanciaInimigo ii
        JOIN Personagem p ON ii.id_inimigo = p.id_personagem
        WHERE ii.id_sala = (SELECT id_sala FROM PC WHERE id_personagem = ?)
    """, (id_personagem,))
    inimigo = cursor.fetchone()

    if inimigo:
        print(f"\nVocê encontrou um inimigo: {inimigo[1]} (HP: {inimigo[2]}, ATK: {inimigo[3]})")
        acao = input("Deseja lutar? (s/n): ")
        if acao.lower() == 's':
            # Simula um combate simples
            cursor.execute("SELECT hp, atk FROM PC WHERE id_personagem = ?", (id_personagem,))
            jogador = cursor.fetchone()
            jogador_hp = jogador[0]
            jogador_atk = jogador[1]

            inimigo_hp = inimigo[2]
            inimigo_atk = inimigo[3]

            while jogador_hp > 0 and inimigo_hp > 0:
                inimigo_hp -= jogador_atk
                if inimigo_hp <= 0:
                    print("Você venceu o combate!")
                    cursor.execute("DELETE FROM InstanciaInimigo WHERE id_instancia = ?", (inimigo[0],))
                    conn.commit()
                    return

                jogador_hp -= inimigo_atk
                if jogador_hp <= 0:
                    print("Você foi derrotado!")
                    return

            cursor.execute("UPDATE PC SET hp = ? WHERE id_personagem = ?", (jogador_hp, id_personagem))
            conn.commit()
        else:
            print("Você fugiu do combate.")
    else:
        print("Não há inimigos nesta sala.")

# Função para abrir baús
def abrir_bau(cursor, conn, id_personagem):
    cursor.execute("""
        SELECT b.id_bau, i.nome, i.descricao
        FROM Bau b
        JOIN InstanciaItem ii ON b.itens = ii.id_instancia_item
        JOIN Item i ON ii.id_item = i.id_item
        WHERE b.id_bau IN (
            SELECT sb.id_bau FROM SalaBau sb
            WHERE sb.id_sala = (SELECT id_sala FROM PC WHERE id_personagem = ?)
        )
    """, (id_personagem,))
    bau = cursor.fetchone()

    if bau:
        print(f"\nVocê encontrou um baú! Contém: {bau[1]} - {bau[2]}")
        acao = input("Deseja pegar o item? (s/n): ")
        if acao.lower() == 's':
            cursor.execute("DELETE FROM Bau WHERE id_bau = ?", (bau[0],))
            conn.commit()
            print("Você pegou o item!")
        else:
            print("Você deixou o baú fechado.")
    else:
        print("Não há baús nesta sala.")

# Função para exibir o inventário do personagem
def exibir_inventario(cursor, id_personagem):
    print("\n=== INVENTÁRIO ===")
    cursor.execute("""
        SELECT i.nome, i.descricao
        FROM Inventario inv
        JOIN InstanciaItem ii ON inv.id_instancia_item = ii.id_instancia_item
        JOIN Item i ON ii.id_item = i.id_item
        WHERE inv.id_personagem = ?
    """, (id_personagem,))
    itens = cursor.fetchall()

    if itens:
        for i, item in enumerate(itens, start=1):
            print(f"{i}. {item[0]} - {item[1]}")
    else:
        print("O inventário está vazio!")

# Menu principal
def menu_principal():
    conn = conectar_banco()
    cursor = conn.cursor()

    id_personagem = 1  # ID do personagem jogável (definido para o exemplo)
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
            cursor.execute("SELECT id_sala FROM PC WHERE id_personagem = ?", (id_personagem,))
            id_sala_atual = cursor.fetchone()[0]
            exibir_mapa(cursor, id_sala_atual)

        elif opcao == "2":
            # Mover personagem
            id_sala_destino = input("Digite o ID da sala para onde deseja ir: ")
            mover_personagem(cursor, conn, id_personagem, int(id_sala_destino))

        elif opcao == "3":
            # Exibir status do personagem
            exibir_status(cursor, id_personagem)

        elif opcao == "4":
            # Abrir baú
            abrir_bau(cursor, conn, id_personagem)

        elif opcao == "5":
            # Iniciar combate
            iniciar_combate(cursor, conn, id_personagem)

        elif opcao == "6":
            # Exibir inventário
            exibir_inventario(cursor, id_personagem)

        elif opcao == "7":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida!")

    conn.close()

if __name__ == "__main__":
    menu_principal()