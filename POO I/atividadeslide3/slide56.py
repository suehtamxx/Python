lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
maior = 0
menor = 100
num = lista[0]
ocorrencia = 0
soma = 0
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    if lista[i] % 2 == 0:
        print(f'{lista[i]} é par')
    if num == lista[i]:
        ocorrencia += 1
    if lista[i] < 0:
        soma += lista[i]
print(f'{maior} é o maior\n')
print(f'{menor} é o menor')
print(f'{num} ocorre {ocorrencia} vezes')
print(f'{soma} é a soma dos numeros negativos')
media = sum(lista)/len(lista)
print(f'{media:.2f} é a media')

