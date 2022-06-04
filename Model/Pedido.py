class Pedido:
    id = 0
    data = ''
    quantidade = 0
    valorTotal = 0.00
    id_produto = 0
    id_cliente = 0

    def __int__(self, id, data, quantidade, valorTotal, id_produto, id_cliente):
        self.id = id
        self.data = data
        self.quantidade = quantidade
        self.valorTotal = valorTotal
        self.id_produto = id_produto
        self.id_cliente = id_cliente

    def getId(self):
        return self.id

    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

    def getQuantidade(self):
        return self.quantidade
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getValorTotal(self):
        return self.valorTotal
    def setValorTotal(self, valorTotal):
        self.valorTotal = valorTotal

    def getIdProduto(self):
        return self.id_produto

    def getIdCliente(self):
        return self.id_cliente