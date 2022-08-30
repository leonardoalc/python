cont18 = contF20 = contM = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ").strip().upper()[0])
    if idade >= 18:
        cont18 = cont18 + 1
    if sexo == "M":
        contM = contM + 1
    if sexo == "F" and idade < 20:
        contF20 = contF20 + 1
    sair = " "
    while sair not in "SN":
        sair = str(input("Deseja continuar [S/N]: ").strip().upper()[0])
    if sair == "N":
        break
print("-" * 40)
print(f"Total de pessoas com mais de 18 anos: {cont18}")
print(f"Total de pessoas do sexo masculino: {contM}")
print(f"Total de mulheres com menos de 20 anos: {contF20}")
