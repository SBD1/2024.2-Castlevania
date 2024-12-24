# DQL - Data Query Language

DQL é a sigla para Data Query Language. É uma linguagem de consulta de dados que permite aos usuários recuperar dados de um banco de dados. O DQL é usado para consultar os dados armazenados em um banco de dados, como recuperar informações específicas de uma tabela ou visualização. O DQL é uma parte importante do projeto físico do banco de dados, pois permite recuperar os dados armazenados no banco de dados.

### Consulta ao banco de dados

 **Listar todos os mundos**

```sql
 
  SELECT * FROM Mundo;

```

  **Listar todas as regiões e seus respectivos mundos**

```sql
SELECT Regiao.nome AS regiao, Mundo.nome AS mundo
FROM Regiao
JOIN Mundo ON Regiao.id_mundo = Mundo.id_mundo;

```
 
 **Detalhes de um personagem específico**

```sql
  SELECT *
  FROM Personagem
  WHERE id_personagem = %s;

```
 

 **Selecionar jogadores registrados:**
```sql

   SELECT nome FROM Personagem;

```

 **Selecionar Missão do jogador:**
```sql

   SELECT nome FROM Missao WHERE id_missao = %s;
   
```

 **Consultar Vida do jogador:**
```sql
   SELECT vida FROM Personagem WHERE id = %s;
```

 **Consultar salas conectadas a partir do personagem:**
```sql

    SELECT sala.id_sala
    FROM Sala sala
    JOIN Personagem personagem ON personagem.id_sala = personagem.id_sala
    WHERE personagem.id_sala_conectada = (
        SELECT personagem.id_sala_conectada
        FROM Sala sala2
        WHERE sala2.id_sala = personagem.id_sala
    );

```

**Quantidade de Inimigos na sala**

```sql

  SELECT COUNT(Instancia_inimigo.id_instancia)
  FROM Instancia_inimigo
  WHERE id_sala = (
    SELECT id_sala
    FROM Personagem
    WHERE id_pc = %s
  ) 

```

**Atualizar o resultado do combate**

```sql

 UPDATE Combate SET resultado = "venceu" WHERE id_combate = %s;

```




<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 23/12/2024 | Primeira versão do DQL | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `1.1`  | 23/12/2024 | Acresentando consultas  | [Márcio Henrique](https://github.com/DeM4rcio)  |

</center>

