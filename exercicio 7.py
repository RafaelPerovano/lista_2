angulo1 = float(input("Digite o primeiro angulo: "))
angulo2 = float(input("Digite o segundo angulo: "))
angulo3 = float(input("Digite o terceiro angulo: "))
soma = angulo1 + angulo2 + angulo3
if soma != 180:
    print("Os angulos informados nao formam um triangulo.")
else:
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("Seu triangulo é acutângulo.")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Seu triangulo é retângulo.")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("Seu triangulo é obtusângulo.")