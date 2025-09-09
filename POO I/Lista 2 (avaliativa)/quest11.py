alunos = {}
for i in range(2):
    nome = input('Digite o nome do aluno:\n')
    nota1 = float(input('Digite a nota do aluno:\n'))
    nota2 = float(input('Digite a nota do aluno:\n'))
    alunos[nome] = {'nota1': nota1, 'nota2': nota2}
for i in alunos:
    print(i, alunos[i])
search = input('Digite o nome do aluno:\n')
if search in alunos:
    print(f'a media do(a) {search} é: {(alunos[search]["nota1"] + alunos[search]["nota2"])/2}')