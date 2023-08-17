n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
nMaior = 1
if n1>n2 and n1>n3:
    nMaior = n1
elif n2>n1 and n2>n3:
    nMaior = n2
else:
    nMaior = n3
print("Seu numero maior é {}".format(nMaior))