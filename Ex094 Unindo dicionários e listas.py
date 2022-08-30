dados_0 = dict()
dados_1 = list()
med_id = contF = 0
while True:
    dados_0["nome"] = str(input("Nome: ")).strip()
    while True:
        dados_0["sexo"] = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if dados_0["sexo"] in "MF":
            if dados_0["sexo"] == "F":
                contF += 1
            break
        else:
            print("Por favor, utilize apenas M ou F... Tente novamente!")
    dados_0["idade"] = int(input("Idade: "))
    med_id += dados_0["idade"]
    dados_1.append(dados_0.copy())
    sair = str(input("Deseja continuar? [S/N]")).strip().upper()
    if sair == "N":
        break
    dados_0.clear
print("-=" * 25)
med_id = med_id / len(dados_1)
print(f"Foram cadastradas {len(dados_1)} pessoas.")
print(f"A média de idade é {med_id:.0f}")
print("Mulheres registradas: ", end="")
for m in dados_1:
    if m["sexo"] == "F":
        print(m["nome"], end=", ")
    if contF == 0:
        print("Nenhuma mulher foi registrada")
print("\nPessoas acima da média de idade: ", end="")
for i in dados_1:
    if i["idade"] > med_id:
        print(i["nome"], end=", ")
