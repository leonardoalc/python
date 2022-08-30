# Salario + Aumento 15%
sal = float(input("Qual o salario do funcionario?"))
desc = sal * 15 / 100
sal_desc = sal + desc 
print("O salario do funcionario era R${} mas com o aumento agora é R${:.6}".format(sal, sal_desc))
