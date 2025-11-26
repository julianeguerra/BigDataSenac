CREATE DATABASE vendas_online;
USE vendas_online;

CREATE TABLE produtos (
 id_produto INT PRIMARY KEY,
 nome VARCHAR(255),
 categoria VARCHAR(100),
 preco DECIMAL(10, 2),
 estoque INT
);


-- QDL (Data Query Language)
SELECT * FROM produtos;
SELECT nome, preco FROM produtos;

SELECT nome, preco FROM produtos
WHERE preco > 1000;

SELECT nome, preco, categoria FROM produtos
WHERE categoria = 'Eletrônicos';

-- --- RETORNO ERRO CSV AULA 03 (Data Injection via Table Data Import Wizard) ---

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)
'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE "C:/Users/juliane.guerra/OneDrive - SENAC RIO/Documentos/BigDataSenac/UC2/Aula03/vendas_produtos.csv" -- Ajuste o caminho no seu banco local
INTO TABLE vendas_online.produtos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_produto, nome, categoria, @preco_var, estoque) -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente


