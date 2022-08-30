# DEF #
def titulo(titulo):
    print("~" * (len(titulo) + 4))
    print(f"  {titulo}")
    print("~" * (len(titulo) + 4))


# PROGRAMA #
while True:
    print("~~~~~~~~~~")
    print("  PYHELP  ")
    print("~~~~~~~~~~")
    func = str(input("Função ou Biblioteca: ")).strip()
    print(titulo(f"ACESSANDO O HELP DE {func.upper()}"))
    print(help(func))
    