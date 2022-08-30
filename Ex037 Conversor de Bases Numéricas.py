n = int(input("Digite seu número: "))
print('''Escolha o tipo de conversão
[ 1 ] Converter para \033[0;35mBINÁRIO\033[0;0m
[ 2 ] Converter para \033[0;35mHEXADECIMAL\033[0;0m
[ 3 ] Converter para \033[0;35mOCTADECIMAL\033[0;0m''')
escolha = int(input("ESCOLHA!"))
if escolha == 1:
    print("{} convertido para binário é {}".format(n, bin(n)[2:]))
elif escolha == 2:
    print("{} convertido para hexadecimal é {}".format(n, hex(n)[2:]))
elif escolha == 3:
    print("{} convertido para octadecimal é {}".format(n, oct(n)[2:]))
else:
    print("ESCOLHA UMA OPÇÃO VÁLIDA!!!")
