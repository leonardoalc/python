# DEF #
def voto(ano):
    """
    -=> Calcula se pode votar ou se é opcional.
    :param ano: Ano de nascimento
    :param idade: Calcula a idade da pessoa com base no 'ano'
    By: Leonardo
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif idade >= 16 and idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    

# PROGRAMA #
nasc = int(input("Ano de nascimento: "))
print(voto(nasc))
print(help(voto))
