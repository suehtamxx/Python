lista = [1,2,3,4,5,6,7,8,9]
tam = len(lista)
tam -= 1
i = 0
print(lista)
while tam != i: 
    lista[i], lista[tam] = lista[tam], lista[i]
    tam -= 1
    i += 1
print(lista)