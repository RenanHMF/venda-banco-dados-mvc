class Produto:
    id = 0
    descricao = ''
    valor = 0.00
    tipoSetor = ''

    def __int__(self, id, descricao, valor, tipoSetor):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.tipoSetor = tipoSetor

    def getId(self):
        return self.id

    def getDescricao(self):
        return self.descricao
    def setDescricao(self, descricao):
        self.descricao = descricao

    def getValor(self):
        return self.valor
    def setValor(self, valor):
        self.valor = valor

    def getTipoSetor(self):
        return self.tipoSetor
    def setTipoSetor(self, tipoSetor):
        self.tipoSetor = tipoSetor