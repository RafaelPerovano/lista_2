dist = float(input("Digite a distancia em km: "))
litros = float(input("Digite o valor do litro gastado: "))
media = dist / litros
if media < 8:
    print("Venda o carro! ")
elif media >= 8 and media <= 14:
    print("Econômico! ")
elif media > 12:
    print("Super econômico! ")