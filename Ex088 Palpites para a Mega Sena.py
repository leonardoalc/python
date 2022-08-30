from random import randint
lista = list()
jogo = list()
quant = int(input("Quantos jogos quer sortear: "))
for c in range(quant):
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador == 6:
            jogo.append(lista[:])
            lista.clear()
            break
for c1 in range(quant):
        print(f"O {c1 + 1}º jogo é: {sorted(jogo[c1])}")
 