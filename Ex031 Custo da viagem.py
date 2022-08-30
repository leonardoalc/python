km = float(input("Qual a distancia da sua viagem? "))
if km <= 200.00:
    kmtot = km * 0.50
else:
    kmtot = km * 0.45
print("Você está prestes a viajar por {}Km".format(km))
print("O preço da sua viagem será de R${:.2f}".format(kmtot))
