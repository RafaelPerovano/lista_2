nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota (de 0 a 10): "))
nota2 = float(input("Digite a segunda nota (de 0 a 10): "))
media = (nota1 + nota2)/2

if nota1 + nota2 >20:
    print("Não foi possivel caucular pois as notas nao estao dentro dos criterios.")
else:
    if media >=0 and media <5:
        print("{} com media {} foi reprovado! ".format(nome, media))
    elif media >=5 and media <7:
        print("{} com media {} esta de recuperação! ".format(nome, media))
    elif media >= 7 and media <=10:
        print("{} com media {} foi aprovado! ".format(nome, media))
