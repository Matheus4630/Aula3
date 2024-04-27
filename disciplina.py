
class Disciplina:
    def __init__(self, nome, professor, sala):
        self.nome = nome
        self.professor = professor
        self.sala = sala

    def getDisciplina(self):
        return self.nome, self.professor, self.sala

    def setDisciplina(self, nome, professor, sala):
        self.nome = nome
        self.professor = professor
        self.sala = sala

