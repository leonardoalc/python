lista = []
for c in range(5):
    num = int(input("Digite um número: "))
    if c == 0 or num > max(lista):
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos = pos + 1
print("Você digitou os números: ", end="")
for l in lista:
    if l == max(lista):
        print(l)
    elif l == lista[len(lista) - 2]:
        print(f"{l} e ", end="") 
    else:
        print(f"{l}, ", end="")
