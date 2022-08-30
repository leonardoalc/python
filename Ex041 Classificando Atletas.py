from datetime import date
ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano
if idade <= 9 and idade >= 1:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: MIRIM")
elif idade <= 14 and idade >= 10:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: INFANTIL")
elif idade <= 19 and idade >= 15:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: JÚNIOR")
elif idade <= 25 and idade >= 20:
    print("O atleta tem {} anos".format(idade))
    print("Categoria: SÊNIOR")
elif idade > 25:
    print("O atleta tem {} anos ".format(idade))
    print("Categoria: MASTER")
else:
    print("COLOQUE VALORES \033[0;31mVÁLIDOS\033[0;0m")
