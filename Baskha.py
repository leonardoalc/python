from math import sqrt
xa = float(input("Primeiro Coeficiente: "))
xb = float(input("Segundo  Coeficiente: "))
xc = float(input("Terceiro Coeficiente: "))
delta = xb ** 2 - 4 * xa * xc
if delta < 0:
    print("Não possui raizes reais")
elif delta == 0:
    print("Possui apenas uma raiz real")
else:
    x1 = (-xb + (sqrt(delta))) / (2 * xa)
    x2 = (-xb - (sqrt(delta))) / (2 * xa)
    print("Possui duas raizes reais")
    print("X'  = {:.2f}".format(x1))
    print("X'' = {:.2f}".format(x2))
