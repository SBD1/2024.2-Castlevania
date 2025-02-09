# 📌 Visão Geral

O jogo baseado em terminal (MUD) permite que os jogadores explorem um mundo interconectado, interajam com NPCs, enfrentem inimigos e completem missões. O progresso do jogador é salvo em um banco de dados PostgreSQL, garantindo uma experiência contínua e estruturada.

## 🎮 Como Jogar

### 📜 Menu Inicial

Quando o jogo é iniciado, o jogador verá o seguinte menu:

Adicionar Novo Jogador → Cria um novo personagem no banco de dados.

Listar Jogadores → Exibe todos os jogadores cadastrados.

Selecionar Jogador e Iniciar Jogo → Permite escolher um personagem para jogar.

Executar Script SQL → Executa comandos SQL personalizados.

Sair → Fecha o jogo.

### 🚶 Movimentação do Jogador

Uma vez dentro do jogo, o jogador pode realizar as seguintes ações:

Explorar a Sala Atual → Descobre inimigos, NPCs e missões disponíveis.

Mover para Outra Sala → Permite viajar para salas conectadas.

Ver Status do Jogador → Mostra atributos como vida, ataque e experiência.

Ver Inventário → Exibe os itens coletados.

Sair do Jogo → Encerra a sessão do jogador.

### 🏠 Exploração de Salas

Cada sala pode conter:

Inimigos → O jogador pode escolher lutar ou fugir.

Mercadores → NPCs que vendem itens úteis.

Contratantes → NPCs que oferecem missões ao jogador.

Missões → Objetivos que concedem recompensas ao serem concluídos.

### ⚔️ Combate

Se o jogador encontrar um inimigo, ele pode:

Atacar → Causar dano ao inimigo.

Usar Item → Recuperar vida ou ganhar bônus temporários.

Fugir → Tentar escapar da luta.

Se a vida do jogador chegar a zero, ele será derrotado.

### 🛒 Interação com Mercadores

Os jogadores podem comprar itens para melhorar suas chances de sobrevivência. O mercador possui um menu interativo para facilitar as compras.

### 🎒 Inventário

O inventário contém todos os itens coletados pelo jogador. Ele pode ser acessado a qualquer momento para visualizar ou utilizar os itens disponíveis.

### 🔧 Estrutura Técnica

Banco de Dados PostgreSQL → Armazena jogadores, salas, NPCs, itens e progressos.

Python → Linguagem principal para lógica do jogo e conexão com o banco de dados.

Interações em Terminal → Simula efeitos de digitação e menus interativos.

# 🚀 Conclusão

Este jogo combina exploração, combate e gestão de recursos para proporcionar uma experiência envolvente e estratégica. O mundo é dinâmico e pode ser expandido conforme novas funcionalidades forem adicionadas!