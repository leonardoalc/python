palavras = ("JESUS", "MARIA", "JOSE", "JEOVA", "BRUNA", "CU",
    "BUCETA", "PIROCA", "XOTA", "JEOVANE", "VAGINA", "ROLA",
    "MICROONDAS", "PIPOCA", "HOMEM-ARANHA", "GUARANA", "BOBO")
cont = 0
for i in palavras:
    print(f"em {palavras[0 + cont]} temos as vogais: ", end= "")
    if "A" in palavras[0 + cont]:
        print("a ", end = "")
    if "E" in palavras[0 + cont]:
        print("e ", end= "")
    if "I" in palavras[0 + cont]:
        print("i ", end= "")
    if "O" in palavras[0 + cont]:
        print("o ", end= "")
    if "U" in palavras[0 + cont]:
        print("u", end= "")
    print("")
    cont += 1
