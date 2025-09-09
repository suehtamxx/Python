import random
lista = [0,0,0,0,0,0]
for i in range(100):
    a = random.randint(1,6)
    lista[a-1] += 1
print('Essa foi a quantidade de vezes que cada numero saiu')
print(f'1 = {lista[0]}\n2 = {lista[1]}\n3 = {lista[2]}\n4 = {lista[3]}\n5 = {lista[4]}\n6 = {lista[5]}')