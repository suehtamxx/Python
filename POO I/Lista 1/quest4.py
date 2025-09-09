def primo(a):
    contador = 0
    for i in range(2, a): # percorro de 2 ate a-1
        if a % i == 0 and contador != 1: #verifico se a é divisivel pelo i e se o contador é diferente de 1(minha condicao de parada
            #se achar um divisor de 2 ate a-1, entao nao é primo. nao preciso verificar o resto)
            contador += 1
    if contador == 0:
        return True
    else:
        return False
  

inicio = int(input('Digite um numero:'))
final = int(input('Digite outro numero:'))
contador = 0
while inicio <= final:
    verificar = primo(inicio) #chamo a funcao passando o inicio
    if verificar == True:
        print(inicio)
        contador += 1
    inicio += 1 #e vou incrementando a cada loop
if contador == 0: #se nao entrar no if o contador permanece 0, ou seja, nenhum primo
    print(f'Nao existe nenhum numero primo nesse intervalo.')