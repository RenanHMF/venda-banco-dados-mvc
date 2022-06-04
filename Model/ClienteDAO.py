import mysql.connector

from Model.Cliente import Cliente

class ClienteDao:
    def __init__(self):
        self.con = None
        self.cursor = None

    def conectar(self):
        self.con = mysql.connector.connect(host='localhost',
                                           database='Venda', user='root', password='')
        if not self.con.is_connected():
            return False
        self.cursor = self.con.cursor()
        return True

    def desconectar(self):
        if self.con.is_connected():
            self.con.close()

    def cadastrar(self, cliente):
        sql = 'INSERT INTO CLIENTE VALUES (%s,%s,%s,%s,%s)'
        valores = (cliente.getId(), cliente.getNome(), cliente.getEndereco(),
                   cliente.getTelefone(), cliente.getCpf())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def consultar(self, id):
        sql = 'SELECT * FROM CLIENTE WHERE ID_CLIENTE =' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        for (id, nome, endereco, telefone, cpf) in self.cursor:
            c = Cliente(id, nome, endereco, telefone, cpf)
            return c
        return None

    def atualizar(self, c):
        sql = 'UPDATE CLIENTE SET NOME=%s, ENDERECO=%s, TELEFONE=%s, CPF=%s WHERE ID_CLIENTE =%s'
        valores = (c.getNome(), c.getEndereco(), c.getTelefone(), c.getCpf(), c.getId())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def excluir(self, id):
        sql = 'DELETE FROM CLIENTE WHERE ID_CLIENTE =' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False