# DD - Dicionário de Dados

## Introdução

Um dicionário de dados é um recurso essencial na área da ciência de dados e da informática. Ele funciona como um catálogo ou compilação de informações sobre os dados utilizados em um sistema, banco de dados, projeto de pesquisa ou qualquer contexto em que a manipulação e interpretação de dados sejam necessárias.


## Entidade: Exemplo

**Descrição**: Esta entidade serve como um modelo para ilustrar como as informações são organizadas e descritas em um banco de dados. Inclui variáveis típicas, tipos de dados, valores permitidos e restrições.

**Observação**: Esta tabela é usada para exemplificar como preencher um dicionário de dados. Os valores e descrições são fictícios.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-exemplo        | int        | Código de identificação do exemplo          | 1-1000            | PK, Not Null           |
| nome              | varchar(50)| Nome associado ao exemplo                   | a-z, A-Z          | Not Null               |
| data-criacao      | date       | Data em que o exemplo foi criado            | Data válida       | Not Null               |
| valor             | decimal(10,2)| Valor numérico do exemplo                 | 0.00-9999.99      | Not Null, Check (>= 0) |
| ativo             | boolean    | Indicador se o exemplo está ativo ou não    | True, False       | Not Null               |

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
| id_personagem     | int        | Código de identificação do personagem      | 1-1000             | PK, Not Null           |
| nome              | varchar(50)| Nome associado ao personagem               | a-z, A-Z           | Not Null               |
| descricao         | varchar(50)| Descrição do personagem                    | a-z, A-Z           | Not Null               |
| tipo              | enum       | Tipo de personagem                         | 'PC', 'NPC'        | Not Null               |


#### PC

**Descrição**: Contém informações específicas dos personagens jogáveis.

**Observação**: Esta tabela contém chave estrangeira da tabela Sala.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| hp                | int        | Ponto de vida do pc                        | 0-1000             | Not Null               |
| mp                | int        | Pontos de mana do pc                       | 0-1000             | Not Null               |
| xp                | int        | Ponto de experiência do pc                 | 0-1000             | Not Null               |
| absorcao          | int        | Redução do dano que o pc recebe            | 0-1000             | Not Null               |
| atk               | int        | Quantidade de dano básica do pc            | 0-1000             | Not Null               |
| lvl               | int        | Level do pc                                | 1-1000             | Not Null               |
| luck              | int        | Indica a sorte do pc                       | 0-1000             | Not Null               |
| combat_status     | enum       | Indica o estado do pc                      | 'Confuso', 'Envenenado', 'Normal' |Not Null |
| coins             | int        | Indica a quantidaade de moedas do pc       | 0-1000             | Not Null               |
| id_sala           | int        | Indica a sala em o pc está                 | 1-1000             | FK, Not Null           |


#### NPC

**Descrição**: Contém informações específicas dos personagens não jogáveis.

**Observação**: Esta tabela não contém chave estrangeira.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| tipo              | varchar(50)| Indica o tipo de NPC                       | a-z, A-Z           | Not Null               |

##### Mercador

**Descrição**: NPC que comercializa itens.

**Observação**: Esta tabela contém chave estrangeira da tabela Sala.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_sala           | int        | Indica a sala em que o mercador está       | 1-1000             | FK, Not Null           |

##### Contratante

**Descrição**: NPC que fornece contratos para o jogador.

**Observação**: Esta tabela contém chave estrangeira da tabela Sala.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_sala           | int        | Indica a sala em que o contratante está    | 1-1000             | FK, Not Null           |

##### Inimigo

**Descrição**: NPC que participa de combates com o jogador.

**Observação**: Esta tabela não possui chaves estrangeiras.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| hp                | int        | Pontos de vida do inimigo                  | 1-1000             | Not Null               |
| xp                | int        | Pontos de experiência fornecidos ao derrotar o inimigo | 1-1000 | Not Null               |
| absorcao          | int        | Redução do dano que o inimigo recebe       | 1-1000             | Not Null               |
| atk               | int        | Dano básico causado pelo inimigo           | 1-1000             | Not Null               |
| habilidade        | int        | Acréscimo no dano básico do inimigo        | 1-1000             | Not Null               |

##### Chefe

**Descrição**: NPC mais desafiador, geralmente finalizando uma região ou missão.

**Observação**: Esta tabela contém chaves estrangeiras das tabelas Sala e Item.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| hp                | int        | Pontos de vida do chefe                    | 1-1000             | Not Null               |
| xp                | int        | Pontos de experiência fornecidos ao derrotar o chefe  | 1-1000  | Not Null               |
| lvl               | int        | Nível do chefe                             | 1-1000             | Not Null               |
| combat_status     | enum       | Indica o estado do chefe                   | 'Confuso', 'Envenenado', 'Normal' |Not Null |
| absorcao          | int        | Redução do dano que o chefe recebe         | 1-1000             | Not Null               |
| atk               | int        | Dano básico causado pelo inimigo           | 1-1000             | Not Null               |
| item_especial     | int        | Item dropado pelo chefe                    | 1-1000             | FK, Not Null           |
| id_sala           | int        | Indica a sala em que o chefe está          | 1-1000             | FK, Not Null           |

---

### Entidade: Instância Inimigo

**Descrição**: Uma instância de NPC inimigo representa um personagem não jogável que atua como oponente no jogo. 
Essa instância é responsável por gerenciar as interações do inimigo com o ambiente, outros NPCs e o jogador, 
desempenhando um papel essencial na mecânica e na dinâmica de combate do jogo.

**Observação**: Esta tabela contém chaves estrangeiras das tabelas Sala e Inimigo.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_instancia      | int        | Código de identificação da instância de inimigo    | 1-1000     | PK, Not Null           |
| id_inimigo        | int        | Código de identificação do inimigo         | 1-1000             | FK, Not Null           |
| id_sala           | int        | Código de identificação da sala que a instância de inimigo está | 1-1000  | FK, Not Null |
| vida_atual        | int| Vida atual da instância de inimigo                 | 1-1000             | Not Null               |
| absorcao          | int       | Redução do dano que a instância de inimigo recebe  | 1-1000      | Not Null               |
| atk               | int | Dano básico causado pela isntância de inimigo     | 1-1000             | Not Null               |
| habilidade        | int    | Acréscimo no dano básico do inimigo            | 1-1000             | Not Null               |
| combat_status     | enum       | Indica o estado do chefe                   | 'Confuso', 'Envenenado', 'Normal' |Not Null |

---

### Entidade: Checkpoint

**Descrição**: é um marco no progresso do jogador dentro do jogo, utilizado para salvar o estado atual e permitir que o jogador continue a partir desse ponto em caso de derrota ou ao retornar ao jogo.

**Observação**: Esta tabela contém cahves estrangeiras das tabelas Sala e PC.

| Nome Variável     | Tipo           | Descrição                                    | Valores Permitidos         | Restrições de Domínio      |
|-------------------|----------------|----------------------------------------------|----------------------------|----------------------------|
| id_checkpoint     | int            | Identificador único do checkpoint            | 1-1000                     | PK, Not Null               |
| id_sala           | int            | Referência à sala onde o checkpoint está     | 1-1000                     | FK, Not Null               |
| id_pc             | int            | Referência ao personagem jogável associado   | 1-1000                     | FK, Not Null               |

---

### Entidade: Baú

**Descrição**: Baús contidos no jogo

**Observação**: Esta entidade irá armazenas os baús que o jogo oferece, tendo chave estrangeira na tabela Instância item

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_bau            | int        | Código de identificação do bau             | 1-1000             | PK, Not Null           |
| itens             | int        | Código de instância de itens               | 1-1000             | FK, Not Null           |



---

### Entidade: Baús

**Descrição**: Baus contidos nas salas

**Observação**: Esta entidade irá armazenas os baus em suas salas, tendo chave estrangeira nas tabelas Bau e Sala

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_sala           | int        | Código de identificação da sala            | 1-1000             | PK,FK, Not Null        |
| id_bau            | int        | Código de identificação do bau             | 1-1000             | PK,FK, Not Null        |

---

### Entidade: Sala 

**Descrição**: A sala é contido nas regiões

**Observação**: Esta entidade irá armazenas as salas contidas do game, tendo chaves estrangeiras contidas nas tabelas Sala e Região

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_sala           | int        | Código de identificação da sala            | 1-1000             | PK, Not Null           |
| id_sala_conectada | int        | Código de identificação da sala conectada  | 1-1000             | FK, Not Null           |
| id_regiao         | int        | Código de identificação da regiao          | 1-1000             | FK, Not Null           |
| nome              | varchar(200) | nome da sala                             | a-z, A-Z           |Not Null                |
| descricao             | varchar(200) | descrição da sala                    | a-z, A-Z           |Not Null                |


---

### Entidade: Região 

**Descrição**: O jogo é dividido em várias regiões

**Observação**: Esta entidade irá armazenas as regiões contidas do game, tendo chaves estrangeiras contidas nas tabelas Região e Mundo

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_regiao         | int        | Código de identificação da regiao          | 1-1000             | PK, Not Null           |
| id_região_conectada| int       | Código de identificação da região conectada| 1-1000             |FK, Not Null            |
| id_mundo          | int        | Código de identificação do mundo           | 1-1000             |FK, Not Null            |
| nome              | varchar(200)| nome do mundo                             | a-z, A-Z           |Not Null                |
| descricao         | varchar(200)| descrição da região                       | a-z, A-Z           |Not Null                |
| dificuldade       | varchar(50) | dificuldade da região (fácil, médio, difícil) | a-z, A-Z       |Not Null                |

---

### Entidade: Mundo 

**Descrição**: Mundo é a visão mais macro do mapa do mud

**Observação**: Esta entidade irá armazenas os mundos contidos do game

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_mundo          | int        | Código de identificação do mundo           | 1-1000             | PK, Not Null           |
| nome              | varchar(200) | nome do mundo                            | a-z, A-Z           |Not Null                |
| data              | date       | data em que o mundo foi criado             | Data válida        |Not Null                |

---

### Entidade: Diálogo

**Descrição**: Dialogos do mud.

**Observação**: Esta entidade irá armazenas todos os dialogos dos personagens, tendo uma chave estrangeira na tabela Personagem.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_dialogo        | int        | Código de identificação do dialogo         | 1-1000             | PK, Not Null           |
| id_personagem     | int        | Código de identificação do personagem      | 1-1000             |FK, Not Null            |
| text              | varchar(200) | texto do diálogo                         | a-z, A-Z           |Not Null                |

---

### Entidade: Transação

**Descrição**: Transação entre o mercador e o jogador.

**Observação**: Esta entidade irá gerenciar as compras e vendas no mud, tendo chave estrangeira nas tabelas Mercador e PC.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_transacao      | int        | Código de identificação da transação       | 1-1000             | PK, Not Null           |
| id_mercador       | int        | Código de identificação do mercador        | 1-1000             |FK, Not Null            |
| id_pc             | int        | Código de identificação do personagem      | 1-1000             |FK, Not Null            |
| valor             | int        | Valor negociado                            | 1-1000             |Not Null                |
| tipo              | enum('venda', 'compra') | Qual tipo de transação        | 'venda' , 'compra' | Not Null               |

---

### Entidade: Combate

**Descrição**: Combate entre o PC e Instância de Inimigo.

**Observação**: Esta tabela contém chaves estrangeiras das tabelas PC e Instância Inimigo.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_combate        | int        | Código de identificação do Combate         | 1-1000             | PK, Not Null           |
| id_pc             | int        | Código de identificação do pc              | 1-1000             |FK, Not Null            |
| id_inimigo        | int        | Código de identificação da instância inimigo   | 1-1000         |FK, Not Null            |
| resultado      | enum('venceu', 'derrotado', 'fugiu') | Resultado do combate | 'venceu' , 'derrotado', 'fugiu' | Not Null |

---

### Entidade: Inventário 

**Descrição**: Inventário do jogador.

**Observação**: Esta entidade irá gerenciar o inventário de cada jogador, contendo chaves estrangeiras nas tabelas PC e Instância itens.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_inventario     | int        | Código de identificação do inventario      | 1-1000             | FK, Not Null           |
| id_instancia-item | int        | Código de identificação da instancia       | 1-1000             |FK, Not Null            |

---

### Entidade: Loja

**Descrição**: Lojas contidas no jogo.

**Observação**: Esta entidade irá gerenciar as lojas contidas no mud, tendo chaves estrangeiras nas tabelas Mercador e Instância item.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_loja           | int        | Código de identificação da loja            | 1-1000             | PK, Not Null           |
| id_mercador       | int        | Código de identificação de mercador        | 1-1000             | FK,Not Null            |
| id_instancia-item | int        | Código de identificação da instancia       | 1-1000             | FK, Not Null           |

---

### Entidade: Instância Item

**Descrição**: Instâncias para os itens.

**Observação**: Esta entidade irá gerenciar o instanciamento de itens dentro do mud, contento chaves estrangeiras das tabelas Item e Sala.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_instancia_item | int        | Código de identificação da instancia       | 1-1000             | PK, Not Null           |
| id_item           | int        | Código de identificação de item            | 1-1000             | FK,Not Null            |
| id_sala           | int        | Código de identificação da localização     | 1-1000             | FK, Not Null           |

---

### Entidade: Missões Realizadas

**Descrição**: Missões que foram realizadas

**Observação**: Esta entidade irá armazenar todas as missões realizadas, tendo chave estrangeira das tabelas Missao e PC

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_missao         | int        | Código de identificação da missao          | 1-1000             | FK,PK, Not Null        |
| id_pc             | int        | Código de identificação do personagem      | 1-1000             | FK,PK, Not Null        |

---

### Entidade: Missão

**Descrição**: Missões contidos no mud.

**Observação**: Esta entidade irá armazenar todas as missões, sem chave estrangeira, ela é uma generalização que contém as tabelas Missão Principal e Contrato

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_missao         | int        | Código de identificação da missao          | 1-1000             | Pk, Not Null           |
| nome              | varchar(50)| nome da missao                             | a-z, A-Z           | Not Null               |
| qnt_xp            | int        | experiencia que a missão oferece de recompensa  | 1-1000        | Not Null               |
| descricao         | varchar(200) | detalhes da missão                       | a-z, A-Z           | Not Null               |

#### Missão Principal

**Descrição**: Missões principais contidos no mud.

**Observação**: Esta tabela contém chave estrangeira da tabela Missão Principal.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_dependencia    | int        | Código de identificação da missao principal dependente | 1-1000 | FK, Not Null           |

#### Contrato

**Descrição**: Contratos contidos no mud.

**Observação**: Esta tabela contém chaves estrangerias das tabelas Contrato e Contratante.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_dependencia    | int        | Código de identificação da contrato dependente | 1-1000         | FK, Not Null           |
| id_contratante    | int        | Código do contrante                        | 1-1000             | FK, Not Null           |

---

### Entidade: Item

**Descrição**: Itens contidos do mud.

**Observação**: Esta entidade vem de uma generalização que terá como espealizações as tabelas Chave, Grimorio, Arma e Consumivel

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_item           | int        | Código de identificação do item            | 1-1000             | Pk, Not Null           |
| descricao         | varchar(50)| descricao geral do item                    | a-z, A-Z           | Not Null               |
| nome              | varchar(50)| nome do item                               | a-z, A-Z           | Not Null               |
| valor             | int        | valor do item                              | 1-1000          | Not Null                  |
| eh_unico          | boolean    | informação se é um unico item              | True, False        | Not Null               |

#### Chave

**Descrição**: Chaves contidos do mud

**Observação**: Esta tabela não contém chave estrangeira.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| bau_requerido     |varchar(50) | Qual bau esta chave é utilizado            | a-z, A-Z           | Not Null               |

#### Arma

**Descrição**: Armas contidos do mud.

**Observação**: Esta tabela não contém chave estrangeira.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| dano              | int        | dano base da arma                          | 1-1000             | Not Null               |

#### Consumível

**Descrição**: Consumíveis contidos do mud.

**Observação**: Esta tabela contém chave estrangeira da tabela Efeito.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_efeito         | int        | Código de identificação do efeito          | 1-1000             | Fk, Not Null           |
| quantidade        | int        | Quantidade de consumíveis                  | 1-1000             | Not Null               |

#### Grimório

**Descrição**: Grimórios contidos do mud.

**Observação**: Esta tabela contém chave estrangeira da tabela Habilidade.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| xp_necessario     | int        | Quantidade de xp para acessar habilidade do grimório | 1-1000   | FK, Not Null           |

---

### Entidade: Habilidade

**Descrição**: Entidade responsável por listar as habildades do mud

**Observação**: Essa tabela possui chave estrangeira da tabela Habilidade, Grimorio e Efeito

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_habildade      | int        | Código de identificação da habilidade      | 1-1000             | PK, Not Null           |
| id_habilidade_dependente| int  | codigo para habilidade que a mesma tem dependência | 1-1000     | FK, Not Null           |
| id_grimorio      | int         | codigo para grimorio                       | 1-1000             | FK, Not Null           |
| efeito           | varchar(50) | efeito relacionado a habilidade            | a-z, A-Z           | Not Null               |
| tipo             | varchar(50) | tipo da habilidade                         | a-z, A-Z           | Not Null               |
| custo_mp         | int         | Custo de magia para usar habilidade        | 1-1000             | Not Null               |

---

### Entidade: Efeito 

**Descrição**: Entidade responsável por listar os efeitos do mud

**Observação**: Essa tabela possui não possui chave estrangeira

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id_efeito         | int        | Código de identificação do efeito          | 1-1000             | PK, Not Null           |
| alcance           | int        | 	Distância ou área onde o efeito é aplicado| 0-1000             | Not Null               |
| duracao           | int        | Duração do efeito em turnos                | 1-1000             | Not Null               |

---

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 24/11/2024 | Primeira versão  do DD  | [Diego Carlito](https://github.com/DiegoCarlito) e [Márcio Henrique](https://github.com/DeM4rcio) |
| `2.0`  | 22/12/2024 | Segunda versão  do DD   | [Diego Carlito](https://github.com/DiegoCarlito) |

</center>