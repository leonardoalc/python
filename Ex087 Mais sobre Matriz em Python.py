from parso import parse


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
# criando a matriz
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input("Digite um número: "))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
# Mostrando a Matriz
print("-=" * 15)
for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^3}]", end="")
    print()
print("-=" * 15)
print(f"A soma de todos os pares é: {par}")
print(f"O maior valor da segunda linha é: {max(matriz[1])}")
print(f"A soma da terceira coluna é: {matriz[2][0] + matriz[2][1] + matriz[2][2]}")
print("-=" * 15)
