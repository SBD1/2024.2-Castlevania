# DQL - Data Query Language

DQL é a sigla para Data Query Language. É uma linguagem de consulta de dados que permite aos usuários recuperar dados de um banco de dados. O DQL é usado para consultar os dados armazenados em um banco de dados, como recuperar informações específicas de uma tabela ou visualização. O DQL é uma parte importante do projeto físico do banco de dados, pois permite recuperar os dados armazenados no banco de dados.

### Consulta ao banco de dados

#### **1. Listar todos os mundos**

```sql
 
  SELECT * FROM Mundo;

```

####  **2. Listar todas as regiões e seus respectivos mundos**

```sql
SELECT Regiao.nome AS regiao, Mundo.nome AS mundo
FROM Regiao
JOIN Mundo ON Regiao.id_mundo = Mundo.id_mundo;

```
 
#### **3. Detalhes de um personagem específico**

```sql
  SELECT *
  FROM Personagem
  WHERE id_personagem = %s;

```
 

#### **4. Selecionar jogadores registrados:**
```sql

   SELECT nome FROM Personagem;

```

#### **5. Selecionar Missão do jogador:**
```sql

   SELECT nome FROM Missao WHERE id_missao = %s;
   
```

#### **6. Consultar Vida do jogador:**
```sql
   SELECT vida FROM Personagem WHERE id = %s;
```

#### **7. Consultar salas conectadas a partir do personagem:**
```sql

  SELECT id_sala_destino, direcao, descricao_conexao
  FROM Conexao
  WHERE id_sala_origem = (
    SELECT id_sala
    FROM PC
    WHERE id_personagem = %s
  );

```

#### **8. Quantidade de Inimigos na sala**

```sql

  SELECT COUNT(Instancia_inimigo.id_instancia)
  FROM Instancia_inimigo
  WHERE id_sala = (
    SELECT id_sala
    FROM Personagem
    WHERE id_pc = %s
  );

```

#### **9. Atualizar o resultado do combate**

```sql

 UPDATE Combate SET resultado = "venceu" WHERE id_combate = %s;

```

#### **10. Consultar o total gasto em transações de venda**

```sql

  SELECT SUM(Valor) FROM Transacao WHERE tipo = 'venda'

```

#### **11. Atualizar status de combate do chefe**

```sql

  UPDATE Chefe SET combat_status = "confuso" WHERE id_personagem = %s

```

>OBS: Todos os status do chefe ou inimigo terá como base esse script, tal que será setado a depender da ação do personagem **UPDATE Chefe SET "Atributo a ser atualizado" WHERE id_personagem = %s**, por exemplo: O personagem reliza um ataque que diminui em 10 de HP do chefe, então o script de update seria dessa forma: **UPDATE Chefe SET hp = "Novo valor de vida" WHERE id_personagem = %s**


#### **12. Listar todos os itens do inventário do personagem**

```sql

  SELECT Instancia_item from inventario WHERE id_inventario = (SELECT id_personagem FROM PC WHERE id = %s)

```

#### **13. Listar todos os itens de um bau**

```sql

  SELECT itens from Bau WHERE id_bau = %s

```

#### **14. Listar missões pendentes do personagem**

```sql

  SELECT PC.nome AS personagem, MissaoPrincipal.nome AS missao_dependente
  FROM MissaoPrincipal
  LEFT JOIN MissoesRealizadas ON MissaoPrincipal.id_missao = MissoesRealizadas.id_missao
  JOIN PC ON PC.id_personagem = MissoesRealizadas.id_pc
  WHERE MissoesRealizadas.id_missao IS NULL;

```

#### **15. Missões que trazem mais recompensas**

```sql

  SELECT Missao.nome, Missao.qnt_xp, Missao.descricao
  FROM Missao
  ORDER BY Missao.qnt_xp DESC
  LIMIT 5;


```




<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 23/12/2024 | Primeira versão do DQL | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `1.1`  | 23/12/2024 | Acresentando consultas  | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `1.2`  | 12/01/2025 | Acresentando consultas  | [Márcio Henrique](https://github.com/DeM4rcio)  |
| `1.3`  | 01/02/2025 | Acresentando consultas  | [Diego Carlito](https://github.com/DiegoCarlito)  |
</center>

