lista = [4,2,7,8,10,4]

a = int(input('Digite um valor:\n'))
contador = 0
for i in range(len(lista)):
    if a == lista[i]:
        contador += 1
print(contador)