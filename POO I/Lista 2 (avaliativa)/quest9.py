agenda = []
for i in range(2):
    pessoa = []
    pessoa.append(input('Digite o nome:\n'))
    pessoa.append(input('Endereco:\n'))
    pessoa.append(int(input('Cep:\n')))
    pessoa.append(input('Bairro:\n'))
    pessoa.append(int(input('Telefone:\n')))
    agenda.append(pessoa)
agenda_invertida = agenda[::-1]

for i in agenda_invertida:
    print(i)

