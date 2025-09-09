a = 'x'
while type(a) != int:
    try:
        a = int(input('Digite um inteiro:\n'))
    except:
        print('Nao é um inteiro, tente novamente:\n')