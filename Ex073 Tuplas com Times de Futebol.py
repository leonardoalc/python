times = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "RB Brangantino", 
        "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional",
        "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport",
        "Chapecoense")
print("-=" * 10)
print("{:^20}".format("BRASILEIRÃO"))
print("-=" * 10)
print(f"""No G4 temos:
1º {times[0]} 
2º {times[1]} 
3º {times[2]} 
4º {times[3]}
5º {times[4]}""")
print("-=" * 10)
print(f"""No Z4 temos:
17º {times[16]}
18º {times[17]}
19º {times[18]}
20º {times[19]}""")
print("-=" * 10)
print(f"""Em ordem alfabética:
{sorted(times)}""")
print("-=" * 10)
print(f"A chapecoense se encontra na {times.index('Chapecoense') + 1}ª posição")
print("-=" * 10)
