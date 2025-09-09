lista = []
i = 0
while i != -1:
    i = int(input('Digite um valor:\n'))
    if i != -1:
        lista.append(i)
listap = []
lista.sort()
for i in lista:
    if i % 2 == 0 and i != 0:
        lista.remove(i)
        listap.append(i)
lista = listap + lista
for i in lista:
    print(i, end='')