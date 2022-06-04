from Model.Pedido import Pedido
from Model.PedidoDAO import PedidoDAO
from Model.ProdutoDAO import ProdutoDAO
from Model.ClienteDAO import ClienteDao


class PedidoController:
    def __init__(self):
        self.pDAO = PedidoDAO()
        self.pedido = None
        self.produtoDAO = ProdutoDAO()
        self.valorProdutoDAO = None
        self.nomeProdutoDAO = None
        self.clienteDAO = ClienteDao()
        self.nomeClienteDAO = None

    def cadastrar(self, id, data, quantidade, id_produto, id_cliente):
        self.valorProdutoDAO = self.produtoDAO.consultar(id_produto).getValor() * quantidade

        pedido = Pedido(id, data, quantidade, self.valorProdutoDAO, id_produto, id_cliente)

        consulta = self.consultar(id)
        if (consulta == None):
            return self.pDAO.cadastrar(pedido)
        return False

    def atualizar(self, id, data, quantidade, valorTotal):
        if not self.pedido.getId() == int(id):
            return False
        self.valorProdutoDAO = self.produtoDAO.consultar(self.pedido.getIdProduto()).getValor() * int(quantidade)
        self.pedido.setData(data)
        self.pedido.setQuantidade(int(quantidade))
        self.pedido.setValorTotal(float(self.valorProdutoDAO))
        return self.pDAO.atualizar(self.pedido)

    def consultar(self, id):
        self.pedido = self.pDAO.consultar(id)

        if self.pedido != None:
            self.nomeProdutoDAO = self.produtoDAO.consultar(self.pedido.getIdProduto()).getDescricao()
            self.nomeClienteDAO = self.clienteDAO.consultar(self.pedido.getIdCliente()).getNome()
            dados = [str(self.pedido.getId()),
                     str(self.pedido.getData()),
                     str(self.pedido.getQuantidade()),
                     str(self.pedido.getValorTotal()),
                     str(self.pedido.getIdProduto()) + ' - ' + str(self.nomeProdutoDAO),
                     str(self.pedido.getIdCliente()) + ' - ' + str(self.nomeClienteDAO)]
            return dados
        return None

    def excluir(self, id):
        consulta = self.consultar(id)

        if consulta == None:
            return False
        return self.pDAO.excluir(int(id))