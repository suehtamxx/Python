import functools as ft
par = []
impar = []
zero = []
lista = []
a = 0
while a != -1:
    a = int(input('Digite um numero:\n'))
    if a != -1:
        lista.append(a)

par += filter(lambda x: x % 2 == 0 and x != 0, lista)
impar += filter(lambda x: x % 2 != 0, lista)
zero += filter(lambda x: x == 0, lista)
 
par.sort()
impar.sort()

numeros = par + zero + impar

print(numeros)