jog = {}
jog["nome"] = str(input("Nome: "))
jog["partidas"] = int(input("Partidas: "))
totgol = cont = 0
totgols_1 = []
for g in range(jog["partidas"]):
    gols = int(input(f"Quantos gols na partida {g}: "))
    totgols_1.append(gols)
    totgol += gols
jog["gols"] = totgols_1[:]
jog["total gols"] = totgol
print("-=" * 25)
print(jog)
print("-=" * 25)
for k, v in jog.items():
    print(f"O campo {k} é igual a {v}")
print("-=" * 25)
print(f"{jog['nome']} marcou {jog['total gols']} gols")
for g in jog["gols"]:
    print(f"=> Na partida {cont} marcou {g}")
    cont += 1
