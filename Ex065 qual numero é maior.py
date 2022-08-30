print("Escolha 3 números DIFERENTES")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
print("O primeiro número é: {}".format(n1))
print("O segundo número é: {}".format(n2))
print("O terceiro número é: {}".format(n3))

#Adicionando vida ao código
print("")

#Descobrindo o maior
if n1 > n2 and n1 > n3:
    print("O maior número é: {}".format(n1))
if n2 > n1 and n2 > n3:
    print("O maior número é: {}".format(n2))
if n3 > n1 and n3 > n2:
    print("O maior número é: {}".format(n3))

#Descobrindo o menor    
if n1 < n2 and n1 < n3:
    print("O menor número é: {}".format(n1))
if n2 < n1 and n2 < n3:
    print("O menor número é: {}".format(n2))
if n3 < n1 and n3 < n2:
    print("O menor número é: {}".format(n3))

#Caso os 3 forem iguais
if n1 == n2 and n1 == n2 and n2 == n3:
    print("Os números são iguais!\nnão existe número menor!")

#Caso sejam colocanos caracteres invalidos 
