media = float(input("Digite o valor da média das notas: "))
nFaltas = float(input("Digite o numero de faltas: "))

if media >=7 and nFaltas <=32:
    print("Aprovado.")
elif media <7 and nFaltas <=32:
    print("Reprovado por nota.")
elif nFaltas >32 and media >=7:
    print("Reprovado por falta.")
elif media <7 and nFaltas >32:
    print("Reprovado por falta e por nota.")
