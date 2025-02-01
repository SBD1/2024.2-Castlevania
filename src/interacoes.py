def exibir_dialogo(db_controller, dialogo_id, player_id):
    db_controller.connect()
    cursor = db_controller.conn.cursor()
    cursor.execute("SELECT texto FROM Dialogo WHERE id_dialogo = %s AND id_personagem = %s", (dialogo_id, player_id))
    dialogo = cursor.fetchone()
    cursor.close()
   
    if dialogo:
        print(f"[Diálogo] {dialogo[0]}")
    else:
        print("Diálogo não encontrado.")

def exibir_dialogo_mercador(db_controller, dialogo_id):
    db_controller.connect()
    cursor = db_controller.conn.cursor()
    cursor.execute("SELECT texto FROM Dialogo WHERE id_dialogo = %s", (dialogo_id,))
    dialogo = cursor.fetchone()
    cursor.close()
   
    if dialogo:
        print(f"[Mercador] {dialogo[0]}")
    else:
        print("Diálogo do Mercador não encontrado.")

def exibir_dialogo_contratante(db_controller, dialogo_id):
    db_controller.connect()
    cursor = db_controller.conn.cursor()
    cursor.execute("SELECT texto FROM Dialogo WHERE id_dialogo = %s", (dialogo_id,))
    dialogo = cursor.fetchone()
    cursor.close()
   
    if dialogo:
        print(f"[Contratante] {dialogo[0]}")
    else:
        print("Diálogo do Contratante não encontrado.")