pessoas = {
}
for i in range(2):
    cpf = input('Digite o cpf:\n')
    pessoas[cpf] = []
    nome = input('Digite o nome:\n')
    idade = int(input('Digite a idade:\n'))
    pessoas[cpf] = {'nome': nome, 'idade': idade}
print(pessoas)

maior_idade = [x for i, x in pessoas.items() if pessoas[i]['idade'] >= 18 ]

print(maior_idade)