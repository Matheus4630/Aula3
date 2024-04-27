
class Contato:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

    def getContato(self):
        return self.telefone, self.email

    def setContato(self, telefone, email):
        self.telefone = telefone
        self.email = email
