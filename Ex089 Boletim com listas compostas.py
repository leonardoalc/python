alunos = list()
# CRIANDO DATA DOS ALUNOS #
while True:
    # Dados do Aluno # 
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    media = (nota1 + nota2 + nota3) / 3
    alunos.append([nome, nota1, nota2, nota3, media])
    # SAINDO #
    sair = str(input("Sair? [S/N]: ")).strip().upper()[0]
    if "S" in sair:
        break
# Printando Organizado #
print("-\n-\nNo    NOME            MÉDIA")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
for a in range(len(alunos)):
    print(f"{a:<5} {alunos[a][0]:<15} {alunos[a][4]:.1f}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
while True:
    sair = int(input("Deseja saber sobre qual aluno (999 para interromper): "))
    if sair == 999:
        break
    print(f"{alunos[sair][0]}\nNotas: 1ª {alunos[a][1]}, 2ª {alunos[sair][2]}, 3ª {alunos[sair][3]}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("FINALIZANDO PROGRAMA, OBG")
