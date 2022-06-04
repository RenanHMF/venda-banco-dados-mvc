from Model.Produto import Produto
from Model.ProdutoDAO import ProdutoDAO

class ProdutoController:
    def __init__(self):
        self.pDAO = ProdutoDAO()
        self.produto = None

    def cadastrar(self, id, descricao, valor, tipoSetor):
        produto = Produto(id, descricao, valor, tipoSetor)

        consulta = self.consultar(id)
        if (consulta == None):
            return self.pDAO.cadastrar(produto)
        return False

    def atualizar(self, id, descricao, valor, tipoSetor):
        if not self.produto.getId() == int(id):
            return False
        self.produto.setDescricao(descricao)
        self.produto.setValor(float(valor))
        self.produto.setTipoSetor(tipoSetor)
        return self.pDAO.atualizar(self.produto)

    def consultar(self, id):
        self.produto = self.pDAO.consultar(id)

        if self.produto != None:
            dados = [str(self.produto.getId()),
                     str(self.produto.getDescricao()),
                     str(self.produto.getValor()),
                     str(self.produto.getTipoSetor())]
            return dados
        return None

    def excluir(self, id):
        consulta = self.consultar(id)

        if consulta == None:
            return False
        return self.pDAO.excluir(int(id))