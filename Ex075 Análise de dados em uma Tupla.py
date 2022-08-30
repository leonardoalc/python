parcount = 0
numcount = 0
nums = tuple(int(input("Digite um valor: ")) for n in range(4))
print(f"Os valores digitados foram {nums}")
print(f"O número 9 apareceu {nums.count(9)}x")
if 3 in nums:
    print(f"O número 3 apareceu na {nums.index(3) + 1}ª posição")
else:
    print("O número 3 não apareceu em nenhuma posição")
for c in nums:
    if nums[0 + numcount] % 2 == 0:
        parcount = parcount + 1
    numcount = numcount + 1
print(f"Quantos números pares: {parcount}")
