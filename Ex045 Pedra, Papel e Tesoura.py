import random
from time import sleep
itens = ("", "Pedra", "Papel", "Tesoura")
bot = random.randint(1, 3)
player = int(input("""ESCOLHA!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Sua escolha: """))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print("-=-" * 12)
print("O Bot escolheu {}".format(itens[bot]))
print("Você escolheu  {}".format(itens[player]))
print("-=-" * 12)
if bot == 1:
    if player == 1:
        print("EMPATE!!")
    elif player == 2:
        print("VOCÊ VENCEU!!")
    elif player == 3:
        print("VOCÊ PERDEU!!")
elif bot == 2:
    if player == 1:
        print("VOCÊ PERDEU!!")
    elif player == 2:
        print("EMPATE!!")
    elif player == 3:
        print("VOCÊ GANHOU!!")
elif bot == 3:
    if player == 1:
        print("VOCÊ GANHOU!!")
    elif player == 2:
        print("VOCÊ PERDEU!!")
    elif player == 3:
        print("EMPATE!!!")
