n = int(input("Digite o número: "))
cont = n - 1
tot = n
print("{}! = ".format(n), end="")
while cont != 0:
    if cont != 1:
        print("{} x ".format(cont), end="")
    else: 
        print("{} = ".format(cont), end="")
    tot = tot * cont
    cont = cont - 1
print("{}".format(tot))
