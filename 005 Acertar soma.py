c = int(12)
acertou = False
while acertou == False:
    r = int(input('Qual é a soma de 5 + 7? '))
    if r != c:
        print('Errou, tente novamente.')
    elif r == c:
        acertou = True
        print('Correto')