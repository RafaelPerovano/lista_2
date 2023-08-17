hInicial = int(input("Digite a hora inical do jogo: "))
mInicial = int(input("Digite o minuto incial do jogo: "))
hFinal = int(input("Digite a hora final do jogo: "))
mFinal = int(input("Digite o minuto final do jogo: "))

hDuracao = 0
mDuracao = 0
if hInicial >= 24 or  mInicial >= 60 or hFinal >= 24 or mFinal >= 60:
    print("Entrada de dados inválida.")
else:
    if hFinal > hInicial:
        hDuracao = hFinal - hInicial
    else:
        hDuracao = 24 - hInicial + hFinal
        
    if mFinal > mInicial:
        mDuracao = mFinal - mInicial
    else:
        mDuracao = 60 - mInicial + mFinal
        
    if mDuracao >= 60:
        mDuracao = mDuracao - 60
        hDuracao = hDuracao + 1

    print(hDuracao, ":",mDuracao)