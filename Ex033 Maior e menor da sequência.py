print("-=" * 13)
print("    COMPARADOR DE PESOS")
print("-=" * 13)
from time import sleep
quantpes = int(input("\nQuantas pessoas: "))
pesomaior = 0
pesomenor = 0
for cont in range(1, quantpes + 1):
    print("")
    print("-=" * 13)
    nome = str(input("\nNome da {}ª pessoa: ".format(cont))).strip().capitalize()
    peso = int(input("Qual o peso de {}: ".format(nome)))
    if cont == 1:
        pesomenor = peso
    if peso > 600:
        sleep(1)
        print("INSIRA VALORES VÁLIDOS!!")
        sleep(1)
        print("Encerrando programa...")
        sleep(1)
        exit()
    if peso > pesomaior:
        pesomaior = peso
        nomemaior = nome
    if peso < pesomenor:
        pesomenor = peso
        nomemenor = nome
print("-=" * 13)
print("\nProcessando...")
print("")
sleep(1)
print("A pessoa mais pesada foi {}, pesando {}Kg".format(nomemaior, pesomaior))
sleep(1)
print("A pessoa mais leve foi {}, pesando {}Kg".format(nomemenor, pesomenor))
print("-=" * 13)
