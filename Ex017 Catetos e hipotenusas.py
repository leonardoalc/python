catop = float(input("Qual o comprimento do cateto oposto?"))
catadj = float(input("Qual o comprimento do cateto adjacente?"))
from math import sqrt
hip = sqrt((catop ** 2 + catadj ** 2))
print("A hipotenusa vai medir {:.2f}".format(hip))
