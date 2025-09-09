fatorial = int(input('Digite um numero:\n'))
while fatorial >= 0:
    while fatorial > 16:
        fatorial = int(input('Digite outro numero:'))
    resultado = 1
    while fatorial != 0:
        resultado *= fatorial
        fatorial -= 1
    print(f'Resultado: {resultado}')
    fatorial = int(input('Digite outro numero:\n'))