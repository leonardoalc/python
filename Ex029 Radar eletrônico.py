print("-=-" * 15)
print("              RADAR ELETRÔNICO")
print("-=-" * 15)
km = int(input("Qual a velocidade do carro?"))
if km > 80:
    import time
    multa = (km - 80) * 7
    print("MULTADO! Você excedeu o limite de 80Km/h")
    time.sleep(2)
    print("Irá pagar uma multa de R${},00""".format(multa))
else:
    print("""Você não excedeu o limite de 80Km/h
    e não será multado""")
print("Tenha um bom dia e diriga com segurança!") 
