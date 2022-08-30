s = ""
while s != "M" and s != "F":
    s = str(input("Informe seu sexo: ")).strip().upper()
    if s != "M" and s != "F":
        print("Dados inválidos, informe novamente\n")
if s == "M":
    print("Sexo MASCULINO registrado!")
elif s == "F":
    print("Sexo FEMININO registrado!")
