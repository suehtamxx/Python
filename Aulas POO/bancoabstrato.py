import abc

class Autenticavel(abc.ABC):
	@abc.abstractmethod
	def autentica(self,senha):
		pass
class Tributavel(abc.ABC):
	"""Classe que contem operacoes de um objeto autenticavel

	As subclasses concretas devem sobrescrever os metodos abstratos
	"""
	@abc.abstractmethod
	def get_valor_imposto(self,valor):
		"""aplica taxa de imposto sobre um determinado valor do objeto"""
		pass
class SeguroDeVida():
	def __init__(self,valor,titular,numero_apolice):
		self._valor = valor
		self._titular = titular
		self._numero_apolice = numero_apolice
	@property
	def titular(self):
		return self._titular
	@property
	def numero_apolice(self):
		return self._numero_apolice
	@property
	def valor(self):
		return self._valor
	@valor.setter
	def valor(self,valor):
		self._valor = valor
	@titular.setter
	def titular(self,nome):	
		self._titular = nome
	@numero_apolice.setter
	def numero_apolice(self,numero):
		self._numero_apolice = numero
	def get_valor_imposto(self):
		return 50 + self._valor * 0.05
	
class ManipuladorDeTriubutaveis:
	def calcula_impostos(self,lista_tributos):
			total = 0
			for t in lista_tributos:
				if isinstance(t, Tributavel):
					total += t.get_valor_imposto()
				else:
					print(t.__repr__(), 'nao eh tributavel')
			return total

class Conta(abc.ABC):
	def __init__(self,numero,titular,tipo,saldo=0,limite=1000):
		self._numero = numero
		self._titular = titular
		self._saldo = saldo
		self._limite = limite
		self.tipo = tipo
	@property
	def titular(self):
		return self._titular

	@titular.setter
	def titular(self,nome):
		self._titular = nome

	@property
	def saldo(self):
		return self._saldo

	@saldo.setter
	def saldo(self,valor):
		self._saldo = valor

	@property
	def limite(self):
		return self._limite

	@limite.setter
	def limite(self,valor):
		self._limite = valor

	@abc.abstractmethod
	def atualiza():
		pass
	def __str__(self):
		return f"Dados da conta \nNumero: {self._numero}\nTitular: {self._titular}\nSaldo: {self._saldo}\nTipo: {self.tipo}\n"
class ContaCorrente(Conta):
	def atualiza(self,taxa):
		self._saldo += self._saldo * ((taxa/100) * 2)
		return self._saldo
	def autentica(self,senha):
		return True
	def get_valor_imposto(self):
		return self._saldo * 0.01
class ContaPoupanca(Conta):
	def atualiza(self,taxa):
		self._saldo += self._saldo * ((taxa/100) *3)
		return self._saldo
	def autentica(self,senha):
		return True
class ContaInvestimento(Conta):
	def atualiza(self,taxa):
		self._saldo +=self._saldo * ((taxa/100) * 5)
		return self._saldo
	def autentica(self,senha):
		return True
	def get_valor_imposto(self):
		return self._saldo * 0.03
	
class SistemaInterno:
	def login(self,obj):
		if isinstance(obj,Autenticavel):
			if obj.autentica('123'):
				print('logado')
			else:
				print('nao logado')
		else:
			print('objeto nao autenticavel')

cp = ContaPoupanca('123','joao','Poupanca',1000,)
cc = ContaCorrente('222','maria','Corrente',2000)
ci = ContaInvestimento('333','pedro','Investimento',3000)
s = SeguroDeVida(100,'jose','345-77')

Tributavel.register(SeguroDeVida)
Tributavel.register(ContaCorrente)
Tributavel.register(ContaInvestimento)

print(cc.get_valor_imposto())
print(s.get_valor_imposto())
print(ci.get_valor_imposto())

lista_tributos = []
lista_tributos.append(cc)
lista_tributos.append(s)
lista_tributos.append(ci)

#questao 13: objeto de conta poupance nao é tributavel
m = ManipuladorDeTriubutaveis()
total = m.calcula_impostos(lista_tributos)
print(total)




#3 questao
#nao posso instanciar uma classe conta sem que o metodo atualiza seja implementado
