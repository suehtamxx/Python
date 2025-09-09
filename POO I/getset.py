class Conta():
	def __init__(self, numero, titular, saldo=0):
		self._numero = numero
		self._titular = titular
		self._saldo = saldo
	@property
	def saldo(self):
		print(f'{self._saldo}')

	@saldo.setter
	def saldo(self, valor):
		self._saldo = valor
c1 = Conta(1, 'elder')
c1.saldo = 100
print(c1.saldo)