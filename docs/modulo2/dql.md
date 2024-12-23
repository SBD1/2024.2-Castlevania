# DQL - Data Query Language

DQL é a sigla para Data Query Language. É uma linguagem de consulta de dados que permite aos usuários recuperar dados de um banco de dados. O DQL é usado para consultar os dados armazenados em um banco de dados, como recuperar informações específicas de uma tabela ou visualização. O DQL é uma parte importante do projeto físico do banco de dados, pois permite recuperar os dados armazenados no banco de dados.

### Consulta ao banco de dados

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


<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 23/12/2024 | Primeira versão do DQL | [Márcio Henrique](https://github.com/DeM4rcio)  |


</center>

