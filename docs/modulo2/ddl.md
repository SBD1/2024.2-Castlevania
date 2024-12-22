# DDL - Data Definition Language

A Linguagem de Definição de Dados, ou Data Definition Language (DDL), é um conjunto de comandos usados em sistemas de gerenciamento de banco de dados (SGBD) para criar, alterar e gerenciar a estrutura dos bancos de dados.

```sql

-- criando a tabela statusNPC --

create table statusNPC (
	idStatus SERIAL primary key,
	hp INTEGER not null,
	absorcao INTEGER,
	atk INTEGER,
	combatStatus VARCHAR(255) not null
);


-- criando a tabela tblRegiao --

create table tblRegiao(
	idRegiao serial primary key not null,
	idRegiaoConectada serial not null,
	idMundo serial not null,
	nome varchar(255) not null,
	descricao varchar(255) not null,
	dificuldade char not null
);


-- criando a tabela habilidade -- 

create table tblHabilidade(
	idHabilidade serial primary key not null,
	idHabilidadeDependente integer not null,
	idGrimorio integer not null,
	efeito varchar(255) not null,
	custo integer not null,
	descricao varchar(255) not null
);

-- criando a tabela instancia inimigo --

create table instanciaInimigo(
	idInstancia integer primary key not null,
	idStatus integer
);

-- tabela inimigo --

create table tblInimigo(
	idInimigo integer primary key not null,
	nomeLoc varchar(255) not null,
	idStatus integer not null
);

-- tabela chave --

create table tblChave (
	bauReqreurido varchar(255) not null
);


-- tabela arma --

create table tblArma(
	dano integer not null
);


-- tabela consumível --

create table tblConsumivel(
	quantidade integer not null
);

-- tabela grimório --

create table tblGrimorio(
	idGrimorio integer not null primary key
);

-- implementando as chaves estrangeiras --

-- chave estrangeira da tblInimigo e instanciaInimigo --

ALTER TABLE tblInimigo
ADD COLUMN idInstancia INTEGER NOT NULL,  
ADD CONSTRAINT fk_inimigo_instancia
  FOREIGN KEY (idInstancia)
  REFERENCES instanciaInimigo(idInstancia)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

 
 -- criando a tabela localização --
 
CREATE TABLE tblLocalizacao (
    id_regiao INTEGER NOT NULL,             
    nome_loc VARCHAR(255) NOT NULL,       
    CONSTRAINT fk_localizacao_regiao       
        FOREIGN KEY (id_regiao)            
        REFERENCES tblRegiao(idRegiao)    
        ON DELETE CASCADE                  
        ON UPDATE CASCADE
);

-- chave estrangeira da tabela statusNPC --

ALTER TABLE statusnpc
ADD COLUMN idHabilidade INTEGER NOT NULL,
ADD CONSTRAINT fk_id_habilidade
    FOREIGN KEY (idHabilidade)
    REFERENCES tblhabilidade(idhabilidade)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
   
   
   
-- chaves estrangeiras da tabela habilidade --
   
   ALTER TABLE tblhabilidade
	ADD CONSTRAINT fk_id_grimorio
	FOREIGN KEY (idGrimorio)
	REFERENCES tblGrimorio(idGrimorio)
	ON DELETE CASCADE
	ON UPDATE CASCADE;

```

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 22/12/2024 | Primeira versão do DDL | [Diego Carlito](https://github.com/DiegoCarlito) e [Filipe Carvalho](https://github.com/filipe-002) |

</center>
