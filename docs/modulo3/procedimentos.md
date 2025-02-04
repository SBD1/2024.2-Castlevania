# Procedimentos

Procedimentos (ou Procedures) armazenados são blocos de código SQL pré-compilados que podem ser executados repetidamente no banco de dados. Eles permitem encapsular lógica complexa, melhorar o desempenho ao reduzir a sobrecarga de comunicação entre a aplicação e o banco de dados e garantir a reutilização do código.

No nosso projeto, utilizamos procedimentos armazenados para otimizar e automatizar diversas operações essenciais, como:

- Manipulação do combate, garantindo que as regras de vitória, derrota e status dos personagens sejam aplicadas corretamente.
- Gerenciamento do inventário, permitindo a adição e remoção de itens enquanto se respeita a capacidade máxima.
Criação e especialização de NPCs, assegurando que cada NPC seja criado com as características apropriadas de acordo com sua função no jogo.
- Controle de respawn de inimigos, garantindo que os adversários retornem ao mundo do jogo seguindo as regras definidas.
- Validação de personagens, evitando que informações inconsistentes sejam inseridas ou modificadas no banco de dados.
A adoção de procedimentos armazenados melhora a performance do sistema, reduzindo a carga da aplicação e garantindo a integridade dos dados do jogo de maneira eficiente e organizada.

## Procedimentos Armazenados

### Procedimento: `mover_pc`
```sql
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
        SELECT 1 FROM SalaConexoes
        WHERE (id_sala_origem = v_id_sala_atual AND id_sala_destino = p_id_sala_destino)
           OR (id_sala_origem = p_id_sala_destino AND id_sala_destino = v_id_sala_atual)
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
```

### Procedimento: `concluir_missao`
```sql
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
```

### Procedimento: `comprar_item`
```sql
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
    INSERT INTO Inventario (id_pc, id_instancia_item)
    VALUES (p_id_pc, p_id_instancia_item);

    -- Deduz o valor da compra dos coins do PC
    UPDATE PC
    SET coins = coins - p_valor
    WHERE id_personagem = p_id_pc;

    RAISE NOTICE 'Compra realizada com sucesso!';
END;
$$;
```

## Funções Relacionadas

### Função: `respawn_inimigo`
```sql
CREATE OR REPLACE FUNCTION respawn_inimigo()
RETURNS TRIGGER AS $$
DECLARE
    nova_sala INT;
BEGIN
    SELECT id_sala INTO nova_sala
    FROM Sala
    WHERE id_sala <> OLD.id_sala  
    ORDER BY RANDOM()
    LIMIT 1;

    INSERT INTO InstanciaInimigo (id_inimigo, id_sala, vida_atual, absorcao, atk, habilidade, combat_status)
    VALUES (OLD.id_inimigo, nova_sala, 100, OLD.absorcao, OLD.atk, OLD.habilidade, 'Normal');

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;
```

### Função: `validar_personagem`
```sql
CREATE OR REPLACE FUNCTION validar_personagem() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.tipo = 'PC' THEN
        IF NOT EXISTS (SELECT 1 FROM PC WHERE id_personagem = NEW.id_personagem) THEN
            RAISE EXCEPTION 'Todo Personagem do tipo PC deve ter um registro correspondente na tabela PC';
        END IF;
    ELSIF NEW.tipo = 'NPC' THEN
        IF NOT EXISTS (SELECT 1 FROM NPC WHERE id_personagem = NEW.id_personagem) THEN
            RAISE EXCEPTION 'Todo Personagem do tipo NPC deve ter um registro correspondente na tabela NPC';
        END IF;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### Função: `validar_especializacao_personagem`
```sql
CREATE OR REPLACE FUNCTION validar_especializacao_personagem() RETURNS TRIGGER AS $$
BEGIN
    IF TG_TABLE_NAME = 'pc' THEN
        IF NOT EXISTS (SELECT 1 FROM Personagem WHERE id_personagem = NEW.id_personagem AND tipo = 'PC') THEN
            RAISE EXCEPTION 'Não é possível inserir um PC sem um registro correspondente na tabela Personagem';
        END IF;
    
    ELSIF TG_TABLE_NAME = 'npc' THEN
        IF NOT EXISTS (SELECT 1 FROM Personagem WHERE id_personagem = NEW.id_personagem AND tipo = 'NPC') THEN
            RAISE EXCEPTION 'Não é possível inserir um NPC sem um registro correspondente na tabela Personagem';
        END IF;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```
