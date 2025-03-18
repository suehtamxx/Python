x = int(input('Digite um numero para a tabuada:\n'))
inicio = int(input('deseja começar a partir de qual numero:\n'))
fim = int(input('Final da tabuada:\n'))
while inicio <= fim:
    print(f'{x} x {inicio} = {x * inicio}')
    inicio += 1