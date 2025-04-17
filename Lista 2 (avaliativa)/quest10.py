import random
lista = []
variancia = 0
for i in range(100):
    lista.append(random.randint(1,100))
media = sum(lista)/len(lista)
print(media)
tam = len(lista)
if tam % 2 == 0:
    print(f'A mediana é {(lista[tam//2-1])} e {lista[tam//2]}')
else:
    print(f'A mediana é {lista[tam//2]}')
for i in range(len(lista)):
    variancia += ((lista[i] - media)**2)
variancia /= (tam-1)
print(f'Variancia:{variancia:.2f}')
raiz = variancia**0.5
print(f'Desvio padrao:{raiz:.2f}')