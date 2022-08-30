s = 0
cont = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        s = s + n
        cont = cont + 1
    else:
        break
print(f"Foram registrados {cont} números e a soma deles foi {s}")