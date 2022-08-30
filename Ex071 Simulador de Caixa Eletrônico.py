cont50 = cont20 = cont10 = cont1 = 0
print("-=" * 15)
print("{:^30}".format("BANCO L&B"))
print("-=" * 15)
valor = int(input("Digite o valor a ser sacado: R$"))
tot = valor
while True:
    while tot != 0:
        tot = tot - 50
        cont50 = cont50 + 1
        if tot < 0:
            tot = tot + 50
            cont50 = cont50 - 1
            while tot != 0:
                tot = tot - 20
                cont20 = cont20 + 1
                if tot < 0:
                    tot = tot + 20
                    cont20 = cont20 - 1
                    while tot != 0:
                        tot = tot - 10
                        cont10 = cont10 + 1
                        if tot < 0:
                            tot = tot + 10
                            cont10 = cont10 - 1
                            while tot != 0:
                                tot = tot - 1
                                cont1 = cont1 + 1
    if tot == 0:
        break
print("-=" * 15)
print(f"O valor inserido foi R${valor}")
if cont50 != 0:
    print(f"Serão sacadas:\n{cont50:3>} notas de R$50")
if cont20 != 0:
    print(f"{cont20:3>} notas de R$20")
if cont10 != 0:
    print(f"{cont10:3>} notas de R$10")
if cont1 != 0:
    print(f"{cont1:3>} moedas de R$1")
print("Obrigado, volte sempre!!!!")
