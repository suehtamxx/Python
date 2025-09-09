import random
resultado = []
aposta1 = []
aposta2 = []
aposta3 = []
i = 0
while len(resultado) != 13 or len(aposta1) != 14 or len(aposta2) != 14 or len(aposta3) != 14:
    if len(resultado) < 13:
        a = random.randint(0,60)
        if a not in resultado:
            resultado.append(a)

    if len(aposta1) < 14:
        a = random.randint(0,60)
        if a not in aposta1:
            aposta1.append(a)

    if len(aposta2) < 14:
        a = random.randint(0,60)
        if a not in aposta2:
            aposta2.append(a)

    if len(aposta3) < 14:
        a = random.randint(0,60)
        if a not in aposta3:
            aposta3.append(a)
aposta1.append(1)
aposta2.append(2)
aposta3.append(3)

cont1 = 0
cont2 = 0
cont3 = 0
for i in range(len(aposta1)-1):
    if aposta1[i] in resultado:
        cont1 += 1
        if cont1 == 13:
            print(f'O apostador {aposta1[14]} ganhou\n')
    if aposta2[i] in resultado:
        cont2 += 1
        if cont2 == 13:
            print(f'O apostador {aposta2[14]} ganhou\n')
    if aposta3[i] in resultado:
        cont3 += 1
        if cont3 == 13:
            print(f'O apostador {aposta3[14]} ganhou\n')

if cont1 != 13 and cont2 != 13 and cont3 != 13:
    if cont1 < 13:
        print(f'O apostador {aposta1[14]} acertou {cont1} numeros\n')
    if cont2 < 13:
        print(f'O apostador {aposta2[14]} acertou {cont2} numeros\n')
    if cont3 < 13:
        print(f'O apostador {aposta3[14]} acertou {cont3} numeros\n')
