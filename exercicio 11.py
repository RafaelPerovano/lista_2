ano = int(input("Digite um ano: "))
mes = str(input("Digite um mês: "))
mes.lower

if mes == "janeiro":
    dias = 31
elif mes == "fevereiro":
    if ano % 100 != 0 and ano % 4 == 0:
        dias = 29
    else:
        dias = 28
elif mes == "março" or mes == "marco":
    dias = 31
elif mes == "abril":
    dias = 30
elif mes == "maio":
    dias = 31
elif mes == "junho":
    dias = 30
elif mes == "julho":
    dias = 31
elif mes == "agosto":
    dias = 31
elif mes == "setembro":
    dias = 30
elif mes == "outubro":
    dias = 31
elif mes == "novembro":
    dias = 30
elif mes == "dezembro":
    dias = 31
print("Seu mês tem {} dias.".format(dias))