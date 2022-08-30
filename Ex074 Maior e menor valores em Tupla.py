from random import randint
num = tuple(randint(1, 50) for n in range(5))
print(f"Os números sorteados foram: {num}")
print(f"O maior número sorteado foi: {max(num)}")
print(f"O menor número sorteado foi: {min(num)}")
