import mysql.connector

from Model.Pedido import Pedido

class PedidoDAO:
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

    def cadastrar(self, pedido):
        sql = 'INSERT INTO PEDIDO VALUES (%s,%s,%s,%s,%s,%s)'
        valores = (pedido.getId(), pedido.getData(),
                   pedido.getQuantidade(), pedido.getValorTotal(),
                   pedido.getIdProduto(), pedido.getIdCliente())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def consultar(self, id):
        sql = 'SELECT * FROM PEDIDO WHERE ID =' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        for (id, data, quantidade, valorTotal, id_produto, id_cliente) in self.cursor:
            p = Pedido(id, data, quantidade, valorTotal, id_produto, id_cliente)
            return p
        return None

    def atualizar(self, p):
        sql = 'UPDATE PEDIDO SET DATA=%s, QUANTIDADE=%s, VALORTOTAL=%s'
        valores = (p.getData(), p.getQuantidade(), p.getValorTotal())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def excluir(self, id):
        sql = 'DELETE FROM PEDIDO WHERE ID =' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False