forma = 0
while forma != 4:
    forma = int(input('1 - Triangulo\n2 - Quadrado\n3 - Circulo\n4 - Sair\n'))
    if forma == 1:
        a = float(input('Digite a base do triangulo:'))
        b = float(input('Digite a altura do triangulo:'))
        area = (a*b)/2
        print(f'Area do triangulo: {area}')
    elif forma == 2:
        a = float(input('Digite o lado do quadrado:'))
        area = a*a
        print(f'Area do quadrado: {area}')
    elif forma == 3:
        a = float(input('Digite o raio do circulo:'))
        area = (a*a) * 3.14
        print(f'Area do circulo: {area}')
    elif forma == 4:
        print('Tchau...')
    else:
        print('Valor invalido.')