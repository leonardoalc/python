somid = 0
mid_maior = 0
cont_fmenor = 0
for cont in range(1, 5):
    print("-=" * 8)
    print("{}ª PESSOA!".format(cont))
    nome = str(input("Nome: ")).strip().capitalize()
    sexo = str(input("Sexo [F/M]: ")).strip().lower()
    idade = int(input("Idade: "))
    somid = somid + idade
    if sexo == "m" and idade > mid_maior:
        mid_maior = idade
        nome_maior = nome
    if sexo == "f" and idade < 20:
        cont_fmenor = cont_fmenor + 1

# Média idade
media = somid / 4
print("A média de idade foi: {:.2f}".format(media))

# Homem mais velho
if mid_maior == 0:
    print("Não tivemos homens registrados!")
else:
    print("O homem mais velho foi: {}, de {} anos".format(nome_maior, mid_maior))

# Mulher -20 anos
if cont_fmenor == 0:
    print("Não tivemos mulheres abaixo dos 20 anos registradas!")
else:
    print("Tivemos {} mulheres abaixo dos 20 anos".format(cont_fmenor))
