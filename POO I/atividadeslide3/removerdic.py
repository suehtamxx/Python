alunos = {
    'joao': [8.0, 9.0, 10.0],
    'maria': [7.0, 8.0, 9.0],
    'pedro': [6.0, 7.0, 8.0],
    'ana': [5.0, 6.0, 7.0]
}

nome = input('Digite o nome do aluno para remover:\n')
if nome in alunos:
    del alunos[nome]
    print('Aluno removido com sucesso!\n')
    print(alunos)
else:
    print('Aluno nao encontrado!\n')