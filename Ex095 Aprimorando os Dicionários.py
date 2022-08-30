from time import sleep
jog_dad = dict()
gols_list = list()
jogadores = list()
totgols = cont = 0
while True:
    jog_dad["nome"] = str(input("Nome: "))
    jog_dad["partidas"] = int(input("Partidas: "))
    for p in range(jog_dad["partidas"]):
        gols_list.append(int(input(f"Gols na partida {p}: ")))
    for g in gols_list:
        totgols += g
    jog_dad["gols"] = gols_list[:]
    jog_dad["totalgols"] = totgols
    jogadores.append(jog_dad.copy())
    jog_dad.clear()
    gols_list.clear()
    totgols = 0
    sair = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if sair == "N":
            break
print("-=" * 25)
print(f"Cod {'Nome':<10}{'Partidas':<12}{'Gols':<5}")
print("-" * 30)
for j in range(len(jogadores)):
    print(f"{j:<3} {jogadores[j]['nome']:<10}{jogadores[j]['partidas']:<11}", 
    f"{jogadores[j]['totalgols']}")
    sleep(1)
print("-=" * 25)
while True:
    sleep(1)
    sair = int(input("Deseja detalhes de qual jogador [cod][999 para sair]: "))
    sleep(1)
    if sair == 999:
        break
    print(f"{jogadores[sair]['nome']} marcou {jogadores[sair]['totalgols']} gols",
    f"em {jogadores[sair]['partidas']} partidas")
    sleep(1)
    for g in range(len(jogadores[sair]["gols"])):
        print(f"      >>> Na partida {g} marcou {jogadores[sair]['gols'][g]} gols")
        sleep(1)
print("Obrigado, até a proxima!")
print("      >>> FINALIZANDO <<<")
sleep(3)
print("      >>> FINALIZADO <<<")
