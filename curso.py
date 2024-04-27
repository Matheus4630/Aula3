
class Curso:
    def __init__(self, nome, duracao, turno):
        self.nome = nome
        self.duracao = duracao
        self.turno = turno
        self.disciplinas = []

    def getCurso(self):
        return self.nome, self.duracao, self.turno, self.disciplinas

    def setCurso(self, nome, duracao, turno, disciplinas): #passe uma lista contendo disciplinas
        self.nome = nome
        self.duracao = duracao
        self.turno = turno
        self.disciplinas = disciplinas

    def newDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)
