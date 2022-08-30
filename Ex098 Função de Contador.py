# IMPORT's #
from time import sleep


# DEF's #
c = 0
def contador(i, f, p):
    print("-=" * 25)
    print(f"Contagem de {i} a {f} de {abs(p)} em {abs(p)}")
    sleep(1)
    print("Iniciando...")
    sleep(1)
    if f > i:
        for c in range(i, f + abs(p), p):
            if c > f:
                break
            print(f"{c}...", end="", flush=True)
            sleep(0.5)
        print("FIM") 
    else:
        for c in range(i, f + p, p):
            if c < f:
                break
            print(f"{c}...", end="", flush=True)
            sleep(0.5)
        print("FIM") 


# Programa Principal #
contador(1, 10, 1)
contador(10, 0, -2)
print("-=" * 25)
print("Agora é a sua vez...")
while True:
    ini = int(input("Início: "))
    fim = int(input("Fim: "))
    while True:
        pas = int(input("Passo: "))
        if pas != 0:
            break
        else:
            print("O passo não pode ser 0! Tente novamente...")
    contador(ini, fim, pas)
    while True:
        sair = str(input("Deseja contar novamente? [S/N]")).strip().upper()[0]
        if sair not in "SN":
            print("Por favor, responda apenas com S ou N...")
        else: 
            break
    if sair == "N":
        break
    print("-=" * 25)
print("FINALIZANDO PROGRAMA...")
