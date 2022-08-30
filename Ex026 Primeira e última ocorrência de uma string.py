frs = str(input("Digite uma frase").lower().strip())
print("A letra 'A' aparece {}x".format(frs.count("a")))
print("A primeira letra 'A' aparece na posição {}".format(frs.find("a")))
print("A ultima letra 'A' aparece na posição {}".format(frs.rfind("a")))
