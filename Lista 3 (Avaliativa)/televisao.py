class Televisao():
	def __init__ (self, canal, volume):
		self.canal = canal
		self.volume = volume
class ControleRemoto():
	def __init__(self, televisao):
		self.televisao = televisao
	def aumentar_volume(self):
		self.televisao.volume += 1
	def diminuir_volume(self):
		self.televisao.volume -= 1
	def trocar_canal(self,canal):
		if canal > 0 and canal < 100:
			self.televisao.canal = canal
		else:
			print('Canal invalido')
	def up_canal(self):
		if self.televisao.canal == 100:
			self.televisao.canal = 1
		else:
			self.televisao.canal += 1
	def down_canal(self):
		if self.televisao.canal == 1:
			self.televisao.canal = 100
		else:
			self.televisao.canal -= 1
	def imprimir(self):
		print(f'Canal: {self.televisao.canal}')
		print(f'Volume: {self.televisao.volume}')
op = 0
controle = ControleRemoto(Televisao(1,1))
while op != -1:
	op = int(input('1 - Trocar canal\n2 - Aumentar volume\n3 - Diminuir volume\n4 - Aumentar canal\n5 - Diminuir canal\n-1 - Sair\n'))
	if op == 1:
		canal = int(input('Digite o canal:\n'))
		controle.trocar_canal(canal)
		controle.imprimir()
	elif op == 2:
		controle.aumentar_volume()
		controle.imprimir()
	elif op == 3:
		controle.diminuir_volume()
		controle.imprimir()
	elif op == 4:
		controle.up_canal()
		controle.imprimir()
	elif op == 5:
		controle.down_canal()
		controle.imprimir()
	elif op == -1:
		print('Tchau...\n')
	else:
		print('Digite um valor valido\n')
		