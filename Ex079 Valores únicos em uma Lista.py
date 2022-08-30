num01 = []
sair = " "
while True:
    num02 = int(input("Digite um valor: "))
    if num02 in num01:
        print(f"{num02} já foi digitado antes! Tente novamente.")
    else:
        num01.append(num02)
    sair = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if "N" in sair:
        break
print("Você digitou os números: ", end="")
for n in sorted(num01):
    if n == max(num01):
        print(f"{n}")
    else:
        print(f"{n},", end=" ")
