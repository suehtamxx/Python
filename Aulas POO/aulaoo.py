import datetime
class Pessoa():
	def __init__(self, nome, cpf):
		self._nome = nome
		self._cpf = cpf
	def imprimir_pessoa(self):
		print(f'{self.nome}, {self.cpf}, {self.idade}\n')
	@property
	def nome(self):
		return self._nome
	@nome.setter
	def nome(self, nome):
		self._nome = nome
	@property
	def cpf(self):
		return self._cpf
	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf
#pessoa1.imprimir_pessoa()
class Historico():
	def __init__(self):
		self._transacoes = []
	def add_transacao(self, t, deposito):
		self.transacoes.append((t, deposito))
	def imp_historico(self):
		for transacao in self.transacoes:
			print(transacao)
	@property
	def transacoes(self):
		return self._transacoes
	@transacoes.setter
	def transacoes(self, t):
		self._transacoes.append(t)
class Conta():
	total_contas = 0
	def __init__(self, numero, cliente, saldo=0):
		self._numero = numero
		self._titular = cliente.nome
		self._saldo = saldo
		Conta.total_contas+=1
		self.historico = Historico()
		self.historico.add_transacao(self.titular, f'Conta criada na data {datetime.datetime.now()}')
	@property
	def numero(self):
		return self._numero
	@numero.setter
	def numero(self, numero):
		if numero > 0:
			self._numero = numero
	@property
	def titular(self):
		return self._titular
	@titular.setter
	def titular(self, cliente):
		self._titular = cliente.nome
	@property
	def saldo(self):
		return self._saldo
	@saldo.setter
	def saldo(self, valor):
		self._saldo = valor
	def depositar(self, valor):
		self.saldo += valor
		self.historico.add_transacao(valor, f'Deposito realizado em {datetime.datetime.now()}')
	def sacar(self, valor):
		self.saldo -= valor
		self.historico.add_transacao(valor, f'Saque realizado em {datetime.datetime.now()}')
	def extrato(self):
		print(f'{self.titular}, {self.numero}, {self.saldo}\n')
	def transferir(self, destino, valor):
		self.saldo -= valor
		destino.saldo += valor
		self.historico.add_transacao(valor, f'Tranferencia realizada em {datetime.datetime.now()}')
	def imprimir_historico(self):
		self.historico.imp_historico()
	def imp_total_contas():
		print(Conta.total_contas)
contas = {}
clientes = {}
op = 0
while op != -1:
	op = int(input('1 - Criar conta\n2 - Depositar\n3 - Sacar\n4 - Extrato\n5 - Tranferir\n6 - Historico\n-1 - Sair\n'))
	if op == 1:
		nome = input('Digite o nome:\n')
		cpf = int(input('CPF:\n'))
		if cpf in clientes:
			print('Cliente ja cadastrado\n')
		else:
			cliente = Pessoa(nome, cpf)
			clientes[cpf] = cliente
			num_conta = int(input('numero da conta:\n'))
			if num_conta in contas:
				print('Conta ja cadastrada\n')
			else:
				contas[num_conta] = Conta(num_conta, cliente)
				print(f'Conta criada com sucesso para {cliente.nome}\n')
	elif op == 2:
		valor = float(input('Digite o valor para depositar:\n'))
		if valor <= 0:
			print('Valor inválido\n')
		search_num = int(input('Digite o numero da conta:\n'))
		if search_num in contas:
			contas[search_num].depositar(valor)
			contas[search_num].extrato()
		else:
			print('conta nao encontrada\n')
	elif op == 3:
		valor = float(input('Digite o valor para sacar:\n'))
		if valor <= 0:
			print('Valor inválido\n')
		search_num = int(input('Digite o numero da conta:\n'))
		if search_num in contas:
			if contas[search_num].saldo < valor:
				print('Saldo insuficiente\n')
			else: 
				contas[search_num].sacar(valor)
				contas[search_num].extrato()
		else:
			print('conta nao encontrada\n')
	elif op == 4:
		search_num = int(input('Digite o numero da conta:\n'))
		if search_num in contas:
			contas[search_num].extrato()
		else:
			print('conta nao encontrada\n')
	elif op == 5:
		valor = float(input('Qual o valor da tranferencia:\n'))
		search_num_trans = int(input('Digite o numero da conta que realizara a transferencia:\n'))
		if search_num_trans not in contas:
			print(f'Esta conta nao esta associada ao banco\n')
		else:
			search_num_rece = int(input('Digite o numero da conta que recebera a transferencia:\n'))
			if search_num_rece in contas:
				if contas[search_num].saldo < valor:
					print('Saldo insuficiente\n')
				else:
					contas[search_num_trans].transferir(contas[search_num_rece], valor)
					contas[search_num_rece].historico.add_transacao(valor, f'Tranferencia recebida em {datetime.datetime.now()}')
					contas[search_num_trans].extrato()
					contas[search_num_rece].extrato()
			else:
				print(f'Esta conta nao esta associada ao banco\n')
	elif op == 6:
		search_num = int(input('Digite o numero da conta que deseja ver o historico:\n'))
		if search_num in contas:
			contas[search_num].imprimir_historico()
	elif op == -1:
		print('Tchau...\n')

