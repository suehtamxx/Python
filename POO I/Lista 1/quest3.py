def recursiva(fat, resultado): #por praticas em C, preferi usar o fatorial recursivo
    if fat == 0 or fat == 1:
        return resultado
    elif fat != 0:
        return recursiva(fat-1, resultado*fat)

# Arranjo
a = int(input('Digite um valor:\n'))
b = int(input('Digite outro valor:\n'))
c = 0
resultado = 1
c = recursiva(a, resultado) #chamo a funcao para o a(n)
d = recursiva(a-b, resultado) #e chamo a funcao para o fatorial de a-b
print(f'O arranjo é: {c/d}') #apos isso faço a divisao do resultado

#Combinacao
a = int(input('Digite um valor:\n'))
b = int(input('Digite outro valor:\n'))
c = 0
resultado = 1
c = recursiva(a, resultado) #chamada para calcular o fatorial de a
d = recursiva(b, resultado) #fatorial de b
e = recursiva(a-b, resultado) #fatorial de a-b
print(f'A combinacao é: {c/(d * e)}') #e a formula final