nome = str(input("Qual o seu nome?")).strip()
print("Seu nome em maiusculo é {}".format(nome.upper()))
print("Seu nome em minusculo é {}".format(nome.lower()))
nome_div = nome.split()
print("Seu nome tem {} letras".format(len(''.join(nome_div))))
#
# Para eliminar os espaços eu poderia colocar o seguinte comando
# no lugar do join, - nome.count(" "), assim ele contaria os espaços
# e retiraria eles, e tambem me faria poder utilizar uma unica
# variavel no codigo, podendo assim otimizar o codigo 
#
print("Seu primeiro nome tem {} letras".format(len(nome_div[0])))
#
# Para otimizar mais ainda, eu poderia eliminar a segunda variavel
# utilizando o comendo find, fincando...
# .format(nome.find(" ")), assim ele procuraria o primeiro espaço
# e tudo que tem antes seria o primeiro nome já que eu usei
# .strip no começo para cortar os espaços aos cantos que
# poderiam aparecer
