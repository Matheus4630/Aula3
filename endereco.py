class Endereco:
    def __init__(self, cidade, bairro, rua, numero):
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

    def getEndereco(self):
        return self.cidade, self.bairro, self.rua, self.numero

    def setEndereco(self, cidade, bairro, rua, numero):
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

