import random
lista = []
menor = 100
maior = 0
for i in range(10):
    lista.append(random.randint(0,100))
    if lista[i] < menor:
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
print(menor)
print(maior)
