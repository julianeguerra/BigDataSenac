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

-- Aula 04

-- Criar tabela clientes
CREATE TABLE clientes (
 id_cliente INT PRIMARY KEY,
 nome VARCHAR(255),
 email VARCHAR(255)
);

-- Carregar tabela clientes
LOAD DATA LOCAL INFILE "C:/Users/juliane.guerra/OneDrive - SENAC RIO/Documentos/BigDataSenac/UC2/Aula04/vendas_clientes.csv"
INTO TABLE vendas_online.clientes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(id_cliente, nome, email);

-- Criar tabela pedidos
CREATE TABLE pedidos (
 id_pedido INT PRIMARY KEY,
 id_cliente INT,
 data_pedido DATE,
 valor_total DECIMAL(10, 2), 
 id_produto INT,
 quantidade INT,
 FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
 FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- Comando para alterar a tabela e inserir colunas
-- --- Exemplo para alterar e inserir chave estrangeira ---
ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_produtos
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

-- Carregar tabela pedidos (carreguei pelo table wizard)
-- LOAD DATA LOCAL INFILE
-- INTO TABLE vendas_online.pedidos
-- FIELDS TERMINATED BY '\r\n'
-- IGNORE 1 ROWS
-- (id_pedido, id_cliente, data_pedido, valor_total, id_produto, quantidade)

 SELECT * FROM clientes, pedidos, produtos;
 
SELECT c.nome, p.data_pedido
FROM clientes c
JOIN pedidos p ON c.id_cliente = p.id_cliente;

SELECT c.nome as Cliente, p.data_pedido, t.nome as Produto
FROM clientes c
JOIN pedidos p ON c.id_cliente = p.id_cliente
JOIN produtos t ON t.id_produto = p.id_produto;
