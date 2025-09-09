import functools as ft

def verifica_numero(x):
    if x % 5 == 0 or x % 7 == 0:
        return True
    return False

def soma_quadrados(x, y):
    return x + y**2

a = range(1, 21)
b = list(filter(verifica_numero, a))
c = ft.reduce(soma_quadrados, b)

print("b:", b)
print("c:", c)