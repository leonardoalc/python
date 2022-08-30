import datetime
from time import sleep
nada = ("\033[0;0m")
vermelho = ("\033[0;31m")
amarelo = ("\033[0;33m")
verde = ("\033[0;32m")
ciano = ("\033[0;36m")
azul = ("\033[0;34m")
roxo = ("\033[0;35m")
print("CONTAGEM REGRESSIVA PARA {}".format(datetime.date.today().year + 1))
for c in range(10, 0, -1): 
    print(c)
    sleep(1)
print("{}F{}{}E{}{}L{}{}I{}{}Z{} {}A{}{}N{}{}O{} {}N{}{}O{}{}V{}{}O{}".format(vermelho, nada, amarelo, nada, verde, nada, ciano, nada, azul, nada, roxo, nada, vermelho, nada, amarelo, nada, verde, nada, ciano, nada, azul, nada, roxo, nada))
