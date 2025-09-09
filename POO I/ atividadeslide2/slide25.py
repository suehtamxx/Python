import functools as ft
lista = []
a = 0
while a != -1:
    a = int(input('Digite um numero:\n'))
    if a != -1:
        lista.append(a)
lista.sort()
par = filter(lambda x: x % 2 == 0 and x != 0, lista)
impar = filter(lambda x: x % 2 != 0, lista)
zero = filter(lambda x: x == 0, lista)
 
numeros = list(par) + list(zero) + list(impar)

print(numeros)