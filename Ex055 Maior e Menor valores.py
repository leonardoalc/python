cont = 0
sair = False
tot = 0
while not sair == True:
    n = int(input("Digite um número: "))
    if cont == 0:
        menor = maior = n
    if n > maior:
        maior = n
    if menor > n:
        menor = n
    
    cont = cont + 1
    tot = tot +  n
    ask = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if ask == "N":
        sair = True
media = tot / cont
print("Você digitou {} números e a média foi {}".format(cont, media))
print("O maior número foi {}".format(maior))
print("O menor número foi {}".format(menor))
    