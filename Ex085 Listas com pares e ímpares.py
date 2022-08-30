lista = [[], []]
cont = 0
while True:
    num = int(input("Digite um número: "))
    if num in lista:
        print("Este número já foi digitado!")
    else:
        if num % 2 == 0:
            lista[0].append(num)
            cont += 1
        else:
            lista[1].append(num)
            cont += 1
    if cont == 7:
        break
lista[0].sort()
lista[1].sort()
print(f"Os valores pares digitados foram: ", end="")
for c in lista[0]:
    if c == min(lista[0]):
        print(f"{c}, ", end="")
    elif c == max(lista[0]):
        print(f"{c}")
    else:
        print(f"{c}, ", end="")
print(f"Os valores impares digitados foram: ", end="")
for c in lista[1]:
    if c == min(lista[1]):
        print(f"{c}, ", end="")
    elif c == max(lista[1]):
        print(f"{c}")
    else:
        print(f"{c}, ", end="")
