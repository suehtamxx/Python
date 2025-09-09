#primeira forma: iterativa
def fatorial(): 
    fat = int(input('Digite o numero fatorial:\n'))# preferi pedir o valor dentro da funcao
    resultado = 1 # necessario inicializar o resultado com 1. se fosse com 0 a multiplicacao seria zerada
    while fat != 0:
        resultado *= fat
        fat -= 1
    return resultado

#segunda forma: recursiva
def recursiva(fat, resultado):
    if fat == 0 or fat == 1: #caso base, pois o fatorial de 0 e 1 é 1
        return resultado
    elif fat != 0:
        return recursiva(fat-1, resultado*fat) #chamada recursiva decrementando o fat e calculando o fatorial

a = fatorial()
print(a)

fat = int(input('Digite o valor:\n')) #pra funcao recursiva preferi pedir o valor fora da funcao
resultado = 1
b = recursiva(fat, resultado)
print(b)