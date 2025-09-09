def binario(a):
    if a >= 2: 
        binario(a // 2) #chama a recursao ate a >= 2. com essa recursao se cria uma pilha
    print(f'{a % 2}') #aqui ele imprime desempilhando

a = int(input('Digite um valor para ser transformado em binario:\n'))
binario(a)