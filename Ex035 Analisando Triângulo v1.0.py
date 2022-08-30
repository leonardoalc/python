l1 = float(input("Primeiro Segmento"))
l2 = float(input("Segundo Segmento"))
l3 = float(input("Terceiro Segmento"))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos podem formar um triangulo")
else:
    print("Os segmento não podem formar um triangulo")
