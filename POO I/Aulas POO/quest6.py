fatorial = int(input('Digite o numero fatorial:\n'))
resultado = 1
while fatorial != 0:
    resultado *= fatorial
    fatorial -= 1
print(f'Resultado: {resultado}')