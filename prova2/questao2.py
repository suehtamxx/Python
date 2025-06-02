class Quarto():
    def __init__(self,numero,tipo,preco,disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = disponivel
        
class Reserva():
    def __init__(self):
        self.reservas = {}
        self.canceladas = {}
    def adicionar_reserva(self,quarto,hospede):
        if quarto.disponivel == True:
            quarto.disponivel = False
            self.reservas[quarto.numero] = hospede
            print('Quarto reservado com sucesso!\n')
        else:
            print('Quarto ja esta hospedado!\n')
    def cancelar_reserva(self,quarto):
        if quarto.disponivel == False:
            quarto.disponivel = True
            self.canceladas[quarto.numero] = self.reservas[quarto.numero]
            del self.reservas[quarto.numero]
            print('Reserva cancelada com sucesso!\n')
        else:
            print('Quarto nao esta hospedado!\n')
    def imprimir_reservas(self):
        for q in self.reservas:
            print(f'Quarto {q}: {self.reservas[q]}\n')
    def imprimir_canceladas(self):
        for q in self.canceladas:
            print(f'Quarto {q}: {self.canceladas[q]}\n')
q1 = Quarto(1,'Simples',100)
q2 = Quarto(2,'Duplo',150)
q3 = Quarto(3,'Suite',200)

reserva = Reserva()
reserva.adicionar_reserva(q1,'Maria')
reserva.adicionar_reserva(q2,'Joao')
reserva.adicionar_reserva(q3,'Pedro')
reserva.cancelar_reserva(q1)
print('Reservas:\n')
reserva.imprimir_reservas()
print('canceladas:\n')
reserva.imprimir_canceladas()
    
