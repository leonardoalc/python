exp = str(input("Digite a expressão: "))
pa = 0
for cont, e in enumerate(exp):
    if e == "(":
        pa += 1
    elif e == ")":
        pa -= 1
if pa != 0:
    print("Sua expressão não é válida!")
else:
    print("Sua expressão é válida!")