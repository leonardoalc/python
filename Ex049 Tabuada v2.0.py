m = 0
n = int(input("Escolha um número: "))
for c in range(0, 11):
    print("{} x {:2} = {}".format(n, m, n*m))
    m = m + 1
