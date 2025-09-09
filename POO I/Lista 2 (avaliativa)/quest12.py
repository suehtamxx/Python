corredores = {}
menor_tempo = 100
volta = 0
campeao = ''
media = 100
for i in range(3):
    nome = input('Digite o nome do corredor:\n')
    volta1 = float(input('Digite o tempo da primeira volta:\n'))
    volta2 = float(input('Digite o tempo da segunda volta:\n'))
    volta3 = float(input('Digite o tempo da terceira volta:\n'))
    corredores[nome] = {'volta1': volta1, 'volta2': volta2, 'volta3': volta3}
for i in corredores:
    if corredores[i]['volta1'] <= corredores[i]['volta2'] and corredores[i]['volta1'] <= corredores[i]['volta3'] and corredores[i]['volta1'] < menor_tempo:
        menor_tempo = corredores[i]['volta1']
        volta = 1
        corredor = i
    elif corredores[i]['volta2'] <= corredores[i]['volta1'] and corredores[i]['volta2'] <= corredores[i]['volta3'] and corredores[i]['volta2'] < menor_tempo:
        menor_tempo = corredores[i]['volta2']
        volta = 2
        corredor = i
    elif corredores[i]['volta3'] <= corredores[i]['volta1'] and corredores[i]['volta3'] <= corredores[i]['volta2'] and corredores[i]['volta3'] < menor_tempo:
        menor_tempo = corredores[i]['volta3']
        volta = 3
        corredor = i
if menor_tempo == 1:
    print(f'Corredor {corredor} completou a volta {volta} com tempo de {menor_tempo} segundo')
else:
    print(f'Corredor {corredor} completou a volta {volta} com tempo de {menor_tempo} segundos')
for i in corredores:
    if media > (corredores[i]['volta1'] + corredores[i]['volta2'] + corredores[i]['volta3'])/3:
        media = (corredores[i]['volta1'] + corredores[i]['volta2'] + corredores[i]['volta3'])/3
        campeao = i
for i in corredores:
    print(i, corredores[i])
print(f'Campeao foi o corredor {campeao} com media de {media:.2f} segundos')