from Model.Cliente import Cliente
from Model.ClienteDAO import ClienteDao

class ClienteController:
    def __init__(self):
        self.cDAO = ClienteDao()
        self.cliente = None

    def cadastrar(self, id, nome, endereco, telefone, cpf):
        cliente = Cliente(id, nome, endereco, telefone, cpf)

        consulta = self.consultar(id)
        if (consulta == None):
            return self.cDAO.cadastrar(cliente)
        return False

    def atualizar(self, id, nome, endereco, telefone, cpf):
        if not self.cliente.getId() == int(id):
            return False
        self.cliente.setNome(nome)
        self.cliente.setEndereco(endereco)
        self.cliente.setTelefone(telefone)
        self.cliente.setCpf(cpf)
        return self.cDAO.atualizar(self.cliente)

    def consultar(self, id):
        self.cliente = self.cDAO.consultar(id)

        if self.cliente != None:
            dados = [str(self.cliente.getId()),
                     self.cliente.getNome(),
                     self.cliente.getEndereco(),
                     self.cliente.getTelefone(),
                     self.cliente.getCpf()]
            return dados
        return None

    def excluir(self, id):
        consulta = self.consultar(id)

        if consulta == None:
            return False
        return self.cDAO.excluir(int(id))