lista = ("AOC Hero 24inch 1080p IPS", 1500, "RTX 3050 EVGA", 2800,
    "SSD NVME 1TB KINGSTON", 800, "B450M MORTAR MAX", 408, "Ryzen 5 3600", 1119,
    "16GB RAM DDR4 2x8 Killsre 3000Mhz", 245, "Redragon Grapple", 200, "Mancer 500w 80+ Bronze", 280,
    "SSD PNY 128GB SATA", 120, "Cooler RiseMode Z2", 40, "Redragon Saturn", 120)
count1 = 0
count2 = 1
print("-=" * 20)
print("{:^40}".format("TERABYTESHOP"))
print("-=" * 20)
for l in range(len(lista) // 2):
    print(f"{lista[0 + count1]:.<35}R${lista[0 + count2]:.2f}")
    count1 = count1 + 2
    count2 = count2 + 2
