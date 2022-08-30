tot = contmil = cont = 0
while True:
    # REGISTRO
    nomeprod = str(input("Nome do produto: ")).strip()
    preco = int(input("Digite o preço: R$"))
    sair = " "
    
    # PROGRAMA
    if cont == 0 or menor > preco:
        menor = preco
        nomemenor = nomeprod
    if preco >= 1000:
        contmil = contmil + 1
    tot = tot + preco

    # SAIDA
    while sair not in "SN":
        sair = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if sair == "N":
        break
print(f"O total da compra foi: R${tot}")
print(f"O produto mais barato foi: {nomemenor}, R${menor}")
print(f"Produtos custando mais de R$1000: {contmil}")
