while True:  
    try:
        num = int(input("Digite um inteiro: "))
    except:
        print("\033[31mERRO: Digite um valor inteiro válido\033[m")
    else:
        print(f"O número {num} foi registrado")
        break
