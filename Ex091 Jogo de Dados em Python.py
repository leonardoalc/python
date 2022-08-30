from random import randint
from operator import itemgetter
jogs = {"Jogador 1": randint(1, 6), "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6), "Jogador 4": randint(1, 6)}
jogs_org = sorted(jogs.items(), key=itemgetter(1), reverse=True)
cont = 1
for k, v in jogs_org:
    print(f"{cont}º - {k}: {v}")
    cont += 1
