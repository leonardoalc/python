nums = [int(input("Digite um número: ")) for nums1 in range(5)]
posmenor = []
posmaior = []
for pos, val in enumerate(nums):
    if val == max(nums):
        posmaior.append(pos)
    if val == min(nums):
        posmenor.append(pos)
print(f"O maior valor foi {max(nums)}, encontrado em {posmaior}")
print(f"O menor valor foi {min(nums)}, encontrado em {posmenor}")
# cu
