salario = float(input("Digite o valor do seu salario: "))
finan = float(input("Digite o valor do financiamento pretendido: "))
if finan <= 5*salario:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")