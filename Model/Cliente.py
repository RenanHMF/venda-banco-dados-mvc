class Cliente :
    id = 0
    nome = ''
    endereco = ''
    telefone = ''
    cpf = ''

    def __int__(self, id, nome, endereco, telefone, cpf):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getEndereco(self):
        return self.endereco
    def setEndereco(self, endereco):
        self.endereco = endereco

    def getTelefone(self):
        return self.telefone
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getCpf(self):
        return self.cpf
    def setCpf(self, cpf):
        self.cpf = cpf