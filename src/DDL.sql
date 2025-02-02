BEGIN TRANSACTION;

-- Tabelas base
CREATE TABLE IF NOT EXISTS Mundo (
    id_mundo SERIAL NOT NULL PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    data DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Item (
    id_item SERIAL NOT NULL PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    descricao VARCHAR(200) NOT NULL
);



CREATE TABLE IF NOT EXISTS Personagem (
    id_personagem SERIAL PRIMARY KEY NOT NULL,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(50) NOT NULL,
    tipo VARCHAR(3) NOT NULL,
    CHECK (tipo IN ('PC', 'NPC'))
);

CREATE TABLE IF NOT EXISTS Regiao (
    id_regiao SERIAL NOT NULL PRIMARY KEY,
    id_regiao_conectada INT,
    id_mundo INT NOT NULL,
    nome VARCHAR(200) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    dificuldade VARCHAR(50) NOT NULL,
    CHECK (id_regiao != id_regiao_conectada),
    FOREIGN KEY (id_regiao_conectada) REFERENCES Regiao(id_regiao),
    FOREIGN KEY (id_mundo) REFERENCES Mundo(id_mundo)
);

CREATE TABLE IF NOT EXISTS Sala (
    id_sala SERIAL NOT NULL PRIMARY KEY,
    id_regiao INT NOT NULL,
    nome VARCHAR(200) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    FOREIGN KEY (id_regiao) REFERENCES Regiao(id_regiao)
);

CREATE TABLE IF NOT EXISTS InstanciaItem (
    id_instancia_item SERIAL NOT NULL PRIMARY KEY,
    id_item INT NOT NULL,
    id_sala INT NOT NULL,
    FOREIGN KEY (id_item) REFERENCES Item(id_item),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala)
);

CREATE TABLE IF NOT EXISTS Missao (
    id_missao SERIAL NOT NULL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    qnt_xp INT NOT NULL,
    descricao VARCHAR(200) NOT NULL
);

-- Tabelas dependentes
CREATE TABLE IF NOT EXISTS PC (
    id_personagem SERIAL PRIMARY KEY REFERENCES Personagem(id_personagem),
    hp INT NOT NULL CHECK (hp BETWEEN 0 AND 1000),
    mp INT NOT NULL CHECK (mp BETWEEN 0 AND 1000),
    xp INT NOT NULL CHECK (xp BETWEEN 0 AND 1000),
    absorcao INT NOT NULL CHECK (absorcao BETWEEN 0 AND 1000),
    atk INT NOT NULL CHECK (atk BETWEEN 0 AND 1000),
    lvl INT NOT NULL CHECK (lvl BETWEEN 1 AND 1000),
    luck INT NOT NULL CHECK (luck BETWEEN 0 AND 1000),
    combat_status VARCHAR(20) NOT NULL,
    CHECK (combat_status IN ('Confuso', 'Envenenado', 'Normal')),
    coins INT NOT NULL CHECK (coins BETWEEN 0 AND 1000),
    id_sala INT NOT NULL REFERENCES Sala(id_sala)
);

CREATE TABLE IF NOT EXISTS NPC (
    id_personagem SERIAL PRIMARY KEY REFERENCES Personagem(id_personagem),
    tipo VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Mercador (
    id_personagem SERIAL PRIMARY KEY REFERENCES NPC(id_personagem),
    id_sala INT NOT NULL REFERENCES Sala(id_sala)
);

CREATE TABLE IF NOT EXISTS Contratante (
    id_personagem SERIAL PRIMARY KEY REFERENCES NPC(id_personagem),
    id_sala INT NOT NULL REFERENCES Sala(id_sala)
);

CREATE TABLE IF NOT EXISTS Inimigo (
    id_personagem SERIAL PRIMARY KEY REFERENCES NPC(id_personagem),
    hp INT NOT NULL CHECK (hp BETWEEN 1 AND 1000),
    xp INT NOT NULL CHECK (xp BETWEEN 1 AND 1000),
    absorcao INT NOT NULL CHECK (absorcao BETWEEN 1 AND 1000),
    atk INT NOT NULL CHECK (atk BETWEEN 1 AND 1000),
    habilidade INT NOT NULL CHECK (habilidade BETWEEN 1 AND 1000)
);

CREATE TABLE IF NOT EXISTS Chefe (
    id_personagem SERIAL PRIMARY KEY REFERENCES NPC(id_personagem),
    hp INT NOT NULL CHECK (hp BETWEEN 1 AND 1000),
    xp INT NOT NULL CHECK (xp BETWEEN 1 AND 1000),
    lvl INT NOT NULL CHECK (lvl BETWEEN 1 AND 1000),
    combat_status VARCHAR(20) NOT NULL,
    CHECK (combat_status IN ('Confuso', 'Envenenado', 'Normal')),
    absorcao INT NOT NULL CHECK (absorcao BETWEEN 1 AND 1000),
    atk INT NOT NULL CHECK (atk BETWEEN 1 AND 1000),
    item_especial INT NOT NULL REFERENCES Item(id_item),
    id_sala INT NOT NULL REFERENCES Sala(id_sala)
);

CREATE TABLE IF NOT EXISTS InstanciaInimigo (
    id_instancia SERIAL PRIMARY KEY NOT NULL,
    id_inimigo INT NOT NULL REFERENCES Inimigo(id_personagem),
    id_sala INT NOT NULL REFERENCES Sala(id_sala),
    vida_atual INT NOT NULL CHECK (vida_atual BETWEEN 1 AND 1000),
    absorcao INT NOT NULL CHECK (absorcao BETWEEN 1 AND 1000),
    atk INT NOT NULL CHECK (atk BETWEEN 1 AND 1000),
    habilidade INT NOT NULL CHECK (habilidade BETWEEN 1 AND 1000),
    combat_status VARCHAR(20) NOT NULL,
    CHECK (combat_status IN ('Confuso', 'Envenenado', 'Normal'))
);

CREATE TABLE IF NOT EXISTS Checkpoint (
    id_checkpoint SERIAL PRIMARY KEY NOT NULL,
    id_sala INT NOT NULL REFERENCES Sala(id_sala),
    id_pc INT NOT NULL REFERENCES PC(id_personagem)
);

CREATE TABLE IF NOT EXISTS Bau (
    id_bau SERIAL PRIMARY KEY NOT NULL,
    itens INT NOT NULL REFERENCES Item(id_item)
);

CREATE TABLE IF NOT EXISTS SalaBau (
    id_bau INT NOT NULL REFERENCES Bau(id_bau),
    id_sala INT NOT NULL REFERENCES Sala(id_sala),
    PRIMARY KEY (id_bau, id_sala)
);

CREATE TABLE IF NOT EXISTS Conexao (
    id_conexao SERIAL PRIMARY KEY NOT NULL,
    id_sala_origem INT NOT NULL,
    id_sala_destino INT NOT NULL,
    direcao VARCHAR(20) NOT NULL,
    descricao_conexao TEXT,
    FOREIGN KEY (id_sala_origem) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_sala_destino) REFERENCES Sala(id_sala),
    CHECK (direcao IN ('Norte', 'Sul', 'Leste', 'Oeste'))
);

CREATE TABLE IF NOT EXISTS Dialogo (
    id_dialogo SERIAL NOT NULL PRIMARY KEY,
    id_personagem INT NOT NULL,
    texto VARCHAR(200) NOT NULL,
    FOREIGN KEY (id_personagem) REFERENCES Personagem(id_personagem)
);

CREATE TABLE IF NOT EXISTS Transacao (
    id_transacao SERIAL NOT NULL PRIMARY KEY,
    id_mercador INT NOT NULL,
    id_pc INT NOT NULL,
    valor INT NOT NULL,
    tipo VARCHAR(10) NOT NULL,
    CHECK (tipo IN ('venda', 'compra')),
    FOREIGN KEY (id_mercador) REFERENCES Mercador(id_personagem),
    FOREIGN KEY (id_pc) REFERENCES PC(id_personagem)
);

CREATE TABLE IF NOT EXISTS Combate (
    id_combate SERIAL NOT NULL PRIMARY KEY,
    id_pc INT NOT NULL,
    id_inimigo INT NOT NULL,
    resultado VARCHAR(20) NOT NULL,
    CHECK (resultado IN ('venceu', 'derrotado', 'fugiu')),
    FOREIGN KEY (id_pc) REFERENCES PC(id_personagem),
    FOREIGN KEY (id_inimigo) REFERENCES InstanciaInimigo(id_instancia)
);

CREATE TABLE IF NOT EXISTS Inventario (
    id_inventario SERIAL NOT NULL PRIMARY KEY REFERENCES PC(id_personagem),
    id_instancia_item INT NOT NULL,
    FOREIGN KEY (id_instancia_item) REFERENCES InstanciaItem(id_instancia_item)
);

CREATE TABLE IF NOT EXISTS Loja (
    id_loja SERIAL NOT NULL PRIMARY KEY,
    id_mercador INT NOT NULL,
    id_instancia_item INT NOT NULL,
    FOREIGN KEY (id_mercador) REFERENCES Mercador(id_personagem),
    FOREIGN KEY (id_instancia_item) REFERENCES InstanciaItem(id_instancia_item)
);



CREATE TABLE IF NOT EXISTS MissoesRealizadas (
    id_missao SERIAL NOT NULL,
    id_pc INT NOT NULL,
    PRIMARY KEY (id_missao, id_pc),
    FOREIGN KEY (id_missao) REFERENCES Missao(id_missao),
    FOREIGN KEY (id_pc) REFERENCES PC(id_personagem)
);

CREATE TABLE IF NOT EXISTS MissaoPrincipal (
    id_missao SERIAL NOT NULL PRIMARY KEY REFERENCES Missao(id_missao),
    id_dependencia INT NOT NULL,
    FOREIGN KEY (id_dependencia) REFERENCES Missao(id_missao)
);

CREATE TABLE IF NOT EXISTS Contrato (
    id_missao SERIAL NOT NULL PRIMARY KEY REFERENCES Missao(id_missao),
    id_dependencia INT,
    id_contratante INT NOT NULL,
    CHECK (id_missao != id_dependencia),
    FOREIGN KEY (id_dependencia) REFERENCES Contrato(id_missao),
    FOREIGN KEY (id_contratante) REFERENCES Contratante(id_personagem)
);

CREATE TABLE IF NOT EXISTS Chave (
    id_item SERIAL PRIMARY KEY REFERENCES Item(id_item),
    bau_requerido VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Arma (
    id_item SERIAL PRIMARY KEY REFERENCES Item(id_item),
    dano INT NOT NULL CHECK (dano BETWEEN 1 AND 1000)
);

CREATE TABLE IF NOT EXISTS Efeito (
    id_efeito SERIAL PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_efeito) REFERENCES Efeito(id_efeito)
);

CREATE TABLE  IF NOT EXISTS Consumivel (
    id_item SERIAL PRIMARY KEY REFERENCES Item(id_item),
    id_efeito INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade BETWEEN 1 AND 1000),
    FOREIGN KEY (id_efeito) REFERENCES Efeito(id_efeito)
);

CREATE TABLE IF NOT EXISTS Habilidade (
    id_habilidade SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Grimorio (
    id_item SERIAL PRIMARY KEY REFERENCES Item(id_item),
    xp_necessario INT NOT NULL CHECK (xp_necessario BETWEEN 1 AND 1000),
    id_habilidade INT NOT NULL,
    FOREIGN KEY (id_habilidade) REFERENCES Habilidade(id_habilidade)
);

CREATE TABLE IF NOT EXISTS Historia (
    id_item SERIAL PRIMARY KEY,
    texto VARCHAR(500)
);



COMMIT;
