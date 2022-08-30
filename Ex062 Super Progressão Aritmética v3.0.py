primeiro = int(input("Digite o primeiro: "))
razao = int(input("Digite a razão: "))
fim = False
ranger = 10
cont = 0
while fim != True:
    for c in range(0, ranger):
        print("{}-> ".format(primeiro), end="")
        primeiro = primeiro + razao
        cont = cont + 1
    print("PAUSA")
    ranger = int(input("Quantos termos quer ver mais: "))
    if ranger == 0:
        fim = True
print("Progressão finalizada com {} termos".format(cont))