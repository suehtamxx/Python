'''
def ispar(n):
    return n % 2 == 0
def dobro(a):
    return a * 2
'''

lista = [1,2,3,4,5,6,7,8,9,10]
par = filter(lambda x: x % 2 == 0 and x != 0, lista)
a = map(lambda x: x * 2, par)
print(list(a))