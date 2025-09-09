x = int(input('Digite um numero:\n'))
y = int(input('Digite outro numero\n'))
z = int(input('Digite outro numero:\n'))

if (x >= (y + z)) or (y >= (x + z)) or (z >= (x + y)):
    print('Nao é possivel formar um triangulo\n')
elif x == y and x == z:
    print('Triangulo equilatero\n')
elif x != y and x != z and y != z:
    print('Triangulo escaleno\n')
else:
    print('Triangulo isoceles\n')