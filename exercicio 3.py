import datetime
dataAtual = datetime.date.today()
ano = dataAtual.year
nome1 = str(input("Digite o nome da primeira pessoa: "))
idade1 = int(input("Digite a idade da primeira pessoa: "))
nome2 = str(input("Digite o nome da segunda pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))
 
if idade1 > idade2:
    pessoaMaisNova = nome2
    nascimento = ano - idade2
else:
    pessoaMaisNova = nome1
    nascimento = ano - idade1
    
print("{} e a pessoa mais nova e seu ano de nascimento é {}".format(pessoaMaisNova, nascimento ))