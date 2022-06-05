-- CRIANDO TABELA CLIENTE
CREATE TABLE CLIENTE(
    ID_CLIENTE INT PRIMARY KEY NOT NULL,
    NOME VARCHAR(255),
    ENDERECO VARCHAR(255),
    TELEFONE VARCHAR(30),
    CPF VARCHAR(30)
);

CREATE TABLE PRODUTO(
    ID_PRODUTO INT PRIMARY KEY NOT NULL,
    DESCRICAO VARCHAR(255),
    VALOR DECIMAL(10,2),
    TIPOSETOR VARCHAR(255)
);

CREATE TABLE PEDIDO(
    ID_PEDIDO INT PRIMARY KEY NOT NULL,
    DATA DATE,
    QUANTIDADE INT,
    VALORTOTAL DECIMAL(10,2),
    ID_PRODUTO INT,
    ID_CLIENTE INT,
    FOREIGN KEY (ID_PRODUTO) REFERENCES PRODUTO(ID_PRODUTO),
    FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTE(ID_CLIENTE)
);