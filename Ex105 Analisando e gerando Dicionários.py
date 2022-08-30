# DEF #
def notas(*notas, sit=False):
    """
    -=> Função para análisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    result = dict()
    result["total"] = len(notas)
    result["maior"] = max(notas)
    result["menor"] = min(notas)
    result["média"] = float(f"{(sum(notas) / len(notas)):.1f}")
    if sit:
        if result["média"] < 5:
            result["situação"] = "RUIM"
        elif result["média"] > 5 and result["média"] < 8:
            result["situação"] = "OK"
        else:
            result["situação"] = "EXCELENTE"
    return result


# PROGRAMA #
a = notas(5.5, 9.5, 10, 6.5, sit=True)
print(a)
