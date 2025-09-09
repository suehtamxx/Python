import random

inicial = int(input('Digite o valor inicial:\n'))
final = int(input('Digite o valor final:\n'))
qtd = int(input('Digite a quantidade de numeros aleatorios:\n'))
lista = []

for i in range(qtd):
    aleatorio = random.randint(inicial, final)
    if aleatorio in lista:
        while aleatorio in lista:
            aleatorio = random.randint(inicial, final)
        lista.append(aleatorio)
        print(aleatorio)
    else:
        lista.append(aleatorio)
        print(aleatorio)
        
