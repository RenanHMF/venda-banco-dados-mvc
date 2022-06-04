import mysql.connector

from Model.Produto import Produto

class ProdutoDAO:
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

    def cadastrar(self, produto):
        sql = 'INSERT INTO PRODUTO VALUES (%s,%s,%s,%s)'
        valores = (produto.getId(), produto.getDescricao(),
                   produto.getValor(), produto.getTipoSetor())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def consultar(self, id):
        sql = 'SELECT * FROM PRODUTO WHERE ID_PRODUTO =' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        for (id, descricao, valor, tipoSetor) in self.cursor:
            p = Produto(id, descricao, valor, tipoSetor)
            return p
        return None

    def atualizar(self, p):
        sql = 'UPDATE PRODUTO SET DESCRICAO=%s, VALOR=%s, TIPOSETOR=%s WHERE ID_PRODUTO=%s'
        valores = (p.getDescricao(), p.getValor(), p.getTipoSetor(), p.getId())
        if not self.conectar():
            return False
        self.cursor.execute(sql, valores)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False

    def excluir(self, id):
        sql = 'DELETE FROM PRODUTO WHERE ID_PRODUTO =' + str(id)
        if not self.conectar():
            return False
        self.cursor.execute(sql)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        return False