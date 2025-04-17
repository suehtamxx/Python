produtos = {}
op = 0
def adicionar_produtos(produtos):
    nome = input('Digite o nome do produto:\n')
    if nome not in produtos:
        produtos[nome] = []
        preco = float(input('Digite o preco do produto:\n'))
        categoria = input('Digite a categoria:\n')
        produtos[nome] = [nome, preco, categoria]
    else:
        print('Produto ja existe\n')
def listar_produtos(produtos):
    if len(produtos) > 0:
        for i in produtos:
            print(i, produtos[i])
    else:
        print('Sem produtos\n')
def buscar_produtos(produtos, search):
    if search in produtos:
        print(produtos[search])
    else:
        print('Produto nao encontrado\n')
def excluir_produto(produtos, excluir):
    if excluir in produtos:
        del produtos[excluir]
    else:
        print('Produto nao encontrado\n')
while op != 5:
    op = int(input('1 - Adicionar produtos\n2 - Listar todos os produtos cadastrados\n3 - Buscar um produto pelo nome\n4 - Remover um produto pelo nome\n5 - Sair\n'))
    if op == 1:
        adicionar_produtos(produtos)
    elif op == 2:
        listar_produtos(produtos)
    elif op == 3:
        search = input('Digite o nome do produto para buscar:\n')
        buscar_produtos(produtos, search)
    elif op == 4:
        excluir = input('Digite o nome do produto para excluir:\n')
        excluir_produto(produtos, excluir)
    elif op == 5:
        print('Tchau...\n')
    else:
        print('Digite um valor valido\n')