sal = float(input("salario "))
if sal <= 1250:
    aumento = (sal * 15) / 100
else: 
    aumento = (sal * 10) / 100
sal_tot = sal + aumento
print("O seu salário atual é de R${:.2f}".format(sal))
print("Com o aumento seu salário será de R${:.2f}".format(sal_tot))
