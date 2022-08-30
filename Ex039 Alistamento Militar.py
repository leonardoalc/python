from datetime import date
sexo = int((input("""ESCOLHA 
[ 1 ] MASCULINO
[ 2 ] FEMININO
Sua escolha: """)))
if sexo == 1:
    ano = int(input("Ano de nascimento: "))

    # Calculando idade2
    idade = date.today().year - ano

    # Quanto tempo para se alistar
    if idade > 18:
        print("Você tem {} anos em {}".format(idade, date.today().year))
        tempalist = 18 - idade
        print("Portanto você já \033[0;31mDEVERIA\033[0;0m ter se alistado há \033[0;31m{} ANOS\033[0;0m".format(abs(tempalist)))
        print("Seu alistamento foi em {}".format(date.today().year - abs(tempalist)))
    elif idade == 18:
        print("Você tem 18 anos em {}".format(date.today().year))
        print("Portando você \033[0;31mDEVE\033[0;0m se alistar \033[0;31mIMEDIATAMENTE\033[0;0;m")
    else:
        print("Você tem {} anos em {}".format(idade, date.today().year))
        print("Ainda \033[0;31mNÃO\033[0;0m possui \033[0;31m18 ANOS\033[0;0m")
        print("Seu alistamento será em {}".format(ano + 18))
elif sexo == 2:
    print("Seu alistamento \033[0;31mNÃO\033[0;0m é obrigatório, femêa inútil!!!")
else:
    print("ESCOLHA UM VALOR VÁLIDO!!!!!!!")
