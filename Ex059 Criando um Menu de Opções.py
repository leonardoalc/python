sair = False
from time import sleep
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
while not sair == True:
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Sair do programa")
    menu = int(input("Sua escolha: "))
    if menu == 1:
        print("A soma de {} e {} é {}".format(n1, n2, n1 + n2))
    elif menu == 2:
        print("Multiplicando {} e {} temos {}".format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print("O maior dos valores inseridos foi {}".format(n1))
        elif n2 > n1:
            print("O maior dos valores inseridos foi {}".format(n2))
        else:
            print("Os dois valores são iguais!")
    elif menu == 4:
        print("Carregando...")
        sleep(1)
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
    elif menu == 5:
        print("Finalizando programa, aguarde.")
        sleep(2)
        exit()
    else: 
        print("INSIRA UMA OPÇÃO VÁLIDA!")
        print("Encerrando programa...")
        sleep(2)
        exit()
    sair2 = str(input("Deseja sair do programa? [Y/N]")).strip().lower()
    if sair2 == "y":
        print("Finalizando programa, aguarde.")
        sleep(2)
    if sair2 == "n":
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
