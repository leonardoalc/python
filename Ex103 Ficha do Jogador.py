# DEF #
def ficha(nome="", gols=0):
    """
    -=> Faz um cabeçalho com o nome e gols do jogador
    :param nome: Recebe o nome do jogador
    :param gols: Recebe os gols do jogador
    :return: Não retorna nada
    By: Leobardo
    """
    # Transformando STR em INT
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = -1

    # Colocando o print do nome
    if nome == "":
        print("<desconhecido> fez", end=" ")
    else:
        print(f"{nome} fez", end=" ")
    
    # Colocando os gols
    if gols < 0:
        print("<desconhecido> gols no campeonato.")
    elif gols == 0:
        print("nenhum gol no campeonato.")
    elif gols == 1:
        print("um gol no campeonato.")
    else:
        print(f"{gols} gols no campeonato.")


# PROGRAMA #
ficha()
