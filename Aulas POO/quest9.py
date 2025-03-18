fibo = int(input('Digite a quantidade de numeros de fibonacci:\n'))
final = 0
antecessor = 0
sucessor = 1
ultimo = 0
while final < fibo:
    print(f'{ultimo}', end=" ")
    ultimo = antecessor + sucessor
    antecessor = sucessor
    sucessor = ultimo
    final += 1
    