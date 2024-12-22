# MER - Modelo Entidade Relacionamento

## Introdução

O Modelo Entidade Relacionamento de um bancos de dados é um modelo conceitual que descreve as entidades de um domínio de negócios, com seus atributos e seus relacionamentos.

> Entidades: os objetos da realidade a ser modelada.<br>
> Relacionamentos: as associações entre as entidades.<br>
> Atributos: características específicas de uma entidade.<br>


## Entidades

- **Personagem**
    - **PC**
    - **NPC**
        - **Mercador**
        - **Contratante**
        - **Inimigo**
        - **Chefe**
- **Instância Inimigo**
- **Missão**
    - **Missão Principal**
    - **Contrato**
- **Inventário**
- **Diálogo**
- **Item**
    - **Grimório**
    - **Consumível**
    - **Arma**
    - **Chave**
- **Instância item**
- **Checkpoint**
- **Sala**
- **Região**
- **Mundo**
- **Baú**
- **Loja**
- **Transação**
- **Combate**
- **Habilidade**
- **Efeito**

## Atributos

- *Personagem*: {<ins>id_personagem</ins>, nome, descricao, tipo}
    - *PC*: {hp, mp, xp, absorcao, atk, lvl, luck, combat_status, coins, id_sala}
    - *NPC*: {tipo}
        - *Mercador*: {id_sala}
        - *Contratante*: {id_sala}
        - *Inimigo*: {hp, xp, absorcao, atk, habilidade}
        - *Chefe*: {hp, xp, lvl, combat_status, absorção, atk, item_especial, id_sala}
- *Instância Inimigo*: {<ins>id_instancia_inimigo</ins>, id_inimigo, id_sala, vida_atual, absorcao, atk, habilidade, combat_status}
- *Missão*: {<ins>id_missao</ins>, nome, descricao, qtd_xp, tipo}
    - *Missão Principal*: {id_dependencia}
    - *Contrato*: {id_contratante, id_dependencia}
- *Inventário*: {<ins>id_inventario</ins>, id_instancia_item, capacidade, qtd_item}
- *Diálogo*: {<ins>id_dialogo</ins>, id_personagem, texto}
- *Item*: {<ins>id_item</ins>, nome, tipo, descricao, eh_unico, valor}
    - *Grimório*: {xp_necessario}
    - *Consumível*: {id_efeito, quantidade}
    - *Arma*: {dano}
    - *Chave*: {bau_requerido}
- *Instância de Item*: {<ins>id_instancia_item</ins>, id_item, id_sala}
- *Checkpoint*: {<ins>id_checkpoint</ins>, id_sala, id_pc}
- *Sala*: {<ins>id_sala</ins>, id_sala_conectada, id_regiao, nome, descricao}
- *Região*: {<ins>id_regiao</ins>, id_mundo, nome, descricao, dificuldade}
- *Mundo*: {<ins>id_mundo</ins>, nome, data}
- *Baú*: {<ins>id_bau</ins>, id_sala, itens, coins}
- *Loja*: {<ins>id_loja</ins>, id_intancias_itens}
- *Transação*: {<ins>id_transacao</ins>, id_mercador, id_pc, valor, tipo_transacao}
- *Combate*: {<ins>id_combate</ins>, id_pc, id_instancia_inimigo, resultado}
- *Habilidade*: {<ins>id_habilidade</ins>, id_habilidade_dependente, id_grimorio, id_efeito, tipo, custo_mp}
- *Efeito*: {<ins>id_efeito</ins>, alcance, duracao}

## Relacionamentos

- **PC *está* em Sala**
  - (1,1) **PC** está em uma **Sala**
  - (0,N) **Sala** pode conter vários PCs

- **NPC *está* em Sala**
  - (1,1) **NPC** está em uma **Sala**
  - (0,N) **Sala** pode conter vários NPCs

- **NPC *possui* especializações**
  - (1,1) **Mercador** é um **NPC**
  - (1,1) **Contratante** é um **NPC**
  - (1,1) **Inimigo** é um **NPC**
  - (1,1) **Chefe** é um **NPC**

- **PC *possui* Inventário**
  - (0,N) **PC** possui itens no **Inventário**
  - (1,1) **Inventário** pertence a um único **PC**

- **Inimigo *possui* Instância Inimigo**
  - (1,1) **Instância Inimigo** representa um **Inimigo**
  - (0,N) **Inimigo** pode ter várias instâncias

- **Contratante *fornece* Contrato**
  - (1,1) **Contrato** é atribuída por um **Contratante**
  - (0,N) **Contratante** pode atribuir várias **Contratos**
  - (0,1) **Contrato** pode depender de um outro **Contrato**


- **Missão *possui* especializações**
  - (1,1) **Missão Principal** é uma **Missão**
  - (1,1) **Contrato** é uma **Missão**

- **Missão Principal *depende* de outra Missão Principal**
  - (0,1) **Missão Principal** pode depender de outra **Missão Principal**
  - (0,1) **Missão Principal** pode ser pré-requisito de outra missão

- **Inventário *possui* Instâncias de Itens**
  - (0,N) **Inventário** contém várias **Instâncias de Itens**  
  - (1,1) **Instância de Item** pertence a um único **Inventário**

- **Item *possui* Instância Item**
  - (1,1) **Instância Item** representa um **Item**  
  - (0,N) **Item** pode ter várias instâncias

- **Personagem *possui* Diálogo**
  - (1,1) **Personagem** pode iniciar um **Diálogo**
  - (0,N) **Diálogo** pertence a um único **Personagem**
  - (0,1) **Diálogo** pode apontar para um próximo **Diálogo**  
  - (1,1) **Diálogo** pode ser parte de uma cadeia sequencial

- **Item *possui* especializações**
  - (1,1) **Grimório** é um **Item**
  - (1,1) **Consumível** é um **Item**
  - (1,1) **Arma** é um **Item**
  - (1,1) **Chave** é um **Item**

- **Loja *contém* Item**
  - (0,N) **Item** pode estar contido em várias **Lojas**  
  - (0,N) **Loja** pode conter vários **Itens**

- **Item *está* em Baú**
  - (0,N) **Item** pode estar em vários **Baús**  
  - (1,1) **Baú** pode conter vários **Itens**

- **Transação *envolve* Item**
  - (0,N) **Item** pode ser parte de uma **Transação**  
  - (1,1) **Transação** envolve pelo menos um **Item**

- **Sala *contém* Checkpoint**
  - (1,1) **Checkpoint** está em uma **Sala**  
  - (0,N) **Sala** pode conter vários **Checkpoints**

- **Checkpont *está* associado a um PC**
  - (0,N) **Checkpoint** está associado a um **PC**

- **Região *contém* Sala**
  - (1,1) **Sala** pertence a uma única **Região**
  - (0,N) **Região** contém várias **Salas**

- **Sala *conecta* Sala**
  - (0,N) **Sala** pode se conectar a outras **Salas**

- **Mundo *contém* Região**
  - (1,1) **Região** pertence a um único **Mundo**  
  - (0,N) **Mundo** contém várias **Regiões**

- **Mercador *possui* Loja**
  - (1,1) **Loja** possui um único **Mercador**  
  - (1,1) **Mercador** possui uma única **Loja**

- **Loja *possui* Instância Item**
  - (0,N) **Loja** possui várias **Instâncias Itens**  
  - (0,N) **Instância Item** pode estar em várias **Lojas**

- **Mercador *realiza* Transação**
  - (1,1) **Transação** envolve um **Mercador**  
  - (0,N) **Mercador** pode realizar várias **Transações**

- **Transação *envolve* PC**
  - (1,1) **Transação** envolve um **PC**  
  - (0,N) **PC** pode realizar várias **Transações**

- **Transação *inclui* Instância Item**
  - (0,N) **Transação** inclui várias **Instâncias de Itens**  
  - (1,1) **Instância de Item** pode estar em várias **Transações**

- **PC *derrota* Instância Inimigo**
  - (0,N) **PC** pode derrotar várias **Instâncias Inimigos**
  - (0,1) **Instância Inimigo** pode ser derrotada por **PC**

- **Habilidade *depende* de outra Habilidade**
  - (1,1) **Habilidade** pode depender de outra **Habilidade**  
  - (0,1) **Habilidade** pode ser pré-requisito de outra habilidade

- **Habilidade *contém* Efeito**
  - (0,1) **Habilidade** pode conter vários **Efeitos**
  - (0,N) **Efeito** pode estar contido em várias **Habilidades**

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 24/11/2024 | Primeira versão  do MER  | [Diego Carlito](https://github.com/DiegoCarlito) |
| `2.0`  | 22/12/2024 | Segunda versão  do MER  | [Diego Carlito](https://github.com/DiegoCarlito) |

</center>
