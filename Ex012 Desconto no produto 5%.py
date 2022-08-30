# Desconto no produto 5%
preco = float(input("Qual o preço do produto?"))
desc = preco * 5 / 100
pre_desc = preco - desc
print("O produto custa R${}, mas com desconto de 5% vai custar R${}".format(preco, pre_desc))
