sair = False
tot = 0
maior = 0
cont = 0
while not sair == True:
    n = int(input("Digite um número [999 para parar]: "))
    if cont == 0:
        menor = n
    if n == 999:
        sair = True
    else:
        tot = tot + n
        cont = cont + 1
        if n > maior:
            maior = n
        if menor > n:
            menor = n
print("O total foi {}".format(tot))
print("O maior número foi {}".format(maior))
print("O menor número foi {}".format(menor))
print("Foram somados {} números".format(cont))
