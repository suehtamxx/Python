lista1 = []
lista2 = []
lista3 = []
for i in range(10):
    lista1.append(int(input('Digite um numero para a lista 1:\n')))
    lista2.append(int(input('Digite um numero para a lista 2:\n')))
                           
for i in range(len(lista1)):
    lista3.append(lista1[i] * lista2[i])
print(lista3)
