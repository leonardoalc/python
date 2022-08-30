dicio = {"Nome": str(input("Nome: ")), "Media": float(input("Media: "))}
print('-------------------------------')
if dicio["Media"] < 5:
    dicio["Situação"] = "Reprovado"
elif dicio["Media"] >= 5 and dicio["Media"] < 7:
    dicio["Situação"] = "Recuperação"
else:
    dicio["Situação"] = "Aprovado"
for k, v in dicio.items():
    print(f"- {k} é igual a {v}")
