hasteCobre = int(input("Digite quantas hastes de cobre comprada: "))
hasteAco = int(input("Digite quantas hastes de aço comprada: "))
hasteAluminio = int(input("Digite quantas hastes de alumínio comprada: "))
hasteValor = hasteCobre * 4 +hasteAco * 2.50 + hasteAluminio * 5
qHastes =  hasteCobre + hasteAco + hasteAluminio
desconto = 0

if qHastes <= 6:
    desconto = 0
elif qHastes >= 7 and qHastes <= 15:
    desconto = 0.10
elif qHastes >= 16 and qHastes <= 20:
    desconto = 0.15
elif qHastes > 20:
    desconto = 0.20
total = hasteValor - desconto * hasteValor    
print("O total que deve ser pago é de {:.2f}R$".format(total))

