class Agenda():
	agenda = {}
	def __init__(self,nome, idade):
		self.nome = nome
		self.idade = idade
	def armazenar_contatos(self):
		nome = input('Digite o nome:\n')
		idade = int(input('Digite a idade:\n'))
		self.agenda[nome] = [nome, idade]
	def excluir_contato(self):
		nome = input('Digite o nome:\n')
		if nome in self.agenda:
			del self.agenda[nome]
		else:
			print('nome nao esta na agenda\n')
	def buscar_contato(self):
		nome = input('Digite o nome:\n')
		if nome in self.agenda:
			print(self.agenda[nome])
		else:
			print('nome nao esta na agenda\n')
	def imprimir_contatos(self):
		for i in self.agenda:
			print(self.agenda[i])
op = 0
while op != -1:
	op = int(input('1 - Adicionar contato\n2 - Excluir contato\n3 - Buscar contato\n4 - Imprimir contatos\n-1 - Sair\n'))
	if op == 1:
		if len(Agenda.agenda) < 10:
			Agenda.armazenar_contatos(Agenda)
		else:
			print('Agenda cheia\n')
	elif op == 2:
		Agenda.excluir_contato(Agenda)
	elif op == 3:
		Agenda.buscar_contato(Agenda)
	elif op == 4:
		Agenda.imprimir_contatos(Agenda)
	elif op == -1:
		print('Tchau...\n')
	else:
		print('Digite um valor valido\n')
		