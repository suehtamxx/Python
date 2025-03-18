a = int(input('Digite um valor:\n'))
while a != -1:
    b = int(input('Digite outro valor:\n'))
    c = input('Qual operacao deseja fazer(+, -, /, *):\n')

    if c == '+':
        print(f'Resultado: {a + b}\n')
    elif c == '-':
        print(f'Resultado: {a - b}\n')
    elif c == '/':
        print(f'Resultado: {a / b}\n')
    elif c == '*':
        print(f'Resultado: {a * b}\n')
    else:
        print('Operador invalido\n')
    a = int(input('Digite um valor:\n'))