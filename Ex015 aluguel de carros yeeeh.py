# Aluguelzinho
dias = int(input("Por quantos dias você ficou com o carro?"))
dias_result = dias * 60 #reais por dia
km = float(input("Por quantos KMs você andou com ele?"))
km_result = km * 0.15 #reais por litro
result = dias_result + km_result
print("Você andou por {}Km que custaram R${}".format(km, km_result))
print("Você ficou com o carro por {} dias que custaram R${}".format(dias, dias_result))
print("O total ficou R${}".format(result))