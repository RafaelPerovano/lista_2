tipo = str(input("Digite o tipo de consumidor: (residencial, comercial, industrial): "))
consumo = float(input("Digite o valor consumido em KWh: "))
total = 0
tipo = tipo.lower()

if tipo == "industrial":
    total = 0.68 * consumo + 34
elif tipo == "comercial":
    total = 0.37 * consumo + 45
else:
    total = 0.77 * consumo - 22
print("Seu valor total a ser pago é de {}R$".format(total))