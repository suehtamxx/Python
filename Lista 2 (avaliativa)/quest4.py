
string = '7654321'

lista_string = list(string)

for i in range(len(lista_string)-1):
    for j in range(len(lista_string)-1-i):
        if lista_string[j] > lista_string[j+1]:
            lista_string[j], lista_string[j+1] = lista_string[j+1], lista_string[j]

nova_string = ''.join(lista_string)
print(nova_string)