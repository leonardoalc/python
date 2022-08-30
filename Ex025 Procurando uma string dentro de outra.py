nome = str(input("Qual o seu nome completo?").lower().strip())
if nome.find("silva") == -1:
    print("False")
else:
    print("True")
