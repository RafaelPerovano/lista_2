salario = float(input("Digite o valor do seu salario: "))
imposto = 1
deducao = 0

if salario < 1903.98:
    desconto = 0  
elif salario >= 1903.99 and salario <= 2826.65:
    imposto = 0.075
    deducao = 142.8
elif salario >= 2826.66 and salario <= 3751.05:
    imposto = 0.15
    deducao = 548.82
elif salario >= 3751.06 and salario <= 4664.68:
    imposto = 0.225
    deducao = 636.13
elif salario > 4664.68:
    imposto = 0.275
    deducao = 869.36

desconto = salario * imposto - deducao
sLiquido = salario - (salario * imposto - deducao)
print("Seu salario bruto é de {}R$, o desconto são {:.2f}R$ e seu salario liquido é de {}R$ ".format(salario, desconto, sLiquido))
