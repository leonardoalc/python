#   Converta temp
temp = float(input("Qual a temperatura? (°C)"))
temp_fah = (((temp * 9) / 5) + 32)
print("A temperatura é de {}°C, em fahrenheit é de {:.4}°F".format(temp, temp_fah))
