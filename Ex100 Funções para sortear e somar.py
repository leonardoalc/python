# IMPORTs #
from random import randint
from time import sleep


# DEFs#
def sortear():
    print("Os números sorteados foram: ", end="")
    for s in range(5):
        sorte = randint(1, 99)
        numeros.append(sorte)
        if s < 3:
            print(sorte, end=", ", flush=True)
        elif s == 3:
            print(sorte, end=" e ", flush=True)
        else:
            print(sorte)
        sleep(1)
def somaPar():
    cont = 0
    totpar = 0
    parnums = list()
    for p in range(len(numeros)):
        if numeros[p] % 2 == 0:
            parnums.append(numeros[p])
            cont += 1
            totpar += numeros[p]
    print("Os números pares foram: ", end="")
    if cont == 0:
        print("Não foram sorteados números pares!")
    else:
        for p2 in range(cont):
            if p2 == (cont - 1):
                print(parnums[p2])
            elif p2 == (cont - 2):
                print(parnums[p2], end=" e ", flush=True)
            else:
                print(parnums[p2], end=", ", flush=True)
            sleep(1)
        if cont > 1:
            print(f"A soma dos pares foi {totpar}")
            
           
# PROGRAMA PRINCIPAL # 
numeros = list()
sortear()
somaPar()
