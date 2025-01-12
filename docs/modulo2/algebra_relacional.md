# Algebra Relacional

## Introdução

A álgebra relacional é uma linguagem formal utilizada para manipular e consultar dados em bancos de dados relacionais. Ela fornece um conjunto de operações básicas, como seleção, projeção, união, diferença, produto cartesiano e junção, que permitem extrair e combinar dados de tabelas de forma precisa e matemática. Essas operações são fundamentais para a execução de consultas em SQL, pois definem como os dados devem ser filtrados, transformados e combinados para produzir os resultados desejados. A álgebra relacional serve como base teórica para a implementação e otimização de sistemas de gerenciamento de bancos de dados (SGBDs).

### Consultas

Algumas consultas realizadas no projeto:

### Consulta ao banco de dados

#### **1. Listar todos os mundos**

````π ∗ ​(Mundo)````

####  **2. Listar todas as regiões e seus respectivos mundos**

```
πRegiao.nome,Mundo.nome​(σRegiao.id_mundo=Mundo.id_mundo​(Regiao×Mundo))

```
 
#### **3. Detalhes de um personagem específico**

```

π∗​(σid_personagem=valor_especifico​(Personagem))

```
 

#### **4. Selecionar jogadores registrados:**
```
πnome​(Personagem)

```

#### **5. Selecionar Missão do jogador:**
```
πnome​(σid_missao=valor_especifico​(Missao))

```

#### **6. Consultar Vida do jogador:**
```

πvida​(σid=valor_especifico​(Personagem))

```

#### **7. Consultar salas conectadas a partir do personagem:**
```

πid_sala​(σPersonagem.id_sala_conectada=Sala.id_sala​(Personagem⋈Sala))

```

#### **8. Quantidade de Inimigos na sala**

```

γCOUNT(id_instancia)​(σid_sala=(πid_sala​(σid_pc=valor_especıˊfico​(Personagem)))​(InstanciaInimigo))

```

#### **9. Atualizar o resultado do combate**

```sql

Atualizar Combate.resultado para "venceu" onde Combate.id_combate=valor_especifico.

```

#### **10. Consultar o total gasto em transações de venda**

```sql

  γSUM(Valor)​(σtipo=′venda′​(Transacao))

```

#### **11. Atualizar status de combate do chefe**

```sql

  Atualizar Chefe.combat_status para "confuso" onde Chefe.id_personagem=valor_especıˊfico.

```


#### **12. Listar todos os itens do inventário do personagem**

```sql

  πInstancia_item​(σid_inventario=(πid_personagem​(σid=valor_especıˊfico​(PC)))​(Inventario))

```

#### **13. Listar todos os itens de um bau**

```sql

  πitens​(σid_bau=valor_especıˊfico​(Bau))

```

#### **14. Listar missões pendentes do personagem**

```

πPC.nome,MissaoPrincipal.nome​((MissaoPrincipal⋈MissoesRealizadas)⋈PC)

```

#### **15. Missões que trazem mais recompensas**

```

πnome,qnt_xp,descricao​(τqnt_xp DESC​(Missao))[:5]


```

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 12/01/2024 | Primeira versão da Algebra_relacional | [Márcio Henrique](https://github.com/DeM4rcio)  |

</center>

