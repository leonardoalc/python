aluno1 = str(input("Qual o nome do primeiro aluno?"))
aluno2 = str(input("Qual o nome do segundo aluno?"))
aluno3 = str(input("Qual o nome do terceiro aluno?"))
aluno4 = str(input("Qual o nome do quarto aluno?"))
from random import choice
result = choice([aluno1, aluno2, aluno3, aluno4])
print("O aluno sorteado foi: {}".format(result))
