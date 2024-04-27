
class Pessoa:
    def __init__(self, nome, idade, sexo, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf

    def getPessoa(self):
        return self.nome, self.idade, self.sexo, self.cpf

    def setPessoa(self, nome, idade, sexo, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf

