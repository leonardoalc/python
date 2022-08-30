# DEF #
def leiaint():
    while True:
        numero = str(input("Digite um número: ")).strip()
        if numero.isnumeric():
            return int(numero)
        else:
            print("\033[0;31mERRO! Digite um valor numérico...\033[0;0m")


# PROGRAMA #
n = leiaint()
print(f"Você digitou {n}")
