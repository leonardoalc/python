from random import randint
n = randint(0, 10)
player = ""
cont = 0
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Jogo da Advinhação!!!!")
print("O computador irá escolher um número de 0 a 10\nTente advinhar o númeoro com menos tentativas que seu oponente!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
while player != n:
    player = int(input("Escolha seu número: "))
    cont = cont + 1
    if player > n:
        print("Menos... Tente novamente!!")
    elif player < n:
        print("Mais... Tente novamente!!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Parabéns, você acertou!!")
print("Foram necessárias {} tentativas.".format(cont))    
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
