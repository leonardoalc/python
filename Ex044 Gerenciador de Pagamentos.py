print("-=-" * 11)
print("          LOJA GUARANÁ")
print("-=-" * 11)
valor = float(input("Valor da compra: R$"))
esc = int(input("""ESCOLHA A FORMA DE PAGAMENGO
[ 1 ] á vista no dinheiro/PIX
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Sua opção: """))
if esc == 1:
    total = valor - ((valor * 10) / 100 )
    print("O total foi de R${:.2f}".format(valor))
    print("com desconto de 10% sairá por R${:.2f}".format(total))
elif esc == 2:
    total = valor - ((valor * 5) /  100)
    print("O total foi de R${:.2f}".format(valor))
    print("Com desconto de 5% sairá por R${:.2f}".format(total))
elif esc == 3:
    parc = valor / 2
    print("O total foi de R${:.2f}".format(valor))
    print("Com 2x parcelas de R${}".format(parc))
elif esc == 4:
    quant_parc = int(input("Quantas parcelas: "))
    juros = valor + ((valor * 20) / 100)
    parc =  juros / quant_parc
    print("O total foi de R${:.2f}".format(valor))
    print("Com 20% de juros o valor será de R${:.2f}".format(juros))
    print("Com {}x parcelas de R${:.2f}".format(quant_parc, parc))
