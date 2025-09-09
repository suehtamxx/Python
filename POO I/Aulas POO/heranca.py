class Funcionario():
	def __init__(self, nome, matricula, salario):
		self._nome = nome
		self._matricula = matricula
		self._salario = salario
	@property
	def nome(self):
		return self._nome
	@property
	def matricula(self):
		return self._matricula
	@nome.setter
	def nome(self,nome):
		self._nome = nome
	@matricula.setter
	def matricula(self,matricula):
		self._matricula = matricula
	@property
	def salario(self):
		return self._salario
	@salario.setter
	def salario(self,salario):
		self._salario = salario
class Gerente(Funcionario):
	def __init__(self,nome,matricula,salario,senha):
		super().__init__(nome,matricula,salario)
		self._senha = senha
	@property
	def senha(self):
		return self._senha
	@senha.setter
	def senha(self, senha):
		self._senha = senha
	def getBonificacao(self):
		return (self.salario * 0.10) + 1000
	def imprimir(self):
		print(f'Nome: {self.nome}\n Matricula: {self.matricula}\n Senha: *****\n Salario: {self.salario}')

class Atendente(Funcionario):
	def getBonificacao(self):
		return self.salario * 0.15
	def imprimir(self):
		print(f'Nome: {self.nome}\n Matricula: {self.matricula}\n Salario: {self.salario}')					
class ControleBonificacao():
	def __init__(self):
		self._total_bonificacao = 0
		self.lista_bonificacoes = []
	@property
	def total_bonificacao(self):
		return self._total_bonificacao
	@total_bonificacao.setter
	def total_bonificacao(self,valor):
		self._total_bonificacao = valor
	def registrar(self,funcionario):
		self.total_bonificacao += funcionario.getBonificacao()
		self.lista_bonificacoes.append(funcionario.nome + ': ' + str(funcionario.getBonificacao()))

g = Gerente('ana',456, 2000,'1234')
a = Atendente('maria',101,1000,)

c = ControleBonificacao()
c.registrar(g)
c.registrar(a)

g.imprimir()
print(g.getBonificacao(),'\n')
a.imprimir()
print(a.getBonificacao(),'\n')

print(c.total_bonificacao)
print(c.lista_bonificacoes)