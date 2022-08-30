lista = []
listapar = []
listaimp = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimp.append(num)
    sair = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if "N" in sair:
        break
print(f"Você digitou os valores {lista}")
print(f"Os valores pares são {listapar}")
print(f"Os valores impares são {listaimp}")
    