import math

z = float(input("Digite o valor de z: "))
w = float(input("Digite o valor de w: "))
if w>0 or z<7:
    x = (5 * w + 1) / 3
    t = 5 * z + 2
else:
    x = 5 * z + 2
    t = (5 * w + 1) / 3
xraiz = math.sqrt(x)
y = 7 * (x*x*x) - 3 * xraiz - 8 * t / 5 * x + 5 * 1
print("Y é igual a {:.2f}".format(y))
