import datetime
import random
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
	contas = {}
	def __init__(self, numero, titular, tipo, saldo=0):
		self._numero = numero
		self._titular = titular
		self._saldo = saldo
		self.tipo = tipo

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
	@classmethod
	def imp_contas(cls):
			for i in cls.contas:
				cls.contas[i].extrato()
	def __str__(self):
		return f"Dados da conta \nNumero: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}\nTipo: {self.tipo}\n"
class ContaPoupanca(Conta):
	def __init__(self,numero,titular,saldo=0):
		super().__init__(numero,titular,saldo)
	def atualiza(self,taxa):
		self._saldo += self._saldo * ((taxa/100) *3)
		return self._saldo

class ContaCorrente(Conta):
	def __init__(self,numero,titular,saldo=0):
		super().__init__(numero,titular,saldo)
	def atualiza(self,taxa):
		self._saldo += self._saldo * ((taxa/100) * 2)
		return self._saldo
	def depositar(self, valor):
		self.saldo += (valor - 0.10)
		self.historico.add_transacao(valor, f'Deposito realizado em {datetime.datetime.now()}')
		self.historico.add_transacao(0.10, f'Taxa de imposto na data de{datetime.datetime.now()}')

class AtualizadorDeConta():
	def __init__(self,selic,saldo_total=0):
		self._selic = selic
		self._saldo_total = saldo_total
	@property
	def selic(self):
		return self._selic
	@selic.setter
	def selic(self, selic):
		self._selic = selic
	@property
	def saldo_total(self):
		return self._saldo_total
	@saldo_total.setter
	def saldo_total(self, saldo_total):
		self._saldo_total = saldo_total
	def roda(self, conta):
		print(f'Saldo da conta: {conta.saldo}')
		self._saldo_total += conta.atualiza(self._selic)
		print(f'Saldo final: {self._saldo_total}')
op = 0

while op != -1:
	op = int(input('1 - Criar conta\n2 - Depositar\n3 - Sacar\n4 - Extrato\n5 - Tranferir\n6 - Historico\n7 - Listar todas as contas\n8 - Excluir conta\n9 - Atualizar conta\n-1 - Sair\n'))
	if op == 1:
		opi = int(input('1 - Conta Poupanca\n2 - Conta Corrente\n'))
		if opi == 1:
			nome = input('Digite o nome:\n')
			num_conta = random.randint(100,999)
			if num_conta in Conta.contas or num_conta % 2 != 0:
				while num_conta in Conta.contas or num_conta % 2 != 0:
					num_conta = random.randint(100,999)
			Conta.contas[num_conta] = ContaPoupanca(num_conta, nome, 'poupanca')
			print(f'Conta poupanca criada com sucesso para {nome}\n')
			Conta.contas[num_conta].extrato()

		elif opi == 2:
			nome = input('Digite o nome:\n')
			num_conta = random.randint(100,999)
			if num_conta in Conta.contas or num_conta % 2 == 0:
				while num_conta in Conta.contas or num_conta % 2 == 0:
					num_conta = random.randint(100,999)
			Conta.contas[num_conta] = ContaCorrente(num_conta, nome, 'corrente')
			print(f'Conta corrente criada com sucesso para {nome}\n')
			Conta.contas[num_conta].extrato()
		
	elif op == 2:
		Conta.imp_contas()
		search_num = int(input('Digite o numero da conta:\n'))
		if search_num in Conta.contas:
			valor = float(input('Digite o valor para depositar:\n'))
			if valor <= 0:
				print('Valor inválido\n')
			else:
				if search_num % 2 != 0:
					ContaCorrente.contas[search_num].depositar(valor)
					Conta.contas[search_num].extrato()
				else:
					Conta.contas[search_num].depositar(valor)
					Conta.contas[search_num].extrato()
		else:
			print('conta nao encontrada\n')
	elif op == 3:
		Conta.imp_contas()
		search_num = int(input('Digite o numero da conta:\n'))
		if search_num in Conta.contas:
				valor = float(input('Digite o valor para sacar:\n'))
				if valor <= 0:
					print('Valor inválido\n')
				if Conta.contas[search_num].saldo < valor:
						print('Saldo insuficiente\n')
				else:
						Conta.contas[search_num].sacar(valor)
						Conta.contas[search_num].extrato()
		else:
			print('conta nao encontrada\n')
	elif op == 4:
		search_num = int(input('Digite o numero da conta:\n'))
		if search_num in Conta.contas:
			search_num = Conta.contas[search_num]
			print(search_num)
		else:
			print('conta nao encontrada\n')
	elif op == 5:
		Conta.imp_contas()
		origem = int(input('Digite o numero da conta de origem:\n'))
		if origem not in Conta.contas:
			print(f'Esta conta nao esta associada ao banco\n')
		else:
			destino = int(input('Digite o numero da conta de destino:\n'))
			if destino in Conta.contas:
				valor = float(input('Qual o valor da tranferencia:\n'))
				if Conta.contas[origem].saldo < valor:
					print('Saldo insuficiente na conta de origem\n')
				else:
					Conta.contas[origem].transferir(Conta.contas[destino], valor)
					Conta.contas[destino].historico.add_transacao(valor, f'Tranferencia recebida em {datetime.datetime.now()}')
					Conta.contas[origem].extrato()
					Conta.contas[destino].extrato()
			else:
				print(f'Esta conta nao esta associada ao banco\n')
	elif op == 6:
		search_num = int(input('Digite o numero da conta que deseja ver o historico:\n'))
		if search_num in Conta.contas:
			Conta.contas[search_num].imprimir_historico()
		else:
			print('Conta nao encontrada\n')
	elif op == 7:
		Conta.imp_contas()
	elif op == 8:
		Conta.imp_contas()
		search = int(input('Digite o numero da conta que deseja excluir:\n'))
		if search in Conta.contas:
			del Conta.contas[search]
		else:
			print('conta nao encontrada\n')
	elif op == 9:
		Conta.imp_contas()
		search = int(input('Digite o numero da conta que deseja atualizar:\n'))
		if search in Conta.contas:
			taxa = float(input('Digite a taxa de atualizacao:\n'))
			adc = AtualizadorDeConta(taxa)
			if search % 2 != 0:
				adc.roda(ContaCorrente.contas[search])
			else:
				adc.roda(ContaPoupanca.contas[search])
		print(adc.saldo_total)
	elif op == -1:
		print('Tchau...\n')