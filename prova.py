import functools as ft
import math as mt
'''

def raiz(n):
	k = 1
	while abs(k - mt.sqrt(n)) >= 0.01:
		k = (k+n/k)/2
	return k

resultado = raiz(25)
print(resultado)
a = range(12)
b = list(filter(lambda x: x % 4 == 0 or x % 5 == 0, a))
c = ft.reduce(lambda x,y: x+y, b)
print(b, c)
'''
tempos = {'joao': [8,9,7],
					'maria':[5,6,8],
					'carlos':[1,2,3],
					'elder':[8,8,8]}
def menor_tempo_media(tempos):
	soma = 1000
	nome_campeao = ''
	media_tempo = []
	for i in tempos:
		if sum(tempos[i]) < soma:
			soma = sum(tempos[i])
			nome_campeao = i
		media_tempo.append((sum(tempos[i]))/3)
	return nome_campeao, media_tempo
nome, media = menor_tempo_media(tempos)
print(nome, media)