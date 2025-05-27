class Elevador():
	def __init__(self, total_andares,capacidade, atual=0, pessoas_presentes = 0):
		self._atual = atual
		self._capacidade = capacidade
		self._total_andares = total_andares
		self._pessoas_presentes = pessoas_presentes
	@property
	def atual(self):
		return self._atual

	@property
	def capacidade(self):
		return self._capacidade

	@property
	def total_andares(self):
		return self._total_andares

	@property
	def pessoas_presentes(self):
		return self._pessoas_presentes
  
	@atual.setter
	def atual(self, valor):
		if valor < self._total_andares:
			self._atual = valor
		else:
			print('Elevador ja esta no ultimo andar')
	@capacidade.setter
	def capacidade(self, total):
		if total <= 0:
			print('Valor invalido\n')
		else:
			self._capacidade = total
	@total_andares.setter
	def total_andares(self, andares):
		if andares <= 0:
			print('Valor invalido\n')
		else:
			self._total_andares = andares
	
	def inicializa(self):
		andares = int(input('Digite o total de andares:\n'))
		capacidade = int(input('Digite a capacidade do elevador:\n'))
		self._total_andares = andares
		self._capacidade = capacidade
	
	def entra(self):
		if self._pessoas_presentes < self._capacidade:
			self._pessoas_presentes +=1
		else:
			print('Elevador cheio\n')
	def sai(self):
		if self._pessoas_presentes > 0:
			self._pessoas_presentes -= 1
		else:
			print('Elevador vazio\n')
	def sobe(self):
		if self._atual < self._total_andares:
			self._atual += 1
		else:
			print('Elevador ja esta no ultimo andar\n')
	def desce(self):
		if self._atual > 0:
			self._atual -= 1
		else:
			print('Elevador ja esta no terreo\n')
	def imprimir(self):
		print(f'Andar atual: {self._atual}')
		print(f'Pessoas presentes: {self._pessoas_presentes}')
elevador = Elevador(0,0)
op = 0
while op != -1:
	op = int(input('1 - Inicializar\n2 - Entrar\n3 - Sair\n4 - Sobe\n5 - Desce\n-1 - Sair\n'))
	if op == 1:
		elevador.inicializa()
	elif op == 2:
		elevador.entra()
		elevador.imprimir()
	elif op == 3:
		elevador.sai()
		elevador.imprimir()
	elif op == 4:
		elevador.sobe()
		elevador.imprimir()
	elif op == 5:
		elevador.desce()
		elevador.imprimir()
	elif op == -1:
		print('Tchau...\n')
	else:
		print('Digite um valor valido\n')
