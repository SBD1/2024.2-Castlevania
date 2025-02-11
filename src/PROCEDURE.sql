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

CREATE OR REPLACE FUNCTION respawn_inimigo()
RETURNS TRIGGER AS $$
DECLARE
    nova_sala INT;
    id_instancia INT;  -- Declara a variável id_instancia
BEGIN
    -- Seleciona uma sala diferente da atual para o inimigo
    SELECT id_sala INTO nova_sala
    FROM Sala
    WHERE id_sala <> OLD.id_sala  
    ORDER BY RANDOM()
    LIMIT 1;

    -- Insere uma nova instância de inimigo (sem incluir o id_instancia no INSERT)
    INSERT INTO InstanciaInimigo (id_inimigo, id_sala, vida_atual, absorcao, atk, habilidade, combat_status)
    VALUES (OLD.id_inimigo, nova_sala, 100, OLD.absorcao, OLD.atk, OLD.habilidade, 'Normal')
    RETURNING InstanciaInimigo.id_instancia INTO id_instancia;  -- Agora a sequência vai gerar o id_instancia automaticamente

    -- Exibe uma mensagem no log
    RAISE NOTICE 'A instância % foi movida para a sala %', id_instancia, nova_sala;

    -- Retorna OLD ou NEW para que a trigger continue funcionando corretamente
    RETURN OLD;  -- Ou RETURN NEW dependendo da lógica
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION validar_personagem() RETURNS TRIGGER AS $$
DECLARE
    novo_nome VARCHAR;
BEGIN
    -- Gera o nome do personagem se não for informado
    IF NEW.nome IS NULL THEN
        RAISE EXCEPTION 'Erro: O nome do personagem não pode ser nulo';
    ELSE
        novo_nome := NEW.nome;
    END IF;

    -- 🔹 Se o nome do personagem já existe em PC ou NPC, retorna NEW sem realizar a inserção
    IF EXISTS (SELECT 1 FROM Personagem WHERE nome = novo_nome)
        THEN
        RAISE EXCEPTION 'Erro: O personagem já existe na tabela PC ou NPC';
    END IF;

    -- Retorna o NEW para permitir a inserção
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
