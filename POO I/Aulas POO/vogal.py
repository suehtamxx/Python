vogais = ['a', 'e', 'i', 'o', 'u']
palavra = 'elder matheus maia de oliveira'
contador = 0
'''''
for i in palavra:
    if i in vogais:
        contador += 1
print(contador)
'''

for i in vogais:
    if i in palavra or i.upper in palavra:
        contador += palavra.count(i)
print(contador)