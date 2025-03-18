import random
a = random.randint(0,100)
b = -1
contador = 0
while a != b:
    b = int(input('Tente adivinhar o numero(intervalo de 0 a 100):\n'))
    contador += 1
    if a == b:
        print(f'Parabens, acertou em {contador} tentativas\n')
    elif b < a:
        print('Errou, tente um valor maior\n')
    else:
        print('Errou, tente um valor menor\n')
