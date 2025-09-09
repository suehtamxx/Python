import functools as ft
def ispar(n):
    return n % 2 == 0
def soma(a,b):
    return a + b
def dobro(n):
    return n * 2
lista = [1,2,3,4,5,6]
a = ft.reduce(soma,map(dobro,filter(ispar,lista)))
'''
par = filter(ispar,lista)
dobro = map(dobro,par)
a = ft.reduce(soma,dobro)'
'''
print(a)
