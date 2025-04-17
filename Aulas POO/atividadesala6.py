op = 0
compras_cliente_1 = ['celular', 'tablet', 'notebook', 'smartwatch', 'fone de ouvido']
compras_cliente_2 = ['notebook', 'smartphone', 'tv', 'tablet', 'smartwatch']
compras_cliente_3 = ['celular', 'tablet', 'smartphone', 'smartwatch', 'fone de ouvido', 'notebook']

while op != -1:
    op = int(input('1 - Produtos comprados por pelo menos um cliente\n2 - Digite um produto para verificar se pelo menos um cliente comprou\n3 - Verificar se algum cliente comprou uma combinacao de produtos\n'))
    if op == 1:
        print(compras_cliente_1)
        print(compras_cliente_2)
        print(compras_cliente_3)
    elif op == 2:
        produto = input('Digite o nome do produto:\n')
        if produto in compras_cliente_1:
            print('Cliente 1 comprou esse produto')
        elif produto in compras_cliente_2:
            print('Cliente 2 comprou esse produto')
        elif produto in compras_cliente_3:
            print('Cliente 3 comprou esse produto')
        else:
            print('Ninguem comprou esse produto')
    elif op == 3:
        produto_1 = input('Digite um produto:\n')
        produto_2 = input('Digite outro produto:\n')
        if produto_1 in compras_cliente_1 and produto_2 in compras_cliente_1:
            print('Cliente 1 tem essa combinacao de produtos\n')
        elif produto_1 in compras_cliente_2 and produto_2 in compras_cliente_2:
            print('Cliente 2 tem essa combinacao de produtos\n')
        elif produto_1 in compras_cliente_3 and produto_2 in compras_cliente_3:
            print('Cliente 3 tem essa combinacao de produtos\n')
    elif op == -1:
        print('Tchau...')