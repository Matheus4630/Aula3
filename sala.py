
class Sala:
    def __init__(self, bloco, sala):
        self.bloco = bloco
        self.sala = sala

    def getSala(self):
        return self.bloco, self.sala

    def setSala(self, bloco, sala):
        self.bloco = bloco
        self.sala = sala
