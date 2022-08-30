aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))
from random import sample
result = sample([aluno1, aluno3, aluno2, aluno4], k=4)
print ("A ordem será\n{}".format(result))
