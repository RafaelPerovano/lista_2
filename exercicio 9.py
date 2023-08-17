sexo = str(input("Digite seu sexo(homem ou mulher): "))
sexo = sexo.lower()
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura(em cm): "))
idade = int(input("Digite sua idade: "))

if sexo == "homem" or sexo == "mulher":
    if sexo == "homem":
        cal = 66 + (13.7 * peso) + 5 * altura - 6.8 * idade
    else:
        cal = 665 + (9.6 * peso) + 1.8 * altura - 4.7 * idade
    print("O seu valor ideal de calorias diarias são {:2f} calorias.".format(cal))
else:
    print("O sexo nao foi possivel ser indentificado.")