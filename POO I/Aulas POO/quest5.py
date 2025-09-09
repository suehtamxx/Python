base = int(input('Digite o numero base:\n'))
expoente = int(input('Digite o numero expoente:\n'))
resultado = 1
if expoente == 0:
    print('Resultado: 1\n')
elif expoente != 0:
    while expoente != 0:
        resultado *= base
        expoente -= 1
    print(f'Resultado: {resultado}')