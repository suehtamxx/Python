def ispar(n):
    return n % 2 == 0 and n != 0
def isimpar(n):
    return n % 2 == 1
def iszero(n):
    return n == 0

lista = []
a = 0
while a != -1:
    a = int(input('Digite um numero:\n'))
    if a != -1:
        lista.append(a)
lista.sort()

par = filter(ispar,lista)
impar = filter(isimpar,lista)
zero = filter(iszero,lista)

numeros = list(par) + list(zero) + list(impar) 

print(numeros)