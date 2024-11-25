# DD - Dicionário de Dados

## Introdução

Um dicionário de dados é um recurso essencial na área da ciência de dados e da informática. Ele funciona como um catálogo ou compilação de informações sobre os dados utilizados em um sistema, banco de dados, projeto de pesquisa ou qualquer contexto em que a manipulação e interpretação de dados sejam necessárias.


## Entidade: Exemplo

**Descrição**: Esta entidade serve como um modelo para ilustrar como as informações são organizadas e descritas em um banco de dados. Inclui variáveis típicas, tipos de dados, valores permitidos e restrições.

**Observação**: Esta tabela é usada para exemplificar como preencher um dicionário de dados. Os valores e descrições são fictícios.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-exemplo        | int        | Código de identificação do exemplo           | 1-1000             | PK, Not Null           |
| nome              | varchar(50)| Nome associado ao exemplo                  | a-z, A-Z           | Not Null               |
| data-criacao      | date       | Data em que o exemplo foi criado            | Data válida        | Not Null               |
| valor             | decimal(10,2)| Valor numérico do exemplo                   | 0.00-9999.99       | Not Null, Check (>= 0) |
| ativo             | boolean    | Indicador se o exemplo está ativo ou não    | True, False        | Not Null               |

  <font size="3"><p style="text-align: center"><b>Autores:</b> <a href="https://github.com/DiegoCarlito">Diego Carlito</a></font>

<details>
  <summary>Descrição de cada título da coluna</summary>

- "Nomes das variáveis": Identificadores específicos para cada conjunto de dados na tabela, como "id-exemplo" e "nome".<br>

- "Descrições das variáveis": Explicações sobre o que cada variável representa, como "Código de identificação do exemplo" e "Nome associado ao exemplo".<br>

- "Tipos de dados": Tipos de informações armazenadas, como inteiro, texto, data e decimal.<br>

- "Valores permitidos" : Intervalos ou opções permitidas para as variáveis, como "1-1000" para um identificador ou "True, False" para um indicador booleano.<br>

- "Restrições de Domínio": Inclui as restrições adicionais aplicáveis, como "PK" (chave primária), "Not Null" (não pode ser nulo), e "Check" (restrições de valor, como valores mínimos e máximos).

</details>

### Entidade: Personagem

**Descrição**: Representa os personagens no jogo, podendo ser jogadores (PC) ou não jogadores (NPC).

**Observação**: Esta tabela não possui chave estrangeira.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_personagem        | int        | Código de identificação do personagem           | 1-1000             | PK, Not Null           |
| nome              | varchar(50)| Nome associado ao personagem                  | a-z, A-Z           | Not Null               |
| descr      | varchar(50)       | Descrição do personagem            | a-z, A-Z        | Not Null               |
| tipo             | varchar(50) | Tipo de personagem                   | a-z, A-Z       | Not Null |


#### PC

**Descrição**: Contém informações específicas dos personagens jogáveis.

**Observação**: Esta tabela contém chave estrangeira da tabela Sala.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| hp       | int        | Ponto de vida do pc           | 1-1000             | Not Null           |
| mp             | int | Pontos de mana do pc                  | 1-1000          | Not Null               |
| xp      | int       | Ponto de experiência do pc            | 1-1000        | Not Null               |
| absorção            | int | Redução do dano que o pc recebe                   | 1-1000       | Not Null |
| atk             | int    | Quantidade de dano básica do pc    | 1-1000        | Not Null               |
| lvl             | int    | Level do pc    | 1-1000        | Not Null               |
| luck             | int    | Indica a sorte do pc   | 1-1000        | Not Null               |
| combat_status             | varchar(50)    | Indica o estado do pc("Confuso", "Envenenado", "Normal")    | a-z, A-Z       | Not Null               |
| coins             | int    | Indica a quantidaade de moedas do pc    | 1-1000       | Not Null               |
| id_sala             | int    | Indica a sala em o pc está    | 1-1000        | FK, Not Null               |


#### NPC

**Descrição**: Contém informações específicas dos personagens não jogáveis.

**Observação**: Esta tabela não contém chave estrangeira.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| tipo       | varchar(50)        | Indica o tipo de NPC           | a-z, A-Z             | Not Null           |

##### Mercador

**Descrição**: NPC que comercializa itens.

**Observação**: Esta tabela contém chave estrangeira da tabela Sala.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_sala        | int        | Indica a sala em que o mercador está           | 1-1000             | FK, Not Null           |

##### Contratante

**Descrição**: NPC que fornece contratos para o jogador.

**Observação**: Esta tabela contém chave estrangeira da tabela Sala.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_sala        | int        | Indica a sala em que o contratante está            | 1-1000             | FK, Not Null           |

##### Inimigo

**Descrição**: NPC que participa de combates com o jogador.

**Observação**: Esta tabela não possui chaves estrangeiras.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| hp       | int        | Pontos de vida do inimigo           | 1-1000             | Not Null           |
| xp              | int | Pontos de experiência fornecidos ao derrotar o inimigo                  | 1-1000           | Not Null               |
| absorção      | int       | Redução do dano que o inimigo recebe            | 1-1000        | Not Null               |
| atk             | int | Dano básico causado pelo inimigo                   | 1-1000       | Not Null |
| habilidade            | int    | Acréscimo no dano básico do inimigo    | 1-1000        | Not Null               |

##### Chefe

**Descrição**: NPC mais desafiador, geralmente finalizando uma região ou missão.

**Observação**: Esta tabela contém chaves estrangeiras das tabelas Sala e Item.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| hp       | int        | Pontos de vida do chefe           | 1-1000             | Not Null           |
| xp              | int | Pontos de experiência fornecidos ao derrotar o chefe                  | 1-1000           | Not Null               |
| lvl              | int | Nível do chefe                  | 1-1000           | Not Null               |
| status              | varchar(50) | Estado do chefe("Confuso", "Envenenado", "Normal")                  | 1-1000           | Not Null               |
| absorção      | int       | Redução do dano que o chefe recebe            | 1-1000        | Not Null               |
| atk             | int | Dano básico causado pelo inimigo                   | 1-1000       | Not Null |
| item_especial            | int    | Item dropado pelo chefe    | 1-1000        | FK, Not Null               |
| id_sala            | int    | Sala em que o chefe está    | 1-1000        | FK, Not Null               |

---

### Entidade: Instância Inimigo

**Descrição**: Esta entidade serve como um modelo para ilustrar como as informações são organizadas e descritas em um banco de dados. Inclui variáveis típicas, tipos de dados, valores permitidos e restrições.

**Observação**: Esta tabela é usada para exemplificar como preencher um dicionário de dados. Os valores e descrições são fictícios.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-exemplo        | int        | Código de identificação do exemplo           | 1-1000             | PK, Not Null           |
| nome              | varchar(50)| Nome associado ao exemplo                  | a-z, A-Z           | Not Null               |
| data-criacao      | date       | Data em que o exemplo foi criado            | Data válida        | Not Null               |
| valor             | decimal(10,2)| Valor numérico do exemplo                   | 0.00-9999.99       | Not Null, Check (>= 0) |
| ativo             | boolean    | Indicador se o exemplo está ativo ou não    | True, False        | Not Null               |

---

### Entidade: Exemplo

**Descrição**: Esta entidade serve como um modelo para ilustrar como as informações são organizadas e descritas em um banco de dados. Inclui variáveis típicas, tipos de dados, valores permitidos e restrições.

**Observação**: Esta tabela é usada para exemplificar como preencher um dicionário de dados. Os valores e descrições são fictícios.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-exemplo        | int        | Código de identificação do exemplo           | 1-1000             | PK, Not Null           |
| nome              | varchar(50)| Nome associado ao exemplo                  | a-z, A-Z           | Not Null               |
| data-criacao      | date       | Data em que o exemplo foi criado            | Data válida        | Not Null               |
| valor             | decimal(10,2)| Valor numérico do exemplo                   | 0.00-9999.99       | Not Null, Check (>= 0) |
| ativo             | boolean    | Indicador se o exemplo está ativo ou não    | True, False        | Not Null               |


---

### Entidade: Bau

**Descrição**: Baus contidos no jogo

**Observação**: Esta entidade irá armazenas os baus que o jogo oferece, tendo chave estrangeira na tabela Instância item

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-bau   | int        | Código de identificação do bau     | 1-1000             | PK, Not Null           |
| itens   | int        | Código de instância de itens     | 1-1000             | FK, Not Null           |



---

### Entidade: Baus

**Descrição**: Baus contidos nas salas

**Observação**: Esta entidade irá armazenas os baus em suas salas, tendo chave estrangeira nas tabelas Bau e Sala

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-sala   | int        | Código de identificação da sala     | 1-1000             | PK,FK, Not Null           |
| id-bau   | int        | Código de identificação do bau     | 1-1000             | PK,FK, Not Null           |



---

### Entidade: Sala 

**Descrição**: A sala é contido nas regiões

**Observação**: Esta entidade irá armazenas as salas contidas do game, tendo chaves estrangeiras contidas nas tabelas Sala e Região

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-sala   | int        | Código de identificação da sala     | 1-1000             | PK, Not Null           |
| id-sala-conectada   | int        | Código de identificação da sala conectada      | 1-1000             | FK, Not Null           |
| id-regiao    | int        | Código de identificação da regiao      | 1-1000             | FK, Not Null           |
| nome    | varchar(200)      | nome da sala         | a-z, A-Z            |Not Null           |
| descr   | varchar(200)      | descrição da sala      | a-z, A-Z            |Not Null           |


---

### Entidade: Região 

**Descrição**: O jogo é dividido em várias regiões

**Observação**: Esta entidade irá armazenas as regiões contidas do game, tendo chaves estrangeiras contidas nas tabelas Região e Mundo

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-regiao    | int        | Código de identificação da regiao      | 1-1000             | PK, Not Null           |
| id-região-conectada    | int       | Código de identificação da região conectada         | 1-1000            |FK, Not Null           |
| id-mundo   | int       | Código de identificação do mundo        | 1-1000            |FK, Not Null           |
| nome    | varchar(200)      | nome do mundo         | a-z, A-Z            |Not Null           |
| descr   | varchar(200)      | descrição da região      | a-z, A-Z            |Not Null           |
| dificuldade  | varchar(50)      | dificuldade da região (fácil, médio, difícil)     | a-z, A-Z            |Not Null           |


---

### Entidade: Mundo 

**Descrição**: Mundo é a visão mais macro do mapa do mud

**Observação**: Esta entidade irá armazenas os mundos contidos do game

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-mundo    | int        | Código de identificação do mundo      | 1-1000             | PK, Not Null           |
| nome    | varchar(200)      | nome do mundo         | a-z, A-Z            |Not Null           |
| data   | date       | data em que o mundo foi criado      | Data válida            |Not Null           |


---

### Entidade: Diálogo

**Descrição**: Dialogos do mud

**Observação**: Esta entidade irá armazenas todos os dialogos dos personagens, tendo uma chave estrangeira na tabela Personagem

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-dialogo    | int        | Código de identificação do dialogo       | 1-1000             | PK, Not Null           |
| id-personagem    | int       | Código de identificação do personagem         | 1-1000            |FK, Not Null           |
| text   | varchar(200)       | texto do diálogo       | a-z, A-Z             |Not Null           |

---

### Entidade: Transação

**Descrição**: Transação entre o mercador e o jogador

**Observação**: Esta entidade irá gerenciar as compras e vendas no mud, tendo chave estrangeira nas tabelas Mercador e PC

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-transação    | int        | Código de identificação da transação       | 1-1000             | PK, Not Null           |
| id-mercador    | int       | Código de identificação do mercador         | 1-1000            |FK, Not Null           |
| id-pc    | int       | Código de identificação do personagem        | 1-1000            |FK, Not Null           |
| valor   | int       | valor n gociado        | 1-1000            |F ot Null           |

| tipo    | varchar(50)       | qual tipo de transação (venda, compra)        | venda , compra            |FK, Not Null           |---

### Entidade: Inventário 

**Descrição**: Inventário do jogador 

**Observação**: Esta entidade irá gerenciar o inventário de cada jogador, contendo chaves estrangeiras nas tabelas PC e Instância itens

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-inventario     | int        | Código de identificação do inventario        | 1-1000             | FK, Not Null           |
| id-instancia-item    | int       | Código de identificação da instancia         | 1-1000            |FK, Not Null           |


---

### Entidade: Loja

**Descrição**: Lojas contidas no jogo

**Observação**: Esta entidade irá gerenciar as lojas contidas no mud, tendo chaves estrangeiras nas tabelas Mercador e Instância item

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-loja      | int        | Código de identificação da loja         | 1-1000             | PK, Not Null           |
| id-mercador       | int       | Código de identificação de mercador        | 1-1000            | FK,Not Null           |
| id-instancia-item    | int       | Código de identificação da instancia         | 1-1000            |FK, Not Null           |


---

### Entidade: Instância Item

**Descrição**: Instancias para os itens

**Observação**: Esta entidade irá gerenciar o instanciamento de itens dentro do mud, contento chaves estrangeiras das tabelas Item e Sala

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-instancia      | int        | Código de identificação da instancia         | 1-1000             | PK, Not Null           |
| id-item       | int       | Código de identificação de item         | 1-1000            | FK,Not Null           |
| localização     | int       | Código de identificação da localização         | 1-1000            |FK, Not Null           |

---

### Entidade: Missões Realizadas

**Descrição**: Missões que foram realizadas

**Observação**: Esta entidade irá armazenar todas as missões realizadas, tendo chave estrangeira das tabelas Missao e PC

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-missao      | int        | Código de identificação da missao         | 1-1000             | FK,PK, Not Null           |
| id-pc      | int        | Código de identificação do personagem        | 1-1000             | FK,PK, Not Null           |


---

### Entidade: Contratos

**Descrição**: Contratos contidos no mud

**Observação**: Esta entidade vem de uma especialização da tabela Missão, com uma chave estrangeria da tabela Missão ,Contrato e Contratante

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-principal     | int        | Código de identificação do contrato        | 1-1000             | Pk,FK, Not Null           |
| id-dependencia      | int        | Código de identificação da contrato dependente        | 1-1000             | FK, Not Null           |
| id-contratante      | int        | Código do contrante        | 1-1000             | FK, Not Null           |

---

### Entidade: Missão Principal

**Descrição**: Missões principais contidos no mud

**Observação**: Esta entidade vem de uma especialização da tabela Missão, com uma chave estrangeria da tabela Missão Principal e Missão

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-principal     | int        | Código de identificação da missao principal        | 1-1000             | Pk,FK, Not Null           |
| id-dependencia      | int        | Código de identificação da missao principal dependente        | 1-1000             | FK, Not Null           |



---

### Entidade: Missão

**Descrição**: Missões contidos no mud

**Observação**: Esta entidade irá armazenar todas as missões, sem chave estrangeira, ela é uma generalização que contém as tabelas Missão Principal e Contrato

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-missao      | int        | Código de identificação da missao         | 1-1000             | Pk, Not Null           |
| nome       | varchar(50)       | nome da missao        | a-z, A-Z            | Not Null           |
| qnt_xp       | int       | experiencia que a missão oferece de recompensa        | 1-1000           | Not Null           |
| descricao      | varchar(200)       | detalhes da missão       | a-z, A-Z            | Not Null           |


---

### Entidade: Item

**Descrição**: Itens contidos do mud

**Observação**: Esta entidade vem de uma generalização que tera como espealizações as tabelas Chave, Grimorio, Arma e Consumivel

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-item      | int        | Código de identificação do item          | 1-1000             | Pk, Not Null           |
| descricao       | varchar(50)       | descricao geral do item         | a-z, A-Z            | Not Null           |
| nome       | varchar(50)       | nome do item         | a-z, A-Z            | Not Null           |
| preço       | varchar(50)       | valor do item         | a-z, A-Z            | Not Null           |
| eh_unico      | varchar(50)       | informação se é um unico item        | a-z, A-Z            | Not Null           |
---

### Entidade: Chave

**Descrição**: Chaves contidos do mud

**Observação**: Esta entidade vem de uma especialização da tabela Item, com uma chave estrangeria da tabela Item 

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-item      | int        | Código de identificação do item          | 1-1000             | Fk, Not Null           |
| requerido       | varchar(50)       | qual bau esta chave é utilizado         | a-z, A-Z            | Not Null           |

---

### Entidade: Arma

**Descrição**: Armas contidos do mud

**Observação**: Esta entidade vem de uma especialização da tabela Item, com uma chave estrangeria da tabela Item 

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-item       | int        | Código de identificação do item          | 1-1000             | Fk, Not Null           |
| dano-base       | int        | dano base da arma         | 1-1000             | Not Null           |

---

### Entidade: Consumível

**Descrição**: Consumíveis contidos do mud

**Observação**: Esta entidade vem de uma especialização da tabela Item, com uma chave estrangeria da tabela Item e Efeito

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-grimorio        | int        | Código de identificação do item          | 1-1000             | Fk, Not Null           |
| efeito        | int        | Código de identificação do efeito          | 1-1000             | Fk, Not Null           |
---

### Entidade: Grimorio

**Descrição**: Grimorios contidos do mud
**Observação**: Esta tabela é usada para exemplificar como preencher um dicionário de dados. Os valores e descrições são fictícios.

Esta entidade vem de uma especialização da tabela Item, com umc a chave | Nome Variávestrangeria da tabela Itemel     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-exemplo        | int        | Código de identificação do exemplo           | 1-1000             | PK, Not Null           |
| nomgrimorio        | varchar(50)| Nome associado ao exemplo                  | a-z, A-Z           | Not Null               |
| data-criacao      | date       | Data em que o exemplo foi critem        | Data válida        | NoFkNull               |

### Entidade: Habilidade

**Descrição**: Entidade responsável por listar as habildades do mud

**Observação**: Essa tabela possui chave estrangeira da tabela Habilidade, Grimorio e Efeito

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-habildade      | int        | Código de identificação da habilidade         | 1-1000             | PK, Not Null           |
| id_habilidade_dependente| int| codigo para habilidade que a mesma tem dependência                 | 1-1000           |FK, Not Null               |
| id-grimorio      | int       | codigo para grimorio            | Data válida        | 1-1000              |FK, Not Null
| efeito            | varchar(50)| efeito relacionado a habilidade                   | a-z, A-Z        | Not Null |
| tipo            | varchar(50)   | tipo da habilidade    | a-z, A-Z         | Not Null               |
| custo         | varchar(50)   | valor da habilidade   | a-z, A-Z         | Not Null               |
---

### Entidade: Efeito 

**Descrição**: Entidade responsável por listar os efeitos do mud

**Observação**: Essa tabela possui não possui chave estrangeira

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-efeito       | int        | Código de identificação do efeito         | 1-1000             | PK, Not Null           |
| alcance            | varchar(50)| até aonde o efeito é adquirido                 | a-z, A-Z           | Not Null               |
| duração     | int      | tempo de duração do efeito          | 1-1000        | Not Null               |

---

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 24/11/2024 | Primeira versão  do DD  | [Diego Carlito](https://github.com/DiegoCarlito) e [Márcio Henrique](https://github.com/DeM4rcio) |

</center>