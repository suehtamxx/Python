lista = []
item = 0
while item != 'fim':
    item = input('Digite um item:\n')
    if item != 'fim':
        lista.append(item)
lista.sort()
for i in lista:
    print(i)
