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

- *Personagem*: {<ins>id_personagem</ins>, nome, descr, tipo}
    - *PC*: {hp, mp, xp, absorção, atk, lvl, luck, combat_status, coins, id_sala}
    - *NPC*: {tipo}
        - *Mercador*: {id_sala}
        - *Contratante*: {id_sala}
        - *Inimigo*: {hp, xp, absorção, atk, habilidade}
        - *Chefe*: {hp, xp, lvl, status, absorção, atk, item_especial, id_sala}
- *Instância Inimigo*: {<ins>id_instancia</ins>, id_inimigo, id_sala, vida_atual, absorção, atk, habilidade, combat_status}
- *Missão*: {<ins>id_missao</ins>, nome, descr, qtd_xp, recompensa, tipo}
    - *Missão Principal*: {id_dependencia}
    - *Contrato*: {id_contratante, id_dependencia}
- *Inventário*: {<ins>id-inventario</ins>, id_instancias_itens, capacidade, qtd-itens}
- *Diálogo*: {<ins>id-dialogo</ins>, texto, proximo-dialogo-id}
- *Item*: {<ins>id_item</ins>, nome, tipo, descricao, eh_unico, valor}
    - *Grimório*: {habilidade-id}
    - *Consumível*: {id_efeito, quantidade}
    - *Arma*: {dano_base}
    - *Chave*: {requerido-id}
- *Instância de Item*: {<ins>id_instancia_item</ins>, id_item, id_sala}
- *Checkpoint*: {<ins>id-checkpoint</ins>, id_sala, id_pc}
- *Sala*: {<ins>id_sala</ins>, id_sala_conectada, id_regiao, nome, descr}
- *Região*: {<ins>id_regiao</ins>, id_mundo, nome, descr, dificuldade}
- *Mundo*: {<ins>id_mundo</ins>, nome, data}
- *Baú*: {<ins>id_bau</ins>, id_sala, qtd-itens, qtd-gold}
- *Loja*: {<ins>id_loja</ins>, id_sala, id_intancias_itens}
- *Transação*: {<ins>id_transacao</ins>, id_mercador, id_pc, valor, tipo}
- *Combate*: {<ins>id_combate</ins>, id_pc, id_inimigo, resultado}
- *Habilidade*: {<ins>id_habilidade</ins>, id_habilidade_dependente, nome, descr, id_efeito, custo_mana}
- *Efeito*: {<ins>id_efeito</ins>, descr, alcance, duracao}

## Relacionamentos

- (1,1) **PC** está em uma **Sala**  
  - (0,N) **Sala** pode conter vários PCs
- (1,1) **NPC** está em uma **Sala**  
  - (0,N) **Sala** pode conter vários NPCs
- **NPC** possui especializações:
  - (1,1) **Mercador** é um **NPC**
  - (1,1) **Contratante** é um **NPC**
  - (1,1) **Inimigo** é um **NPC**
  - (1,1) **Chefe** é um **NPC**
- (0,N) **PC** possui itens no **Inventário**  
  - (1,1) **Inventário** pertence a um único **PC**

- (1,1) **Instância de Inimigo** representa um **Inimigo**  
  - (0,N) **Inimigo** pode ter várias instâncias 

- (1,1) **Contrato** é atribuída por um **Contratante**  
  - (0, N) **Contratante** pode atribuir várias **Contratos**
- **Missão** possui especializações:
  - (1,1) **Missão Principal** é uma **Missão**
  - (1,1) **Contrato** é uma **Missão**
- (0,1) **Missão Principal** pode depender de outra **Missão Principal**  
  - (0,1) **Missão Principal** pode ser pré-requisito de outra missão
- (0,1) **Contrato** pode depender de um outro **Contrato**

- (0,N) **Inventário** contém várias **Instâncias de Itens**  
  - (1,1) **Instância de Item** pertence a um único **Inventário**
- (1,1) **Instância de Item** representa um **Item**  
  - (0,N) **Item** pode ter várias instâncias

- (1,1) **NPC** pode iniciar um **Diálogo**  
  - (0,N) **Diálogo** pertence a um único **NPC**
- (0,1) **Diálogo** pode apontar para um próximo **Diálogo**  
  - (1,1) **Diálogo** pode ser parte de uma cadeia sequencial

- (1,1) **Item** é classificado como:
  - **Grimório**, **Consumível**, **Arma** ou **Chave** (1,1)
- (0,N) **Item** pode ser vendido em várias **Lojas**  
  - (0,N) **Loja** pode vender vários **Itens**
- (0,N) **Item** pode estar em vários **Baús**  
  - (1,1) **Baú** pode conter vários **Itens**
- (0,N) **Item** pode ser parte de uma **Transação**  
  - (1,1) **Transação** envolve pelo menos um **Item**

- (1,1) **Checkpoint** está em uma **Sala**  
  - (0,N) **Sala** pode conter vários **Checkpoints**
- (0,N) **Checkpoint** está associado a um **PC**

- (1,1) **Sala** pertence a uma única **Região**  
  - (0,N) **Região** contém várias **Salas**
- (0,N) **Sala** pode se conectar a outras **Salas**

- (1,1) **Região** pertence a um único **Mundo**  
  - (0,N) **Mundo** contém várias **Regiões**

- (1,1) **Loja** possui um único **Mercador**  
  - (1,1) **Mercador** está associado a uma única **Loja**
- (0,N) **Loja** pode vender várias **Instâncias de Itens**  
  - (0,N) **Instância de Item** pode estar em várias **Lojas**

- (1,1) **Transação** envolve um **Mercador**  
  - (0,N) **Mercador** pode realizar várias **Transações**
- (1,1) **Transação** envolve um **PC**  
  - (0,N) **PC** pode realizar várias **Transações**
- (0,N) **Transação** inclui várias **Instâncias de Itens**  
  - (1,1) **Instância de Item** pode estar em várias **Transações**

- (0,N) **PC** pode derrotar várias **Instâncias de Inimigos**
  - (0,1) **Instância de Inimigo** pode ser derrotada por **PC**

- (1,1) **Habilidade** pode depender de outra **Habilidade**  
  - (0,1) **Habilidade** pode ser pré-requisito de outra habilidade
- (1,1) **Habilidade** está associada a um único **Efeito**

- (0,N) **Efeito** pode ser usado por várias **Habilidades**

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 24/11/2024 | Primeira versão  do MER  | [Diego Carlito](https://github.com/DiegoCarlito) |

</center>
