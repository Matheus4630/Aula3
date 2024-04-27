
def menuHome():
    print(f"{"=" * 15} Sistema Para {"=" * 15}\n"
           "1 - Alunos\n"
           "2 - Professores\n"
           "3 - Servidores\n"
           "4-  Diretor\n"
           "5 - Coordenador\n"
           "0 - sair do programa\n")


def homeOpcoes():
    menuHome()
    try:
        num = int(input("Escolha um opção: "))
    except ValueError:
        print("digite um valor inteiro valido!")
        homeOpcoes()
    match num:
        case 1:
            print("Acessando sessão Alunos")
        case 2:
            print("Acessando sessão Professores")
        case 3:
            print("Acessando sessão Servidores")
        case 4:
            print("Acessando sessão Diretores")
        case 5:
            print("Acessando sessão Coordenadores")
        case 0:
            print("saindo do programa")
        case _:
            print("escolha uma opção valida!")
            homeOpcoes()


def menuAlunos():
    pass


def sessaoAlunos():
    pass


def menuProfessores():
    pass


def sessaoProfessores():
    pass


def menuServidores():
    pass


def sessaoServidores():
    pass


def menuDiretor():
    pass


def sessaoDiretor():
    pass


def menuCoordenador():
    pass


def sessaoCoordenador():
    pass

