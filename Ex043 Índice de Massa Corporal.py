altura = float(input("Altura: "))
peso = int(input("Peso: "))
imc = peso / (altura * altura)
print("Seu IMC é {:.2f}".format(imc))
if imc <= 18.5:
    print("Está ABAIXO do peso ideal!!")
elif imc <= 25:
    print("O peso é IDEAL!!")
elif imc <= 30:
    print("Está com SOBREPESO!!")
elif imc <= 40:
    print("Está com OBESIDADE!!")
else:
    print("Está com OBESIDADE MÓRBIDA!! CUIDADO!!")
