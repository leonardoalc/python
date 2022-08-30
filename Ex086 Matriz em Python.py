# ESTE METÓDO É RUIM E SUJO, NO 087 TEM UM METODO MELHOR
lista = []
cont = 0
while True:
    nums = int(input("Digite um número: "))
    if nums in lista:
        print(f"{nums} já está presente na matriz")
    elif nums > 999:
        print(f"{nums} é maior que 999, logo não pode ser adicionado")
    else:
        lista.append(nums)
        cont += 1
    if cont == 9:
        break
cont = 0
for c in lista:
    if cont == 2 or cont == 5:
        print(f"[{c:^3}]")
    else:
        print(f"[{c:^3}]", end="")
    cont += 1
