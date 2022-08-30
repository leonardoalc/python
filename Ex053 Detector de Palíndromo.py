frase = str(input("Frase: ")).strip().lower()
frasewords = frase.split()
frasejunta = "".join(frasewords)
inverso = ""
print(frasejunta)
for c in range(len(frasejunta), 0, -1):
    inverso += frasejunta[c]
print (inverso)
# DEU TUDO ERRADO E EU NN TERMINEI, PORTANTO EU DECLARO QUE SOU UM LIXO EM STR
