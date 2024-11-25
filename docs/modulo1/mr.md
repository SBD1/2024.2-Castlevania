# MR - Modelo Relacional

O **Modelo Relacional** é uma abordagem lógica para organizar dados em um banco de dados, onde as informações são representadas em tabelas (também chamadas de relações). Ele é amplamente utilizado devido à sua simplicidade, flexibilidade e forte fundamento matemático.

#### **Principais Conceitos**

1. **Tabelas (Relações):** Representam entidades ou objetos, como **Clientes**, **Produtos** ou **Pedidos**.  
   - Cada tabela é composta por linhas (**tuplas**) e colunas (**atributos**).

2. **Atributos:** Correspondem às características dos dados armazenados em uma tabela, como `nome`, `preço` ou `quantidade`.

3. **Chave Primária (PK):** Um atributo (ou conjunto de atributos) que identifica de forma única cada tupla em uma tabela.  
   - Exemplo: `id_cliente` em uma tabela de **Clientes**.

4. **Chave Estrangeira (FK):** Um atributo em uma tabela que referencia a chave primária de outra tabela, estabelecendo um relacionamento.  
   - Exemplo: `id_cliente` na tabela **Pedidos**, que referencia a tabela **Clientes**.

5. **Relacionamentos entre Tabelas:** Definem como os dados em diferentes tabelas estão conectados, podendo ser:  
   - **1:1 (Um para Um):** Cada funcionário tem um crachá exclusivo.  
   - **1:N (Um para Muitos):** Um cliente pode fazer vários pedidos.  
   - **N:M (Muitos para Muitos):** Alunos podem estar matriculados em várias disciplinas, e cada disciplina pode ter vários alunos.

6. **Integridade de Dados:** Regras que garantem a consistência dos dados no banco de dados, incluindo:  
   - **Integridade Referencial:** As chaves estrangeiras devem corresponder a valores existentes.  
   - **Integridade de Domínio:** Os valores dos atributos devem obedecer às restrições definidas, como tipo de dado ou intervalo.

---

#### **Por que Usar o Modelo Relacional?**

O Modelo Relacional oferece uma forma eficiente e lógica de organizar e acessar dados. Sua estrutura facilita:  
- **Manutenção:** Simplifica alterações e atualizações no banco de dados.  
- **Consulta:** Permite realizar operações complexas usando SQL.  
- **Integridade:** Ajuda a garantir que os dados sejam consistentes e confiáveis.  
- **Escalabilidade:** Suporta o crescimento do banco de dados sem perda de desempenho.

### Modelo Relacional (MR)

Abaixo está o nosso Modelo Relacioanl interativo:

<center>

<iframe 
  src="https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=MR-Castlevania.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1iqkQ5bLyo5ngIUHikCxP1Zgu3P8RBQPV%26export%3Ddownload" 
  width="100%" 
  height="600px" 
  style="border:none;">
</iframe>

V1 do MR.

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 24/11/2024 | Primeira versão  do MER  | Grupo |

</center>
