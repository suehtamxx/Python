def primo(a):
    contador = 0
    for i in range(2, a):
        if a % i == 0 and contador != 1:
            contador += 1
    if contador == 0:
        return True
    else:
        return False
  

inicio = int(input('Digite um numero:'))
final = int(input('Digite outro numero:'))
contador = 0
while inicio <= final:
    verificar = primo(inicio)
    if verificar == True:
        print(inicio)
        contador += 1
    inicio += 1
if contador == 0:
    print(f'Nao existe nenhum numero primo nesse intervalo.')