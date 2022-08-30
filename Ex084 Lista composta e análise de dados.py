pessoas = list()
nomepeso = [str(), int()]
nomepeso1 = [[], []]
contpess = pesomaior = pesomenor = 0
while True:
    # Salvando dados e copiando para a lista pessoas
    nomepeso[0] = str(input("Nome: "))
    nomepeso[1] = int(input("Peso: "))
    pessoas.append(nomepeso[:])
    # Adicionando os primeiros valores
    if contpess == 0:
        pesomenor = nomepeso[1]
        pesomaior = nomepeso[1]
    # Salvando os nomes do peso maior e menor e o valor dos pesos
    # caso hajam empates nos maiores e menores pesos
    if nomepeso[1] == pesomaior:
        nomepeso1[0].append(nomepeso[0])    
        pesomaior = nomepeso[1]
    if nomepeso[1] == pesomenor:
        nomepeso1[1].append(nomepeso[0])
        pesomenor = nomepeso[1]
    # Salvando os nomes do peso maior e menor e o valor dos pesos
    # Caso NÃO haja empates nos maiores e menores pesos
    if nomepeso[1] > pesomaior:
        nomepeso1[0].clear()
        nomepeso1[0].append(nomepeso[0])    
        pesomaior = nomepeso[1]
    if nomepeso[1] < pesomenor:
        nomepeso1[1].clear()
        nomepeso1[1].append(nomepeso[0])
        pesomenor = nomepeso[1]
    # Finalizando o código
    contpess += 1
    sair = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if "N" in sair:
        break
print("=" * 30)
print(f"Foram registradas {contpess} pessoas")
print(f"As pessoas mais pesadas, com {pesomaior}Kg, foram ", end="")
for p in nomepeso1[0]:
    print(f"{p}, ", end="")

print(f"\nAs pessoas mais leves, com {pesomenor}Kg, foram ", end="")
for pe in nomepeso1[1]:
    print(f"{pe}, ", end="")
