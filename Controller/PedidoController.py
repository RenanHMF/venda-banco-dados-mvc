from Model.Pedido import Pedido
from Model.PedidoDAO import PedidoDAO

class PedidoController:
    def __init__(self):
        self.pDAO = PedidoDAO()
        self.pedido = None

    def cadastrar(self, id, data, quantidade, valorTotal, id_produto, id_cliente):
        pedido = Pedido(id, data, quantidade, valorTotal, id_produto, id_cliente)

        consulta = self.consultar(id)
        if (consulta == None):
            return self.pDAO.cadastrar(pedido)
        return False

    def atualizar(self, id, data, quantidade, valorTotal):
        if not self.pedido.getId() == int(id):
            return False
        self.pedido.setData(data)
        self.pedido.setQuantidade(int(quantidade))
        self.pedido.setValorTotal(float(valorTotal))
        return self.pDAO.atualizar(self.pedido)

    def consultar(self, id):
        self.pedido = self.pDAO.consultar(id)

        if self.pedido != None:
            dados = [str(self.pedido.getId()),
                     str(self.pedido.getData()),
                     str(self.pedido.getQuantidade()),
                     str(self.pedido.getValorTotal()),
                     str(self.pedido.getIdProduto()),
                     str(self.pedido.getIdCliente())]
            return dados
        return None

    def excluir(self, id):
        consulta = self.consultar(id)

        if consulta == None:
            return False
        return self.pDAO.excluir(int(id))