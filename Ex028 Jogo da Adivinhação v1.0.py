from random import randint
import time
n = randint(0, 5)
print("Jogo da Advinhação!!")
print("""O computador vai falar um número de 0 a 5 
e você tem que advinhar qual ele falou!""")
n1 = int(input("Digite o número (0 a 5): "))
print("""O número que você escolheu foi {}
e o número do computador foi {}""".format(n1, n))
print("LOADING...")
time.sleep(2)
if n1 == n:
    print("Parabéns, você acertou!!!")
else:
    print("Uma pena, você errou! Tente novamente")
