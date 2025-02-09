# Triggers 

No contexto de bancos de dados, triggers são procedimentos armazenados que são automaticamente executados (ou "disparados") em resposta a determinados eventos em uma tabela, como inserções, atualizações ou exclusões de registros. Eles são utilizados para garantir a integridade dos dados, aplicar regras de negócio automaticamente e evitar inconsistências.

No nosso projeto, utilizamos triggers para automatizar e reforçar algumas regras fundamentais do jogo, como:

- Atualização do status do personagem após um combate, garantindo que seu estado seja ajustado conforme o resultado.
- Verificação da capacidade do inventário, impedindo que um personagem carregue mais itens do que o permitido.
- Validação do tipo de NPC, assegurando que cada personagem não-jogador tenha a classificação correta conforme sua função no jogo.
- Gerenciamento do respawn de inimigos, controlando o reaparecimento de adversários no mundo do jogo.
- Validação de personagens e especializações, evitando que personagens sejam criados ou atualizados com informações inconsistentes.
- Essas triggers desempenham um papel essencial na manutenção da lógica do jogo e na garantia da consistência dos dados, proporcionando uma experiência mais estruturada e fluida para os jogadores.

## 1. Trigger: `trigger_atualizar_status_combate_pc`

**Descrição:**
Atualiza o status de combate do PC com base no resultado do combate registrado na tabela `Combate`.

**Trigger:**
```sql
CREATE TRIGGER trigger_atualizar_status_combate_pc
AFTER INSERT ON Combate
FOR EACH ROW
EXECUTE FUNCTION atualizar_status_combate_pc();
```

**Função Associada:**
```sql
CREATE OR REPLACE FUNCTION atualizar_status_combate_pc()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.resultado = 'derrotado' THEN
        UPDATE PC
        SET combat_status = 'Envenenado'
        WHERE id_personagem = NEW.id_pc;
    ELSIF NEW.resultado = 'venceu' THEN
        UPDATE PC
        SET combat_status = 'Normal'
        WHERE id_personagem = NEW.id_pc;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

---

## 2. Trigger: `trigger_verificar_capacidade_inventario`

**Descrição:**
Garante que a capacidade máxima do inventário de um personagem não seja excedida ao adicionar um novo item.

**Trigger:**
```sql
CREATE TRIGGER trigger_verificar_capacidade_inventario
BEFORE INSERT ON Inventario
FOR EACH ROW
EXECUTE FUNCTION verificar_capacidade_inventario();
```

**Função Associada:**
```sql
CREATE OR REPLACE FUNCTION verificar_capacidade_inventario()
RETURNS TRIGGER AS $$
DECLARE
    capacidade_maxima INT := 10;
    quantidade_itens INT;
BEGIN
    SELECT COUNT(*) INTO quantidade_itens
    FROM Inventario
    WHERE id_inventario = NEW.id_inventario;
    
    IF quantidade_itens >= capacidade_maxima THEN
        RAISE EXCEPTION 'Capacidade do inventário excedida.';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

---

## 3. Trigger: `trigger_valida_tipo_npc_*`

**Descrição:**
Valida o tipo de NPC ao inserir ou atualizar registros nas tabelas `Mercador`, `Contratante`, `Inimigo` e `Chefe`.

**Triggers:**
```sql
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
```

**Função Associada:**
```sql
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
```

---

## 4. Trigger: `trigger_respawn_inimigo`

**Descrição:**
Ativa a função de respawn de inimigos após sua remoção da tabela `InstanciaInimigo`.

**Trigger:**
```sql
CREATE OR REPLACE TRIGGER trigger_respawn_inimigo
AFTER DELETE ON InstanciaInimigo
FOR EACH ROW
EXECUTE FUNCTION respawn_inimigo();
```

---

## 5. Trigger: `trigger_validar_personagem`

**Descrição:**
Valida as regras gerais de criação e atualização de personagens na tabela `Personagem`.

**Trigger:**
```sql
CREATE TRIGGER trigger_validar_personagem
BEFORE INSERT OR UPDATE ON Personagem
FOR EACH ROW
EXECUTE FUNCTION validar_personagem();
```

---

## 6. Trigger: `trigger_validar_pc` e `trigger_validar_npc`

**Descrição:**
Garante que os personagens `PC` e `NPC` sigam suas regras de especialização.

**Triggers:**
```sql
CREATE TRIGGER trigger_validar_pc
BEFORE INSERT OR UPDATE ON PC
FOR EACH ROW
EXECUTE FUNCTION validar_especializacao_personagem();

CREATE TRIGGER trigger_validar_npc
BEFORE INSERT OR UPDATE ON NPC
FOR EACH ROW
EXECUTE FUNCTION validar_especializacao_personagem();
