# 4FUN
print("-=-" * 15)
print("         Calculadora de Empréstimos")
print("-=-" * 15)
# Variaveis base
casa_valor = float(input("Qual o valor da casa?"))
sal = float(input("Qual o Salário?"))
temp_pag = int(input("Em quantos anos irá pagar?"))

# Calculando Prestações mensais
prest_anual = casa_valor / temp_pag
prest_mes = prest_anual / 12

# Calculando 30%
sal_30 = (sal * 30) / 100 

# Concluindo
print("Para pegar uma casa de R${} em {} anos".format(casa_valor, temp_pag))
print("Você vai precisar pagar R${:.2f} por mês".format(prest_mes))
if prest_mes > sal_30:
    print("R${:.2f}, \033[1;31mé mais de 30%\033[0;0m do seu salário que é de \033[0;32mR${}\033[0;0m".format(prest_mes, sal))
    print("Portanto, seu empréstimo foi \033[1;31mNEGADO\033[0;0m!")
else:
    print("R${:.2f}, \033[0;36mé menos de 30%\033[0;0m do seu salário que é de \033[0;32mR${}\033[0;0m".format(prest_mes, sal))
    print("Portanto, seu empréstimo foi \033[0;36mAPROVADO\033[0;0m!")
