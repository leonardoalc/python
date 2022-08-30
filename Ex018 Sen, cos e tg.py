#                        IMPORTANDO
from math import sin, cos, tan, radians
num = int(input("Digite um número"))
print("O seno de {} é {:.2f}\nseu cosseno é {:.2f}\nsua tangente é {:.2f}".format(num, sin(radians(num)), cos(radians(num)), tan(radians(num))))
