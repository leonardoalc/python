from zipfile import LargeZipFile


def area(l, c):
    a = l * c
    print(f"A área de um terreno {l} x {c} é {a:.2f}m²")
larg = float(input("Largura: "))
comp = float(input("Comprimento: "))
area(larg, comp)
