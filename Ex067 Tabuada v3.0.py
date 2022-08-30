print("-=" * 15)
while True:
    n = int(input("Tabuada de qual número: "))
    print("-=" * 15)
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f"{n} x {c:>2} = {n * c}")
    print("-=" * 15)
print("Programa finalizado. Volte sempre!!")    