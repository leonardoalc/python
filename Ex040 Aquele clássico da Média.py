print("-=-" * 11)
print("          HENRIQUE LAGE")
print("-=-" * 11)
nome = str(input("Aluno: ")).strip().capitalize()
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
m = (n1 + n2 + n3) / 3
import time
print("Calculando média...")
print("Carregando resultado...")
time.sleep(2)
if m < 5 and m >= 0.0:
    print("""{} ficou com média {:.1f}\nPortanto está \033[0;31mREPROVADO(A)\033[0;0m""".format(nome, m))
elif m >= 5 and m <= 6.9:
    print("""{} está com média {:.1f}\nPortanto está de \033[0;33mRECUPERAÇÃO\033[0;0m""".format(nome, m))
elif m >= 7 and m <= 10:
    print("""{} ficou com média {:.1f}\nPortanto está \033[0;36mAPROVADO\033[0;0m""".format(nome, m))
else:
    print("INSIRA VALORES VÁLIDOS!!!!")
