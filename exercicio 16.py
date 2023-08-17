numero = int(input("Digite um numero inteiro de 3 dígitos: "))
n1 = numero // 100
n2 = (numero % 100) // 10
n3 = (numero % 100) % 10
soma = n1 + n2 + n3
print(soma)
if soma % 4==0 and 16 % soma==0:
    print("Seu numero é multiplo de 4 e divisivel por 16.")
else:
    print("Seu numero nao é multiplo de 4 e nao é divisivel por 16.")
