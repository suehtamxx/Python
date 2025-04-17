def print_lista(lista):
    for i in lista:
        if type(i) == list:
            print_lista(i)
        else:
            print(i)
lista = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
print_lista(lista)