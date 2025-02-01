CREATE OR REPLACE PROCEDURE mover_pc(
    p_id_pc INT,
    p_id_sala_destino INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_sala_atual INT;
    v_conexao_existe BOOLEAN;
BEGIN
    -- Obtém a sala atual do PC
    SELECT id_sala INTO v_id_sala_atual
    FROM PC
    WHERE id_personagem = p_id_pc;

    -- Verifica se a sala de destino está conectada à sala atual
    SELECT EXISTS(
        SELECT 1 FROM Sala
        WHERE id_sala = p_id_sala_destino
        AND id_sala_conectada = v_id_sala_atual
    ) INTO v_conexao_existe;

    IF NOT v_conexao_existe THEN
        RAISE EXCEPTION 'Movimento inválido: a sala de destino não está conectada à sala atual.';
    END IF;

    -- Atualiza a sala do PC
    UPDATE PC
    SET id_sala = p_id_sala_destino
    WHERE id_personagem = p_id_pc;

    RAISE NOTICE 'PC movido para a sala %.', p_id_sala_destino;
END;
$$;

CREATE OR REPLACE PROCEDURE concluir_missao(
    p_id_missao INT,
    p_id_pc INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_xp_recompensa INT;
BEGIN
    -- Obtém a recompensa de XP da missão
    SELECT qnt_xp INTO v_xp_recompensa
    FROM Missao
    WHERE id_missao = p_id_missao;

    -- Marca a missão como concluída
    INSERT INTO MissoesRealizadas (id_missao, id_pc)
    VALUES (p_id_missao, p_id_pc);

    -- Concede a recompensa de XP ao PC
    UPDATE PC
    SET xp = xp + v_xp_recompensa
    WHERE id_personagem = p_id_pc;

    RAISE NOTICE 'Missão concluída! % XP concedido ao PC.', v_xp_recompensa;
END;
$$;

CREATE OR REPLACE PROCEDURE comprar_item(
    p_id_pc INT,
    p_id_mercador INT,
    p_id_instancia_item INT,
    p_valor INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_coins_pc INT;
BEGIN
    -- Verifica se o PC tem coins suficientes
    SELECT coins INTO v_coins_pc
    FROM PC
    WHERE id_personagem = p_id_pc;

    IF v_coins_pc < p_valor THEN
        RAISE EXCEPTION 'Coins insuficientes para realizar a compra.';
    END IF;

    -- Realiza a transação
    INSERT INTO Transacao (id_mercador, id_pc, valor, tipo)
    VALUES (p_id_mercador, p_id_pc, p_valor, 'compra');

    -- Adiciona o item ao inventário do PC
    INSERT INTO Inventario (id_inventario, id_instancia_item)
    VALUES (p_id_pc, p_id_instancia_item);

    -- Deduz o valor da compra dos coins do PC
    UPDATE PC
    SET coins = coins - p_valor
    WHERE id_personagem = p_id_pc;

    RAISE NOTICE 'Compra realizada com sucesso!';
END;
$$;