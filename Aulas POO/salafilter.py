def ispar(n):
    return n % 2 == 0
def dobro(a):
    return a * 2

lista = [1,2,3,4,5,6,7,8,9,10]
par = filter(ispar,lista)
a = map(dobro,par)
print(list(a))