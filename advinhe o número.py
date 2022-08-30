from random import randint
print("-=" * 16)
print("        JOGO DE ADVINHAÇÃO")
print("-=" * 16)
sn = ""
bot = randint(1, 10)
while sn != "n":

    player = int(input("Seu palpite: "))
    if player > bot:
        print("Chute um número menor!")
    elif player < bot:
        print("Chute um número maior!")
    elif player == bot:
        print("Parabéns, você acertou!!!")
        sn = str(input("Aperte ENTER para jogar novamente!\nOu Digite 'n' para parar!\n")).strip().lower()
    print("-=" * 16)
