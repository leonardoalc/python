# Quantos litros de tinta por parede 
a = float(input("Qual a altura da parede?"))
c = float(input("Qual o comprimento da parede?"))
area = a * c
lt = area / 2
mlt = int(input("Quantas demãos na parede?"))
mltr = (lt * mlt)
print("A parede tem {:.4}m² e vai precisar de {:.4}L de tinta com {} demãos".format(area, mltr, mlt))
