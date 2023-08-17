sexo = str(input("Digite seu sexo(homem ou mulher): "))
idade = int(input("Digite sua idade: "))
sexo = sexo.lower()
if sexo == "homem":
    if idade >= 21:
        print("É maior de idade.")
    else:
        print("Não é maior de idade.")
elif sexo == "mulher":
    if sexo == "mulher" and idade >= 18:
        print("É maior de idade.")
    else:
        print("Não é maior de idade.")
else:
    print("Sexo digitado errado.")