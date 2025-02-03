BEGIN TRANSACTION;

-- Inserções na tabela Mundo
INSERT INTO Mundo (id_mundo, nome, data) VALUES 
(1, 'Mundo 1', '2024-01-01') ON CONFLICT (id_mundo) DO NOTHING;

-- Inserções na tabela Regiao
INSERT INTO Regiao (id_regiao, id_regiao_conectada, id_mundo, nome, descricao, dificuldade) VALUES 
(1, NULL, 1, 'Jardim do castelo', 'Jardim do castelo do dracula.', 'Fácil'),
(2, 1, 1, 'Entrada do Castelo', 'Entrada do castelo.', 'Médio'),
(3, 2, 1, 'Corredores Assombrados', 'Corredores longos e cheios de armadilhas.', 'Médio'),
(4, 3, 1, 'Salão do Trono', 'O salão principal onde Drácula aguarda.', 'Difícil') ON CONFLICT (id_regiao) DO NOTHING;

-- Inserções na tabela Sala
INSERT INTO Sala (id_sala, id_regiao, nome, descricao) VALUES 
(1, 1, 'Jardim do castelo', 'O início da aventura.'),
(2, 1, 'Entrada do castelo', 'Local belo cheios de objetos de ouro.'),
(3, 3, 'Corredor Principal', 'Um corredor longo e escuro, com armadilhas por todos os lados.'),
(4, 3, 'Biblioteca Antiga', 'Uma sala cheia de livros antigos e segredos.'),
(5, 4, 'Salão do Trono', 'O local onde Drácula aguarda seu desafio final.') ON CONFLICT (id_sala) DO NOTHING;

-- Inserções na tabela Conexao
INSERT INTO Conexao (id_conexao, id_sala_origem, id_sala_destino, direcao, descricao_conexao) VALUES 
(1, 1, 2, 'Norte', 'Um corredor escuro leva à entrada do castelo.'),
(2, 2, 1, 'Sul', 'Um corredor escuro leva de volta ao jardim.'),
(3, 2, 3, 'Leste', 'Uma passagem leva aos corredores assombrados.'),
(4, 3, 2, 'Oeste', 'Uma passagem retorna à entrada do castelo.'),
(5, 3, 4, 'Norte', 'Uma porta pesada leva à biblioteca antiga.'),
(6, 4, 5, 'Norte', 'Uma escadaria leva ao salão do trono.') ON CONFLICT (id_conexao) DO NOTHING;

-- Inserções na tabela Personagem
INSERT INTO Personagem (id_personagem, nome, descricao, tipo) VALUES 
(2, 'Mercador', 'Vendedor de itens raros.', 'NPC'),
(3, 'Morcego', 'Um inimigo pequeno e traiçoeiro.', 'NPC'),
(4, 'Contratante', 'Ajuda com contratos.', 'NPC'),
(5, 'Drácula', 'O lendário Senhor das Trevas.', 'NPC'),
(6, 'Esqueleto Guerreiro', 'Um inimigo armado com espada e escudo.', 'NPC'),
(7, 'Bibliotecário', 'Um NPC que oferece informações e itens raros.', 'NPC') ON CONFLICT (id_personagem) DO NOTHING;

-- Inserções na tabela PC

-- Inserções na tabela NPC
INSERT INTO NPC (id_personagem, tipo) VALUES 
(2, 'Mercador'),
(3, 'Inimigo'),
(4, 'Contratante'),
(5, 'Chefe'),
(6, 'Inimigo'),
(7, 'Mercador') ON CONFLICT (id_personagem) DO NOTHING;

-- Inserções na tabela Mercador
INSERT INTO Mercador (id_personagem, id_sala) VALUES 
(2, 2),
(7, 4);

-- Inserções na tabela Contratante
INSERT INTO Contratante ( id_personagem, id_sala) VALUES
(4, 2);

-- Inserções na tabela Inimigo
INSERT INTO Inimigo (id_personagem, hp, xp, absorcao, atk, habilidade) VALUES 
(3, 50, 10, 5, 10, 5),
(6, 80, 20, 10, 15, 5),
(5, 500, 100, 50, 40, 20);

-- Inserções na tabela InstanciaInimigo
INSERT INTO InstanciaInimigo (id_instancia, id_inimigo, id_sala, vida_atual, absorcao, atk, habilidade, combat_status) VALUES 
(1, 3, 2, 50, 5, 10, 5, 'Normal'),
(2, 6, 3, 80, 10, 15, 5, 'Normal'),
(3, 5, 5, 500, 50, 40, 20, 'Normal');

-- Inserções na tabela Item
INSERT INTO Item (id_item, nome, descricao) VALUES 
(1, 'Espada de Ferro', 'Uma espada básica.'),
(2, 'Poção de Cura', 'Recupera 50 pontos de vida.');

-- Inserções na tabela InstanciaItem
INSERT INTO InstanciaItem (id_instancia_item, id_item, id_sala) VALUES 
(1, 1, 1),
(2, 2, 2);

-- Inserções na tabela Bau
INSERT INTO Bau (id_bau, itens) VALUES 
(1, 1);

-- Inserções na tabela SalaBau
INSERT INTO SalaBau (id_bau, id_sala) VALUES 
(1, 1);

-- Inserções na tabela Missao
INSERT INTO Missao (id_missao, nome, qnt_xp, descricao) VALUES 
(1, 'Derrotar o Morcegos', 50, 'Encontre e elimine os morcegos no castelo.');


-- Inserções na tabela Efeito
INSERT INTO Efeito (id_efeito, tipo, descricao) VALUES 
(1, 'envenenado', 'envenenamento por segundo');

-- Inserções na tabela Consumivel
INSERT INTO Consumivel (id_item, id_efeito, quantidade) VALUES 
(2, 1, 1);

-- Inserções na tabela Chave
INSERT INTO Chave (id_item, bau_requerido) VALUES 
(1, 'Bau1');

-- Inserções na tabela Arma
INSERT INTO Arma (id_item, dano) VALUES 
(1, 100);

-- Inserções na tabela Habilidade
INSERT INTO Habilidade (id_habilidade, nome) VALUES 
(1, 'Ataque de Espada');

-- Inserções na tabela Grimorio
INSERT INTO Grimorio (id_item, xp_necessario, id_habilidade) VALUES 
(1, 100, 1);

-- Inserções na tabela Contrato
INSERT INTO Contrato (id_missao, id_dependencia, id_contratante) VALUES 
(1, NULL, 4);

INSERT INTO Historia (texto) VALUES 
(
    'O vento uiva como um lamento ancestral, ecoando pelo vale sombrio. A névoa rasteja pelo solo pedregoso, ocultando as sombras que se movem à espreita. Você sente um arrepio percorrer sua espinha quando avista, ao longe, a silhueta titânica do Castelo de Drácula, seus pináculos perfurando os céus enevoados.'

);

INSERT INTO Historia (texto) VALUES 
(
    'Uma voz grave e soturna rompe o silêncio.

??? - "Então... você ousa desafiar o Senhor das Trevas?"'

);

INSERT INTO Historia (texto) VALUES 
(
    'Uma figura encapuzada emerge da penumbra, seus olhos rubros brilhando na escuridão.

Encapuzado - "Poucos adentram estes domínios e vivem para contar a história. Você busca poder, vingança ou a ruína inevitável?"'

);


INSERT INTO Historia (texto) VALUES 
(
    'Antes que possa responder, um corvo grasna alto, e o céu se ilumina com um relâmpago. De repente, o chão sob seus pés parece tremer, como se algo ancestral despertasse.

Encapuzado - "Se deseja seguir adiante, deve provar seu valor. As forças das trevas não se curvam a meros mortais..."'

);


INSERT INTO Historia (texto) VALUES 
(
    'O vulto se dissipa como névoa, deixando para trás apenas um amuleto antigo. Ao pegá-lo, uma energia fria percorre seus dedos. O destino foi selado. A escuridão chama... e a caçada começa.'

);



COMMIT;