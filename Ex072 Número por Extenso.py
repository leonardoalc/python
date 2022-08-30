extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze" , "doze", "treze", "catorze", "quinze", "dezesseseis", "dezessete", "dezoito", "dezenove", "vinte")
sair = " "
while sair != "N":
    while True:
        num = int(input("Digite um número de 0 a 20: "))
        if num >= 0 and num <= 20:
            break
        else:
            print("Por favor, digite um número válido!")
    print(f"Você escreveu {extenso[num]}")
    sair = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
