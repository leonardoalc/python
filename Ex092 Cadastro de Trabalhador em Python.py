from datetime import date
dados = {"nome": str(input("Nome: ")), "nascimento": int(input("Nascimento: ")), 
    "CTPS": int(input("CTPS (0 = não tem): "))}
dados["idade"] = abs(dados["nascimento"] - date.today().year)
if dados["CTPS"] != 0:
    dados["ano contratação"] = int(input("Ano de contratação: "))
    dados["salario"] = int(input("Salário: "))
    dados["aposentadoria"] = (dados["ano contratação"] - dados["nascimento"]) + 35
print("===========================================")
for k, v in dados.items():
    print(f"{k} é {v}")
