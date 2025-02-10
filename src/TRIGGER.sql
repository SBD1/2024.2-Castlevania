CREATE OR REPLACE FUNCTION atualizar_status_combate_pc()
RETURNS TRIGGER AS $$
BEGIN
    -- Atualiza o status de combate do PC com base no resultado do combate
    IF NEW.resultado = 'derrotado' THEN
        UPDATE PC
        SET combat_status = 'Envenenado' -- Exemplo de status após derrota
        WHERE id_personagem = NEW.id_pc;
    ELSIF NEW.resultado = 'venceu' THEN
        UPDATE PC
        SET combat_status = 'Normal' -- Retorna ao normal após vitória
        WHERE id_personagem = NEW.id_pc;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_atualizar_status_combate_pc
AFTER INSERT ON Combate
FOR EACH ROW
EXECUTE FUNCTION atualizar_status_combate_pc();

CREATE OR REPLACE FUNCTION verificar_capacidade_inventario()
RETURNS TRIGGER AS $$
DECLARE
    capacidade_maxima INT := 10; -- Defina a capacidade máxima do inventário
    quantidade_itens INT;
BEGIN
    -- Conta quantos itens o PC já possui no inventário
    SELECT COUNT(*) INTO quantidade_itens
    FROM Inventario
    WHERE id_inventario = NEW.id_inventario;

    -- Verifica se a capacidade máxima foi atingida
    IF quantidade_itens >= capacidade_maxima THEN
        RAISE EXCEPTION 'Capacidade do inventário excedida.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_verificar_capacidade_inventario
BEFORE INSERT ON Inventario
FOR EACH ROW
EXECUTE FUNCTION verificar_capacidade_inventario();

CREATE OR REPLACE FUNCTION valida_tipo_npc()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_TABLE_NAME = 'Mercador' AND NEW.tipo != 'Mercador') THEN
        RAISE EXCEPTION 'O tipo de NPC deve ser Mercador para a tabela Mercador';
    ELSIF (TG_TABLE_NAME = 'Contratante' AND NEW.tipo != 'Contratante') THEN
        RAISE EXCEPTION 'O tipo de NPC deve ser Contratante para a tabela Contratante';
    ELSIF (TG_TABLE_NAME = 'Inimigo' AND NEW.tipo != 'Inimigo') THEN
        RAISE EXCEPTION 'O tipo de NPC deve ser Inimigo para a tabela Inimigo';
    ELSIF (TG_TABLE_NAME = 'Chefe' AND NEW.tipo != 'Chefe') THEN
        RAISE EXCEPTION 'O tipo de NPC deve ser Chefe para a tabela Chefe';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_valida_tipo_npc_mercador
BEFORE INSERT OR UPDATE ON Mercador
FOR EACH ROW
EXECUTE FUNCTION valida_tipo_npc();

CREATE TRIGGER trigger_valida_tipo_npc_contratante
BEFORE INSERT OR UPDATE ON Contratante
FOR EACH ROW
EXECUTE FUNCTION valida_tipo_npc();

CREATE TRIGGER trigger_valida_tipo_npc_inimigo
BEFORE INSERT OR UPDATE ON Inimigo
FOR EACH ROW
EXECUTE FUNCTION valida_tipo_npc();

CREATE TRIGGER trigger_valida_tipo_npc_chefe
BEFORE INSERT OR UPDATE ON Chefe
FOR EACH ROW
EXECUTE FUNCTION valida_tipo_npc();

CREATE OR REPLACE TRIGGER trigger_respawn_inimigo
AFTER DELETE ON InstanciaInimigo
FOR EACH ROW
EXECUTE FUNCTION respawn_inimigo();

CREATE TRIGGER trigger_validar_personagem
BEFORE INSERT OR UPDATE ON Personagem
FOR EACH ROW
EXECUTE FUNCTION validar_personagem();

