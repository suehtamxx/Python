def soma(a,b):
    c = a + b
    return c
def subtrair(a,b):
    c = a - b
    return c
def multiplicar(a,b):
    c = a * b
    return c
def dividir(a,b):
    c = a / b
    return c
def recebe_val():
    print('Digite os valores para a calculadora')
    a = float(input('Digite um valor:'))
    b = float(input('Digite outro valor:'))
    return a,b
op = 0
a = 0
b = 0
while op != 5:
    op = int(input('Deseja fazer soma(1), subtracao(2), multiplicacao(3), divisao(4):'))
    if op == 1:
        a , b = recebe_val()
        r = soma(a,b)
        print(r)
    elif op == 2:
        a , b = recebe_val()
        r = subtrair(a,b)
        print(r)
    elif op == 3:
        a , b = recebe_val()
        r = multiplicar(a,b)
        print(r)
    elif op == 4:
        a , b = recebe_val()
        r = dividir(a,b)
        print(r)
    elif op == 5:
        print('Tchau...')
    else:
        print('Valor incorreto, tente novamente.')

