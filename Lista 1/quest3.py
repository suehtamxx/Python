def recursiva(fat, resultado):
    if fat == 0 or fat == 1:
        return resultado
    elif fat != 0:
        return recursiva(fat-1, resultado*fat)

#Arranjo
'''
a = int(input('Digite um valor:\n'))
b = int(input('Digite outro valor:\n'))
c = 0
resultado = 1
c = recursiva(a, resultado)
d = recursiva(a-b, resultado)
print(f'O arranjo é: {c/d}')
'''
#Combinacao
a = int(input('Digite um valor:\n'))
b = int(input('Digite outro valor:\n'))
c = 0
resultado = 1
c = recursiva(a, resultado)
d = recursiva(b, resultado)
e = recursiva(a-b, resultado)
print(f'A combinacao é: {c/(d * e)}')