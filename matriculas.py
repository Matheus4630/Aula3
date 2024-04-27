from random import randint
from unittest import case

listaMatriculas = list
def geraMatricula(modo):
    match modo:
        case 1:
            matricula = randint(1000, 9999)
            return matricula
        case 2:
            matricula = randint(10000, 99999)
            return matricula
        case 3:
            matricula = randint(100000, 999999)
            return matricula
        case 4:
            matricula = randint(1000000, 9999999)
            return matricula
        case 5:
            matricula = randint(10000000, 99999999)
            return matricula

def verificarMatricula(matriculas, newMatricula):
    for matricula in matriculas:
        if matricula == newMatricula:
            return True
    return False

def adicionarMatricula(tipo):
    while True:
        matricula = geraMatricula(tipo)
        if verificarMatricula(listaMatriculas, matricula):
            continue
        listaMatriculas.append(matricula)
        break
    return matricula
