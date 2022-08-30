# IMPORTs #
from time import sleep


# DEFs #
def menudef(txt):
    print("-=" * 25)
    print(f"{txt:^50}".upper())
    print("-=" * 25, end="")
    return ""
    

# PROGRAMA PRINCIPAL #
cont = 1


# CRIANDO ARQUIVO CASO NÃO EXISTA #
try:
    arquivo = open("C:/Users/Leonardo/Documents/PROGRAMAÇÃO/Workspace vscode/Python/Python Exercicios CeV/Ex155 Dados", "r")
    arquivo.close()
except FileNotFoundError:
    arquivo = open("C:/Users/Leonardo/Documents/PROGRAMAÇÃO/Workspace vscode/Python/Python Exercicios CeV/Ex155 Dados", "w")
    arquivo.close()


while True:
    # MENU #
    while True:
        try:
            menu = int(input(f"""{menudef('MENU PRINCIPAL')}
            \033[33m 1 -\033[m \033[34mVER PESSOAS CADASTRADAS\033[m
            \033[33m 2 -\033[m \033[34mCADASTRAR NOVA PESSOA\033[m
            \033[33m 3 -\033[m \033[34mSAIR DO SISTEMA\033[m
            \033[33m Sua opção: \033[m"""))
            sleep(0.5)
        except:
            print("\033[31mERRO: Digite um valor válido!\033[m")
            sleep(0.2)
        else:
            if menu > 0 and menu < 4:
               break
            else:
                print("\033[31mERRO: Digite um valor válido!\033[m")
                sleep(0.2)


    # OPÇÕES
    if menu == 3:
        sleep(0.5)
        break
    elif menu == 1:
        print(menudef(f"PESSOAS CADASTRADAS"))
        arquivo = open("C:/Users/Leonardo/Documents/PROGRAMAÇÃO/Workspace vscode/Python/Python Exercicios CeV/Ex155 Dados", "r")
        for c in arquivo.readlines():
            sleep(0.3)
            print(f"              \033[33m{cont}ª -\033[m \033[34m{c}\033[m", end="")
            cont += 1
        cont = 1
        arquivo.close()
        sleep(0.5)
    elif menu == 2:
        print(menudef(f"NOVO CADASTRO"))
        arquivo = open("C:/Users/Leonardo/Documents/PROGRAMAÇÃO/Workspace vscode/Python/Python Exercicios CeV/Ex155 Dados", "a")
        quant = int(input("\033[33m             Quantas Adicionar: \033[m"))
        sleep(0.3)
        for ap in range(quant):
            print(f"\033[33m             {ap+1}ª Pessoa: \033[m")
            nome = str(input("\033[34m             Nome: \033[m"))
            sleep(0.3)
            idade = str(input("\033[34m             Idade: \033[m"))
            arquivo.write(f"{nome:<23} {idade} anos\n")
            if ap+1 == quant:
                print("             \033[32mAdicionado!\033[m")
            else:
                print("             \033[32mAdicionado!\033[m\n")
            sleep(0.3)
        arquivo.close()
print(menudef("Encerrando programa..."))
