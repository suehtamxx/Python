import functools as ft
lista = [1,2,3,4,5,6,7,8]
par = []
a = []
par += filter(lambda x: x % 2 == 0 and x != 0, lista)
a = ft.reduce(lambda x,y: x + y, par)

print(a)