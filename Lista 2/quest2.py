palavra = 0
op = 0
while op != 2:
    print('1 - Digite uma palavra\n2 - Sair')
    op = int(input(''))
    if op == 1:
        palavra = input('Digite uma palavra:\n')
        if palavra == palavra[::-1]:
            print('Eh palindromo')
        else:
            print('Nao eh palindromo')
    elif op == 2:
        print('Tchau...')

        
