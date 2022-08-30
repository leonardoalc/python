from random import randint
cont = 0
print("-=" * 15)
print("       JOGO PAR OU ÍMPAR")
print("-=" * 15)
while True:
    cpu = randint(1, 10)
    escolha = str(input("Deseja par ou ímpar [P/I]: ").strip().upper()[0])
    player = int(input("Seu número: "))
    result = cpu + player
    print(f"O cpu escolheu: {cpu}")
    print(f"O resultado foi: {result}")

    # É PAR OU ÍMPAR
    if result % 2 == 0:
        print(f"{result} é par!")
    else:
        print(f"{result} é ímpar!")

    # QUEM VENCEU 
    if escolha == "P" and result % 2 == 0:
        print("Você ganhou!!")
        cont = cont + 1
    elif escolha == "I" and result % 2 != 0:
        print("Você ganhou!!")
        cont = cont + 1
    else:
        print("Você perdeu!")
        print("-=" * 15)
        break
    print("-=" * 15)
if cont == 0:
    print("Você não venceu nenhuma!")
elif cont == 1:
    print("Você venceu uma vez")
else:
    print(f"Você venceu {cont} vezes")
