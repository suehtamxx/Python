import random
a = random.randint(0,100)
b = -1
contador = 0
op = -1
while a != b or op == 1 or contador > 10:
    b = int(input('Tente adivinhar o numero(intervalo de 0 a 100):\n'))
    contador += 1
    if a == b:
        print(f'Parabens, acertou em {contador} tentativas\n')
        op = int(input('Deseja continuar(1) ou sair(0):\n'))
        if op == 1:
            a = random.randint(0,100)
            contador = 0
    elif b < a:
        print(f'Errou, tente um valor maior (tentativa {contador})\n')
    else:
        print(f'Errou, tente um valor menor (tentativa {contador})\n')
