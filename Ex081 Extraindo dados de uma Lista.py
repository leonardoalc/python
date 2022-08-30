lista = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    sair = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if "N" in sair:
        break
lista.sort(reverse=True)
print("Você digitou {} elementos".format(len(lista)))
print(f"Os valores em ordemd decrescente são: {lista}",)
if 5 in lista:
    print("5 está presente na lista!")
else:
    print("5 não está presente na lista!")
