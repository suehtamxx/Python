import datetime
class Pessoa():
	def __init__(self, nome, data_nasc, altura):
		self._nome = nome
		self._data_nasc = data_nasc
		self._altura = altura
		self.idade = self.idade()
	@property
	def nome(self):
		return self._nome
	@nome.setter
	def nome(self, entrada):
		if type(entrada) == type(str):
			self._nome = entrada
	@property
	def data_nasc(self):
		return self._data_nasc
	@data_nasc.setter
	def data_nasc(self, entrada):
		if type(entrada) == type(datetime.date):
			self._data_nasc = entrada
	@property
	def altura(self):
		return self._altura
	@altura.setter
	def altura(self, entrada):
		self._altura = entrada
	def imprimir_pessoa(self):
		print(f'Nome: {self._nome}, Data de nascimento: {self._data_nasc}, Altura: {self._altura}, Idade: {self.idade}\n')
	def idade(self):
		hoje = datetime.date.today()
		idade = hoje.year - self._data_nasc.year - ((hoje.month, hoje.day) < (self._data_nasc.month, self._data_nasc.day))
		return idade
pessoa1 = Pessoa('Joao', datetime.date(2000, 1, 1), 1.80)
pessoa1.imprimir_pessoa()
