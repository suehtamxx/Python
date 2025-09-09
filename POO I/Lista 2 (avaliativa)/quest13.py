telefones = {
}
op = 0
def adicionar_nome(telefones, nome):
    n = int(input('Quantos numeros deseja adicionar(1 é obrigatorio):\n'))
    while n < 1:
        n = int(input('Deve ter pelo menos um numero:\n'))
    telefones[nome] = []
    for i in range(n):
        telefone = int(input('Digite o telefone:\n'))
        telefones[nome].append(telefone)
def adicionar_telefone(telefones):
    nome = input('Digite o nome:\n')
    if nome in telefones:
        telefone = int(input('Digite o telefone:\n'))
        telefones[nome].append(telefone)
    else:
        a = int(input("Esse nome nao existe na agenda, deseja adicionar?\n1 - Sim\n2 - Nao\n"))
        if a == 1:
            adicionar_nome(telefones, nome)
        elif a == 2:
             print('Voltando ao menu...\n')
def excluir_telefone(telefones, numero):
    for nome, lista_numeros in telefones.items():
        if numero in lista_numeros:
            lista_numeros.remove(numero)
            if len(lista_numeros) == 0:
                del telefones[nome]
            print('Numero excluido com sucesso!\n')
            return
    print('Numero nao encontrado\n')
def excluir_nome(telefones, nome):
    if nome in telefones:
        del telefones[nome]
    else:
        print('Nome nao encontrado:\n')
while op != -1:
    op = int(input('1 - Adicionar nome na agenda\n2 - Adicionar telefone\n3 - Excluir telefone\n4 - Excluir nome\n5 - Consultar telefone\n-1 - Sair\n'))
    if op == 1:
        nome = input('Digite o nome:\n')
        if nome in telefones:
            print('Esse nome ja existe na agenda\n')
        else:
            adicionar_nome(telefones, nome)
        print(telefones)
    elif op == 2:
        adicionar_telefone(telefones)
        print(telefones)
    elif op == 3:
        numero = int(input('Digite o telefone:\n'))
        excluir_telefone(telefones, numero)
        print(telefones)
    elif op == 4:
        nome = input('Digite o nome para excluir:\n')
        excluir_nome(telefones, nome)
        print(telefones)
    elif op == 5:
        if telefones == {}:
            print('Agenda vazia\n')
        else:
            nome = input('Digite o nome para consultar:\n')
            if nome in telefones:
                print(telefones[nome])
            else:
                print('Esse nome nao existe na agenda\n')
    elif op == -1:
        print('Tchau...')
