from datetime import date
print("-=" * 16)
print("    CALCULADORA DE MAIORIDADE")
print("-=" * 16)
quant = int(input("Quantas pessoas: "))
menor = 0
maior = 0
for c in range(1, quant + 1):
    print("-=" * 16)
    print("")
    nome = str(input("Nome da {}ª pessoa: ".format(c))).strip().capitalize()
    ano = int(input("Em que ano {} nasceu: ".format(nome)))
    idade = abs(ano - date.today().year)
    print("{} tem {} anos".format(nome, idade))
    if idade >= 18:
        print("{} é maior de idade!".format(nome))
        maior = maior + 1
    else:
        print("{} não é maior de idade".format(nome))
        menor = menor + 1
    print("")
print("-=" * 16)
print("Foram {} pessoas maiores de idade".format(maior))
print("E {} pessoas menores de idade".format(menor))
