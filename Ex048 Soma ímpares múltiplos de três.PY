s = 0
r = 0
t = 0
for c in range(1, 501):
    r = r + 1
    if  r % 2 != 0 and r % 3 == 0:
        s = s + r
        t = t + 1
print("A soma de todos {} números é {}".format(t, s))
