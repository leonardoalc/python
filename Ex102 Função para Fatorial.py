# DEF #
def fatorial(num, show=False):
    """
    -=> Mostra o fatorial de um número
    :param num: Número a ser fatorado
    :param show: default =False, se =True ele mostrará os detalhes do fatoramento
    :return: O valor do num fatorado 
    """
    f = 1
    for fc in range(num, 0, -1):
        if show:
            if fc == 1:
                print(f"{fc} = ", end="")
            else:
                print(f'{fc} x ', end="")
        f *= fc
    return f


# PROGRAMA #
print(fatorial(9, True))
print(help(fatorial))
