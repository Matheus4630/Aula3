from endereco import Endereco
from pessoa import Pessoa
from contato import Contato

class Aluno(Pessoa, Endereco, Contato):
    def __init__(self, nome, idade, sexo, cpf, cidade, bairro, rua, numero, telefone, email, curso, matricula):
        Pessoa.__init__(self, nome, idade, sexo, cpf)
        Endereco.__init__(self, cidade, bairro, rua, numero)
        Contato.__init__(self, telefone, email)
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = list

    def getAluno(self):
        return (self.nome, self.idade, self.sexo, self.cpf, self.cidade, self.bairro, self.rua, self.numero,
                self.telefone, self.email,self.matricula, self.curso, self.disciplinas)

    def setAluno(self, nome=None, idade=None, sexo=None, cpf=None, cidade=None, bairro=None,
                 rua=None, numero=None, telefone=None, email=None, matricula=None, curso=None, disciplinas=None):
        if nome is not None:
            self.nome = nome
        if idade is not None:
            self.idade = idade
        if sexo is not None:
            self.sexo = sexo
        if cpf is not None:
            self.cpf = cpf
        if cidade is not None:
            self.cidade = cidade
        if bairro is not None:
            self.bairro = bairro
        if rua is not None:
            self.rua = rua
        if numero is not None:
            self.numero = numero
        if telefone is not None:
            self.telefone = telefone
        if email is not None:
            self.email = email
        if matricula is not None:
            self.matricula = matricula
        if curso is not None:
            self.curso = curso
        if disciplinas is not None:
            self.disciplinas = disciplinas

