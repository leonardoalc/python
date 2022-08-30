l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos \033[0;36mPODEM\033[0;0m formar um triangulo!!")
    if l1 == l2 and l2 == l3:
        print("Todos os lados são IGUAIS, portanto")
        print("O triangulo é \033[0;36mEQUILATERO\033[0;0m!!")
    #                        L1                          /                         L2                          /                         L3
    #                                                 FAZENDO O ESCALENO COMO UM MACACO MANCO IMBECIL E SEM CEREBRO
    elif (l1 == l2 and l1 != l3) or (l1 == l2 and l1 != l2) or (l2 == l1 and l2 != l3) or (l2 == l3 and l2 != l1) or (l3 == l1 and l3 != l2) or (l3 == l2 and l3 != l1):
        print("Dois lados são IGUAIS e um DIFERENTE, portanto")
        print("O triangulo é \033[0;36mISÓSCELES\033[0;0m!!")
    elif l1 != l2 and l2 != l3:
        print("\033[0;31mNENHUM\033[0;0m lado é igual, portanto")
        print("O triangulo é \033[0;36mESCALENO\033[0;0m!!")
else:
    print("Os segmento \033[0;31mNÃO PODEM\033[0;0m formar um triangulo!!")
