# Detalhamento do Código

Este documento apresenta o detalhamento do código criado para um terminal em Python que interage com um banco de dados criado para o Castlevania. O terminal permite movimentação pelo mapa, combate, interação com baús e exibição de status do personagem.

## 📋 Funcionalidades Principais

### 1. **Exibição do Mapa**
- Mostra a sala atual do personagem.
- Lista as salas conectadas à sala atual, permitindo que o jogador visualize suas opções de movimentação.
- **Função**: `exibir_mapa(cursor, id_sala_atual)`

**Exemplo de Saída:**
```
=== MAPA ===
Você está em: Jardim do castelo - O início da aventura.

Salas conectadas:
[2] Entrada do castelo - Um local belo cheio de objetos de ouro.
```

### 2. **Movimentação do Personagem**
- Permite ao jogador mover-se entre salas conectadas.
- Atualiza a posição do personagem no banco de dados.
- **Função**: `mover_personagem(cursor, conn, id_personagem, id_sala_destino)`

**Fluxo de Uso:**
- O jogador escolhe o ID da sala para onde deseja ir.
- O sistema verifica se a sala é válida e, em caso positivo, move o personagem.

**Exemplo de Entrada:**
```
Digite o ID da sala para onde deseja ir: 2
```

**Exemplo de Saída:**
```
Você se moveu para a nova sala.
```

### 3. **Exibição do Status do Personagem**
- Mostra informações detalhadas do personagem:
  - Nome
  - HP (vida), MP (mana), XP (experiência)
  - Moedas
  - Localização atual
- **Função**: `exibir_status(cursor, id_personagem)`

**Exemplo de Saída:**
```
=== STATUS DO PERSONAGEM ===
Nome: Herói
HP: 100 | MP: 50 | XP: 10 | Coins: 20
Localização: Jardim do castelo
```

### 4. **Combate**
- Simula um combate básico contra inimigos presentes na sala.
- O jogador e o inimigo trocam ataques até que um deles seja derrotado.
- Atualiza o banco de dados para refletir o resultado do combate:
  - Remove o inimigo caso ele seja derrotado.
  - Atualiza o HP do jogador caso ele sobreviva.
- **Função**: `iniciar_combate(cursor, conn, id_personagem)`

**Fluxo de Combate:**
- O jogador encontra um inimigo e decide lutar ou fugir.
- Durante o combate, o HP do inimigo e do jogador é reduzido com base nos valores de ataque.

**Exemplo de Entrada:**
```
Deseja lutar? (s/n): s
```

**Exemplo de Saída:**
```
Você encontrou um inimigo: Goblin (HP: 30, ATK: 10)
Você venceu o combate!
```

### 5. **Interação com Baús**
- Permite que o jogador abra baús encontrados na sala.
- Mostra os itens contidos no baú e dá a opção de coletá-los ou deixá-los.
- Atualiza o banco de dados para remover o baú após a coleta.
- **Função**: `abrir_bau(cursor, conn, id_personagem)`

**Exemplo de Saída:**
```
Você encontrou um baú! Contém: Espada Lendária - Uma espada com poder mágico.
Deseja pegar o item? (s/n): s
Você pegou o item!
```

### 6. **Menu Principal**
- Apresenta um menu interativo com as seguintes opções:
  1. Exibir Mapa
  2. Mover Personagem
  3. Exibir Status do Personagem
  4. Abrir Baú
  5. Iniciar Combate
  6. Sair
- **Função**: `menu_principal()`

**Exemplo de Saída:**
```
=== MENU ===
1. Exibir Mapa
2. Mover Personagem
3. Exibir Status do Personagem
4. Abrir Baú
5. Iniciar Combate
6. Sair
Escolha uma opção: 
```

## 🛠️ Configuração Necessária

1. **Banco de Dados**:
   - Certifique-se de que o banco de dados `rpg.db` está configurado corretamente.
   - O banco deve conter as tabelas e dados necessários para salas, personagens, inimigos, baús e itens.

2. **Dependências**:
   - O código utiliza apenas a biblioteca padrão do Python (`sqlite3`), portanto, não é necessário instalar dependências externas.

3. **Execução**:
   - Salve o código em um arquivo chamado, por exemplo, `terminal_rpg_completo.py`.
   - Execute o script com o comando:
     ```bash
     python terminal_rpg_completo.py
     ```

## 🔧 Possíveis Melhorias Futuras
- Adicionar suporte a missões e eventos.
- Implementar um sistema de inventário para o personagem.
- Melhorar o combate com habilidades e efeitos especiais.
- Criar uma interface gráfica para substituir o terminal.

## 📜 Estrutura do Código

- **Conexão com o Banco**:
    - `conectar_banco()`
- **Mapa**:
    - `exibir_mapa(cursor, id_sala_atual)`
- **Movimentação**:
    - `mover_personagem(cursor, conn, id_personagem, id_sala_destino)`
- **Status do Personagem**:
    - `exibir_status(cursor, id_personagem)`
- **Combate**:
    - `iniciar_combate(cursor, conn, id_personagem)`
- **Baús**:
    - `abrir_bau(cursor, conn, id_personagem)`
- **Menu Principal**:
    - `menu_principal()`


---
**Nota**: Certifique-se de ajustar o ID do personagem jogável e os dados do banco de dados para testar corretamente o jogo.

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 23/12/2024 | Primeira versão do terminal  | [Emivalto](https://github.com/EmivaltoJrr) |