string = input('Digite uma string:\n')
search = input('Digite o que deseja procurar:\n')
index = 0
for i in string:
    if i == search:
        print(f'o caractere {search} foi encontrado na string na posicao {index}')
    index += 1
    