cont = 1
cont_mult = 0
n = int(input("Digite o número: "))
for c in range(1, n + 1):
    if n % cont == 0:
        print("\033[0;36m{}\033[0;0m".format(cont), end=" ")
        cont_mult = cont_mult + 1
    else:
        print("\033[0;31m{}\033[0;0m".format(cont), end=" ")
    cont = cont + 1
print("")
print("O número {} foi divisível {}x".format(n, cont_mult))
if cont_mult == 2:
    print("Portanto,\n{} é um número primo".format(n))
else: 
    print("Portanto,\n{} não é um número primo".format(n))
