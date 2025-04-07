'''
def metade(n):
    return n / 2
lista = [0,1,2,3,4,5]
lista_metade = map(metade,lista)
for i in lista_metade:
    print(i)
'''
def iszero(n):
    return type(n) == type(int)
lista = [0,1,2,3,4,5,0,3.5]
lista_zero = filter(iszero,lista)
print(list(lista_zero))
    