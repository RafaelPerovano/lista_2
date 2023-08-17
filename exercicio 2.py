d1 = float(input("Digite a distancia do carro1: "))
t1 = float(input("Digite o tempo do carro1: "))
d2 = float(input("Digite a distancia do carro2: "))
t2 = float(input("Digite o tempo do carro2: "))
media1 = d1/t1
media2 = d2/t2
if media1 > media2:
    print("O primeiro carro teve maior velocidade media")
elif media2 > media1:
    print("O segundo carro teve maior velocidade media")
else:
    print("Os dois possuem a mesma velocidade media")
