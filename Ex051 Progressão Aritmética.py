primeiro = int(input("Digite o primeiro número: "))
razao = int(input("Digite a razáo: "))
decimo = primeiro + (10 -  1) * razao
for c in range (primeiro, decimo + razao, razao):
    print(c, end="-> ")
print("FIM!!")
