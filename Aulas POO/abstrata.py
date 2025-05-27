import abc
class Funcionario(abc.ABC):
	def __init__(self,nome,salario):
		self.nome = nome
		self._salario = salario
	@abc.abstractmethod
	def get_bonificacao(self):
		pass
	def __str__(self):
		return f'Nome: {self.nome}\nSalario: {self._salario}\n'
	@property
	def salario(self):
		return self._salario
	@salario.setter
	def salario(self,salario):
		self._salario = salario
class Gerente(Funcionario):
	def get_bonificacao(self):
		bonificacao = self._salario * 0.10
		self.salario += bonificacao
		return bonificacao
class Secretario(Funcionario):
	def get_bonificacao(self):
		bonificacao = self._salario * 0.15
		self.salario += bonificacao
		return bonificacao

g = Gerente('maria',5000)
print('Bonificacao:',g.get_bonificacao())
print(g)
s = Secretario('pedro',5000)
print('Bonificacao:',s.get_bonificacao())
print(s)