# DML - Data Manipulation Language

ou Linguagem de Manipulação de Dados, um conjunto de comandos SQL que permite a manipulação de dados em bancos de dados.

----

```sql

BEGIN TRANSACTION;

INSERT INTO Mundo (id_mundo, nome, data) VALUES 
(1, 'Mundo 1', '2024-01-01');


INSERT INTO Regiao (id_regiao, id_regiao_conectada, id_mundo, nome, descricao, dificuldade) VALUES 
(1, NULL, 1, 'Jardim do castelo', 'Jardim do castelo do dracula.', 'Fácil'),
(2, 1, 1, 'Entrada do Castelo', 'Entrada do castelo.', 'Médio');

INSERT INTO Sala (id_sala, id_sala_conectada, id_regiao, nome, descricao) VALUES 
(1, NULL, 1, 'Jardim do castelo', 'O início da aventura.'),
(2, 1, 1, 'Entrada do castelo', 'Local belo cheios de objetos de ouro.');

INSERT INTO Personagem (id_personagem, nome, descricao, tipo) VALUES 
(1, 'Guerreiro', 'Um bravo lutador.', 'PC'),
(2, 'Mercador', 'Vendedor de itens raros.', 'NPC'),
(3, 'Morcego', 'Um inimigo pequeno e traiçoeiro.', 'NPC');


INSERT INTO PC (id_personagem, hp, mp, xp, absorcao, atk, lvl, luck, combat_status, coins, id_sala) VALUES 
(1, 1000, 500, 0, 50, 100, 1, 10, 'Normal', 100, 1);

INSERT INTO NPC (id_personagem, tipo) VALUES 
(2, 'Mercador'),
(3, 'Inimigo');

INSERT INTO Mercador (id_personagem, id_sala) VALUES 
(2, 2);

INSERT INTO Inimigo (id_personagem, hp, xp, absorcao, atk, habilidade) VALUES 
(3, 50, 10, 5, 10, 5);

INSERT INTO InstanciaInimigo (id_instancia, id_inimigo, id_sala, vida_atual, absorcao, atk, habilidade, combat_status) VALUES 
(1, 3, 3, 50, 5, 10, 5, 'Normal');

INSERT INTO Item (id_item, nome, descricao) VALUES 
(1, 'Espada de Ferro', 'Uma espada básica.'),
(2, 'Poção de Cura', 'Recupera 50 pontos de vida.');

INSERT INTO InstanciaItem (id_instancia_item, id_item, id_sala) VALUES 
(1, 1, 1),
(2, 2, 2);

INSERT INTO Bau (id_bau, itens) VALUES 
(1, 1);


INSERT INTO SalaBau (id_bau, id_sala) VALUES 
(1, 1);

INSERT INTO Missao (id_missao, nome, qnt_xp, descricao) VALUES 
(1, 'Derrotar o Morcegos', 50, 'Encontre e elimine os morcegos no castelo.');


INSERT INTO MissoesRealizadas (id_missao, id_pc) VALUES 
(1, 1);


INSERT INTO Combate (id_combate, id_pc, id_inimigo, resultado) VALUES 
(1, 1, 1, 'venceu');

COMMIT;
```

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 22/12/2024 | Primeira versão do DML | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `1.1`  | 22/12/2024 | Complementando a primeira versão do DML | [Márcio Henrique](https://github.com/DeM4rcio)  |

</center>
