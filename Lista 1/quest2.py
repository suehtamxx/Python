#primeira forma: iterativa
def fatorial():
    fat = int(input('Digite o numero fatorial:\n'))
    resultado = 1
    while fat != 0:
        resultado *= fat
        fat -= 1
    return resultado

#segunda forma: recursiva
def recursiva(fat, resultado):
    if fat == 0 or fat == 1:
        return resultado
    elif fat != 0:
        return recursiva(fat-1, resultado*fat)

a = fatorial()
print(a)

fat = int(input('Digite o valor:\n'))
resultado = 1
b = recursiva(fat, resultado)
print(b)