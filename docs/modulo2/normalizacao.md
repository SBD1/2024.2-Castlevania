## Introdução

A normalização é um processo utilizado no design de bancos de dados para organizar os dados de forma eficiente, reduzindo redundâncias e melhorando a integridade dos dados. Por meio de uma série de regras e formas normais, a normalização divide as informações em tabelas menores relacionadas, promovendo consistência e facilitando o gerenciamento. Esse processo ajuda a evitar anomalias em operações como inserção, atualização e exclusão, além de otimizar o desempenho e a escalabilidade do sistema.

O processo de normalização se divide em 5 etapas, chamadas de Formas Normais (FN).

* **1ª Forma Normal (1FN)**: Na 1FN, cada campo da tabela deve conter apenas um único valor indivisível, e todos os registros da tabela devem ter a mesma estrutura, sem repetições de grupos de atributos.

* **2ª Forma Normal (2FN)**: Para estar em 2FN, é necessário que não haja dependências parciais, ou seja, todos os atributos não-chave devem depender da totalidade da chave primária.

* **3ª Forma Normal (3FN)**: Na 3FN, deve-se garantir que todos os atributos não-chave sejam diretamente dependentes da chave primária, sem intermediários.

* **Forma Normal de Boyce-Codd (FNBC)**: A FNBC é uma versão mais rigorosa da 3ª Forma Normal. Por já atender a 2ª e 3ª forma Normal.

* **4ª Forma Normal (4FN)**:  A 4FN exige que não existam dependências multivaloradas, onde um único atributo poderia ser relacionado a múltiplos valores de outro atributo de forma independente.

### Tabelas a serem Normalizadas

Todas as tabelas contidas na [primeira versão do MR](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=MR-Castlevania.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1iqkQ5bLyo5ngIUHikCxP1Zgu3P8RBQPV%26export%3Ddownload) ( modelo relacional), entraram no processo de normalização, sendo detalhadas a seguir.

---

## Tabela Sala

> id-sala ➡ id_sala_conectada, id_regiao, nome e descr

Na tabela Sala, os atributos `id-sala` , `id_sala_conectada`, `id_regiao`, `nome` e `descr` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
 Como a tabela possui apenas uma chave primária simples (id-sala), automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela item, todos os atributos (`id_sala_conectada`, `id_regiao`, `nome` e `descr`)  depende diretamente do `id-sala`, atendendo ao critério da 3ª Forma Normal.

 A tabela Sala, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Bau

> id-bau ➡ itens

Na tabela Bau, o atributo `itens` fere essa propriedade isso porque terá vários itens sendo um atributo multivalorado. Para que atende a esse critério, será necessário que o atributo `itens` sejá parte da chave primária, tornando `id-bau` e `itens` chave primária composta.

### Correção

tornando `itens` como chave primária e mudando seu nome para melhor clareza para `item` agora ele atende a **1ª Forma Normal**.

##

 Como a tabela possui apenas dois atributos das quais compõe a chave a primária (composta) não é ferido a 2ª Forma Normal.
Na tabela Bau todos os atributos são chaves.

 A tabela Bau, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Baus

> id-bau ➡ id-sala

Na tabela Baus, os atributos `id-sala` , `id_bau` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
 Como a tabela Baus possui apenas chave primária , automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela Baus, por não existir atributos não chave, automaticamente já é atendido a 3ª  Forma normal.

 A tabela Baus, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Chefe

> id-Chefe ➡ localização, hp, level, status, atk, item_especial

Na tabela Chefe , os atributos `id-chefe` , `localização`, `hp`, `level`, `status`, `atk` e `item_especial` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
 Como a tabela Chefe possui apenas uma chave primária , automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela item, todos os atributos (`localização`, `hp`, `level` , `status`, `atk`, `item_especial`)  depende diretamente do `id-chefe`, atendendo ao critério da 3ª Forma Normal.

 A tabela Chefe, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Checkpoint

> id-checkpoint ➡ id_sala, id_pc

Na tabela Checkpoint , os atributos `id-checkpoint` , `id_sala`e `id_pc`, atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
 Como a tabela Checkpoint possui apenas uma chave primária , automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela item, todos os atributos (`id_sala`e `id_pc`)  depende diretamente do `id-checkpoint`, atendendo ao critério da 3ª Forma Normal.

 A tabela Checkpoint, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Mundo

> id-mundo ➡ nome, data

Na tabela Mundo , os atributos `id-mundo` , `nome`e `data`, atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
 Como a tabela Mundo possui apenas uma chave primária , automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela item, todos os atributos (`nome`e `id-data`)  depende diretamente do `id-mundo`, atendendo ao critério da 3ª Forma Normal.

 A tabela Mundo, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Instância Inimigo

> idInstancia ➡ idInimigo, localizacao, hp, absorcao, atk, habilidade, combatStatus

Nessa tabela, observamos algumas violações às formas normais. Se tratando da primeira, não foram encontradas violações, mas quando tratamos da 2ª FN, identificamos que existem atributos que não dependem exclusivamente da chave primária, como o campo localização e os demais campos, hp, atk, habilidade, entre outros.

### Correção

Foi criada uma tabela, statusNPC, que armazena todos os dados relacionados à atributos do NPC, como vida, dano, etc. Assim, para que um inimigo possua atributos, é necessário que tenha um idInstancia, atendendo à 2ª FN. Fazendo isso eliminamos também as dependências transitivas, atendendo assim à 3ª FN e a FNBC.

---

## Tabela Inimigo

> id-inimigo ➡ hp, xp, absorcao, atk, habilidade

A tabela se encontra na 1ª FN, por não haver atributos repetidos, ou seja, seus dados são atômicos. Porém enfrentamos o mesmo problema encontrado na tabela instanciaInimigo, com atributos não dependendo excluisivamente da chave idInimigo.

### Correção

Foram retirados os campos de hp, atk, absorcao, etc, sendo referenciados em outra tabela através do campo idStatus. Além disso, tornamos o campo idInimigo uma chave primária, atendendo assim às 2ª e 3ª FN.

---

## Tabela Região

> idRegiao ➡ idRegiaoConectada, idMundo, nome, desc, dificuldade

Atende à 1ª FN, por somente possuir valores atômicos, com cada linha sendo única. Também atende à 2ª FN por não possuir dependências parciais e por fim, atende à 3ª FN por não possuir dependências transitivas, por sua vez, também atende à FNBC.

---

## Tabela Habilidade

idHabilidade ➡ idHabilidadeDependente, idGrimorio, efeito, tipo, custo, descricao

A tabela cumpre a 1ª Forma Normal porque todos os valores armazenados nas colunas são atômicos, ou seja, indivisíveis, e cada linha apresenta um identificador único. Ela também satisfaz a 2ª Forma Normal, já que não existem dependências parciais, ou seja, todas as colunas não-chave dependem integralmente da chave primária. Por fim, a tabela está em conformidade com a 3ª Forma Normal, pois não apresenta dependências transitivas, ou seja, não há colunas não-chave dependendo de outras colunas não-chave. Assim, ela também segue a FNBC (Forma Normal de Boyce-Codd).

---

## Tabela Grimório

> idGrimorio ➡ idHabilidade

Esta tabela respeita a 1ª Forma Normal, pois cada célula contém apenas um valor indivisível, garantindo que os dados sejam atômicos, e as linhas são identificadas unicamente. Na 2ª Forma Normal, não há dependências parciais, já que todas as colunas não-chave dependem completamente da chave primária. Na 3ª Forma Normal, a ausência de dependências transitivas entre colunas não-chave mostra que a tabela é eficiente. Dessa forma, ela também atende aos critérios da FNBC.

---

## Tabela Consumível

> idItem ➡ efeito

Em relação à 1ª Forma Normal, a tabela está normalizada porque armazena apenas valores atômicos em cada célula, e cada linha possui um identificador exclusivo. Quanto à 2ª Forma Normal, não existem dependências parciais, ou seja, todas as colunas que não fazem parte da chave primária dependem inteiramente dela. Na 3ª Forma Normal, a tabela não apresenta dependências transitivas, uma vez que as colunas não-chave não dependem umas das outras. Por isso, ela também segue os princípios da FNBC.

---

## Tabela Arma 

> idItem ➡ danoBase

A tabela atende à 1ª Forma Normal, já que os dados armazenados são atômicos e não há repetições ou conjuntos de valores em uma mesma célula. Além disso, a tabela segue a 2ª Forma Normal porque não possui dependências parciais, garantindo que todas as colunas não-chave dependam da chave primária por completo. No que diz respeito à 3ª Forma Normal, não há dependências transitivas entre colunas não-chave. Por essas razões, a tabela também está em conformidade com a FNBC.

---

## Tabela Chave

> idItem ➡ requerido

Cumprindo a 1ª Forma Normal, a tabela contém apenas valores atômicos, sendo todos os dados indivisíveis, e cada linha tem um identificador exclusivo. Ela também obedece à 2ª Forma Normal, pois não existem dependências parciais entre as colunas, já que todas dependem diretamente da chave primária. Além disso, ao atender à 3ª Forma Normal, a tabela não apresenta dependências transitivas, tornando-a eficiente e bem projetada. Assim, ela segue os princípios da FNBC.

---

## Tabela PC

> id-pc ➡ hp, mp, xp, absorção, atk, lvl, luck, combat_status, coins, localização

Na tabela PC, os atributos `id-pc`, `hp`, `mp`, `xp`, `absorção`, `atk`, `lvl`, `luck`, `combat_status`, `coins` e `localização` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela PC possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela PC, todos os atributos (`hp`, `mp`, `xp`, `absorção`, `atk`, `lvl`, `luck`, `combat_status`, `coins`, `localização`) dependem diretamente do `id-pc`, atendendo ao critério da 3ª Forma Normal.

A tabela PC, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Transação

> id-transação ➡ id_mercador, id_pc, valor, tipo_transação

Na tabela **Transação**, os atributos `id-transação`, `id_mercador`, `id_pc`, `valor` e `tipo_transação` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Transação** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Transação**, todos os atributos (`id_mercador`, `id_pc`, `valor`, `tipo_transação`) dependem diretamente do `id-transação`, atendendo ao critério da 3ª Forma Normal.

A tabela **Transação**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Combate

> id-combate ➡ id_pc, id_inimigo, resultado

Na tabela **Combate**, os atributos `id-combate`, `id_pc`, `id_inimigo` e `resultado` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Combate** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Combate**, todos os atributos (`id_pc`, `id_inimigo`, `resultado`) dependem diretamente do `id-combate`, atendendo ao critério da 3ª Forma Normal.

A tabela **Combate**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Inventário

> id-inventario ➡ id_instancias_itens, capacidade, qtd-itens

Na tabela **Inventário**, os atributos `id-inventario`, `id_instancias_itens`, `capacidade` e `qtd-itens` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Inventário** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Inventário**, todos os atributos (`id_instancias_itens`, `capacidade`, `qtd-itens`) dependem diretamente do `id-inventario`, atendendo ao critério da 3ª Forma Normal.

A tabela **Inventário**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Instância Item

> id-instancia-item ➡ id_item, id_sala

Na tabela **Instância Item**, os atributos `id-instancia-item`, `id_item` e `id_sala` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Instância Item** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Instância Item**, todos os atributos (`id_item`, `id_sala`) dependem diretamente do `id-instancia-item`, atendendo ao critério da 3ª Forma Normal.

A tabela **Instância Item**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Item

> id-item ➡ nome, tipo, descricao, eh_unico, valor

Na tabela **Item**, os atributos `id-item`, `nome`, `tipo`, `descricao`, `eh_unico` e `valor` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Item** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Item**, todos os atributos (`nome`, `tipo`, `descricao`, `eh_unico`, `valor`) dependem diretamente do `id-item`, atendendo ao critério da 3ª Forma Normal.

A tabela **Item**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Efeito

> id-efeito ➡ alcance, duracao

Na tabela **Efeito**, os atributos `id-efeito`, `alcance` e `duracao` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Efeito** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Efeito**, todos os atributos (`alcance`, `duracao`) dependem diretamente do `id-efeito`, atendendo ao critério da 3ª Forma Normal.

A tabela **Efeito**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Personagem

> id-personagem ➡ nome, descrição, tipo

Na tabela **Personagem**, os atributos `id-personagem`, `nome`, `descrição` e `tipo` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Personagem** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Personagem**, os atributos (`nome`, `descrição`, `tipo`) dependem diretamente do `id-personagem`, atendendo ao critério da 3ª Forma Normal.

A tabela **Personagem**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela NPC

> id-npc ➡ tipo

Na tabela **NPC**, os atributos `id-npc` e `tipo` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **NPC** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **NPC**, o atributo `tipo` depende diretamente do `id-npc`, atendendo ao critério da 3ª Forma Normal.

A tabela **NPC**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Contratante

> id-contratante ➡ localização

Na tabela **Contratante**, os atributos `id-contratante` e `localização` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Contratante** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Contratante**, o atributo `localização` depende diretamente do `id-contratante`, atendendo ao critério da 3ª Forma Normal.

A tabela **Contratante**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Mercador

> id-mercador ➡ localização

Na tabela **Mercador**, os atributos `id-mercador` e `localização` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Mercador** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Mercador**, o atributo `localização` depende diretamente do `id-mercador`, atendendo ao critério da 3ª Forma Normal.

A tabela **Mercador**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

## Tabela Loja

> id-loja ➡ id_mercador, id_instâncias_itens

Na tabela **Loja**, os atributos `id-loja`, `id_mercador` e `id_instâncias_itens` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
Como a tabela **Loja** possui apenas uma chave primária, automaticamente todos os atributos dependem da chave em sua totalidade.
Na tabela **Loja**, todos os atributos (`id_mercador`, `id_instâncias_itens`) dependem diretamente do `id-loja`, atendendo ao critério da 3ª Forma Normal.

A tabela **Loja**, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 13/12/2024 | Primeira versão da Normalização  | [Márcio Henrique](https://github.com/DeM4rcio) |
| `1.1`  | 13/12/2024 | Normalização das tabelas (Mundo, Checkpoint, Sala, Bau, Baus, Chefe)  | [Márcio Henrique](https://github.com/DeM4rcio) |
| `1.2`  | 20/12/2024 | Normalização das tabelas (PC, Transação, Combate, Inventário, Instância Item, Item)  | [Diego Carlito](https://github.com/DiegoCarlito) |
| `1.3`  | 21/12/2024 | Normalização das tabelas (instanciaInimigo, inimigo, regiao, habilidade, grimorio, consumivel, arma, chave)  | [Filipe Carvalho](https://github.com/filipe-002) |
| `1.4`  | 22/12/2024 | Normalização das tabelas (Efeito, Personagem, NPC, Contratante, Mercador, Loja)  | [Diego Carlito](https://github.com/DiegoCarlito) |
