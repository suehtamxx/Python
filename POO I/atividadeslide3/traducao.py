dicionario = {
    'bug': 'inseto',
    'dog': 'cachorro',
    'cat': 'gato',
    'one': 'um'
}

search = input('Digite a palavra em ingles:\n')
if search in dicionario:
    print(dicionario[search])
else:
    print('Palavra nao encontrada\n')