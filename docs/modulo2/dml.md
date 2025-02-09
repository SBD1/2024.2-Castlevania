# DML - Data Manipulation Language

A Linguagem de Manipulação de Dados, e um conjunto de comandos SQL que permite a manipulação de dados em bancos de dados.

----

```sql

BEGIN TRANSACTION;

-- Inserções na tabela Mundo
INSERT INTO Mundo (id_mundo, nome, data) VALUES 
(1, 'Mundo 1', '2024-01-01');

-- Inserções na tabela Regiao
INSERT INTO Regiao (id_regiao, id_regiao_conectada, id_mundo, nome, descricao, dificuldade) VALUES 
(1, NULL, 1, 'Jardim do castelo', 'Jardim do castelo do dracula.', 'Fácil'),
(2, 1, 1, 'Entrada do Castelo', 'Entrada do castelo.', 'Médio');

-- Inserções na tabela Sala
INSERT INTO Sala (id_sala, id_regiao, nome, descricao) VALUES 
(1, 1, 'Jardim do castelo', 'O início da aventura.'),
(2, 1, 'Entrada do castelo', 'Local belo cheios de objetos de ouro.');

-- Inserções na tabela Conexao
INSERT INTO Conexao (id_conexao, id_sala_origem, id_sala_destino, direcao, descricao_conexao) VALUES 
(1, 1, 2, 'Norte', 'Um corredor escuro leva à entrada do castelo.'),
(2, 2, 1, 'Sul', 'Um corredor escuro leva de volta ao jardim.');

-- Inserções na tabela Personagem
INSERT INTO Personagem (id_personagem, nome, descricao, tipo) VALUES 
(1, 'Guerreiro', 'Um bravo lutador.', 'PC'),
(2, 'Mercador', 'Vendedor de itens raros.', 'NPC'),
(3, 'Morcego', 'Um inimigo pequeno e traiçoeiro.', 'NPC');

-- Inserções na tabela PC
INSERT INTO PC (id_personagem, hp, mp, xp, absorcao, atk, lvl, luck, combat_status, coins, id_sala) VALUES 
(1, 1000, 500, 0, 50, 100, 1, 10, 'Normal', 100, 1);

-- Inserções na tabela NPC
INSERT INTO NPC (id_personagem, tipo) VALUES 
(2, 'Mercador'),
(3, 'Inimigo');

-- Inserções na tabela Mercador
INSERT INTO Mercador (id_personagem, id_sala) VALUES 
(2, 2);

-- Inserções na tabela Inimigo
INSERT INTO Inimigo (id_personagem, hp, xp, absorcao, atk, habilidade) VALUES 
(3, 50, 10, 5, 10, 5);

-- Inserções na tabela InstanciaInimigo
INSERT INTO InstanciaInimigo (id_instancia, id_inimigo, id_sala, vida_atual, absorcao, atk, habilidade, combat_status) VALUES 
(1, 3, 2, 50, 5, 10, 5, 'Normal');

-- Inserções na tabela Item
INSERT INTO Item (id_item, nome, descricao) VALUES 
(1, 'Espada de Ferro', 'Uma espada básica.'),
(2, 'Poção de Cura', 'Recupera 50 pontos de vida.');

-- Inserções na tabela InstanciaItem
INSERT INTO InstanciaItem (id_instancia_item, id_item, id_sala) VALUES 
(1, 1, 1),
(2, 2, 2);

-- Inserções na tabela Bau
INSERT INTO Bau (id_bau, itens) VALUES 
(1, 1);

-- Inserções na tabela SalaBau
INSERT INTO SalaBau (id_bau, id_sala) VALUES 
(1, 1);

-- Inserções na tabela Missao
INSERT INTO Missao (id_missao, nome, qnt_xp, descricao) VALUES 
(1, 'Derrotar o Morcegos', 50, 'Encontre e elimine os morcegos no castelo.');

-- Inserções na tabela MissoesRealizadas
INSERT INTO MissoesRealizadas (id_missao, id_pc) VALUES 
(1, 1);

-- Inserções na tabela Combate
INSERT INTO Combate (id_combate, id_pc, id_inimigo, resultado) VALUES 
(1, 1, 1, 'venceu');

-- Inserções na tabela Efeito
INSERT INTO Efeito (id_efeito, alcance, duracao) VALUES 
(1, 0, 1);

-- Inserções na tabela Consumivel
INSERT INTO Consumivel (id_item, id_efeito, quantidade) VALUES 
(2, 1, 1);

-- Inserções na tabela Chave
INSERT INTO Chave (id_item, bau_requerido) VALUES 
(1, 'Bau1');

-- Inserções na tabela Arma
INSERT INTO Arma (id_item, dano) VALUES 
(1, 100);

-- Inserções na tabela Habilidade
INSERT INTO Habilidade (id_habilidade, id_habilidade_dependente, id_grimorio, efeito, tipo, custo_mp) VALUES 
(1, 1, 1, 'Cura', 'Suporte', 50);

-- Inserções na tabela Grimorio
INSERT INTO Grimorio (id_item, xp_necessario, id_habilidade) VALUES 
(1, 100, 1);

-- Inserções na tabela Contrato
INSERT INTO Contrato (id_missao, id_dependencia, id_contratante) VALUES 
(1, 1, 2);

COMMIT;

```

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 22/12/2024 | Primeira versão do DML | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `1.1`  | 22/12/2024 | Complementando a primeira versão do DML | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `1.1`  | 12/01/2024 | Complementando DML | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `2.0`  | 01/02/2025 | Segunda versão do DML | [Diego Carlito](https://github.com/DiegoCarlito)  |
</center>
