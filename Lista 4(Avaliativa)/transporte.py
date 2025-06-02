import abc

class Veiculo(abc.ABC):
    @abc.abstractmethod
    def calcular_custo_viagem(self,distancia):
        """ metodo para calcular o custo da viagem de acordo com distancia percorrida"""
        pass

class Carro():
    def __init__(self,cons_combustivel):
        self._cons_combustivel = cons_combustivel #consumo do carro em km por litro
    @property
    def cons_combustivel(self):
        return self._cons_combustivel
    @cons_combustivel.setter
    def cons_combustivel(self,cons_combustivel):
        self._cons_combustivel = cons_combustivel
    def calcular_custo_viagem(self,distancia):
        litros_necessarios = distancia / self._cons_combustivel
        return distancia * litros_necessarios
class Moto():
    def __init__(self,cons_combustivel):
        self._cons_combustivel = cons_combustivel #consumo da moto em km por litro
    @property
    def cons_combustivel(self):
        return self._cons_combustivel
    @cons_combustivel.setter
    def cons_combustivel(self,cons_combustivel):
        self._cons_combustivel = cons_combustivel
    def calcular_custo_viagem(self,distancia):
        litros_necessarios = distancia / self._cons_combustivel
        return distancia * litros_necessarios
class Caminhao():
    def __init__(self,cons_combustivel):
        self._cons_combustivel = cons_combustivel #consumo do caminhao em km por litro
    @property
    def cons_combustivel(self):
        return self._cons_combustivel
    @cons_combustivel.setter
    def cons_combustivel(self,cons_combustivel):
        self._cons_combustivel = cons_combustivel
    def calcular_custo_viagem(self,distancia):
        litros_necessarios = distancia / self._cons_combustivel
        return distancia * litros_necessarios + 200

class CalculadoraCustoViagem():
    def __init__(self,custo_total=0):
        self._custo_total = custo_total
    @property
    def custo_total(self):
        return self._custo_total
    @custo_total.setter
    def custo_total(self,custo_total):
        self._custo_total = custo_total
    def calcular_e_armazenar_custo(self,veiculo,distancia):
        """ metodo para calcular e armazenar o custo da viagem, utilizando o veiculo e a distancia fornecida"""
        if isinstance(veiculo,Veiculo):
            self._custo_total += veiculo.calcular_custo_viagem(distancia)
        else:
            print('Veiculo nao reconhecido')
    def get_custo_total(self):
        return self._custo_total

Veiculo.register(Carro)
Veiculo.register(Moto)
Veiculo.register(Caminhao)

carro = Carro(10)
moto = Moto(15)
caminhao = Caminhao(12)

calc = CalculadoraCustoViagem()

calc.calcular_e_armazenar_custo(carro,100)
calc.calcular_e_armazenar_custo(moto,100)
calc.calcular_e_armazenar_custo(caminhao,100)

print(calc.get_custo_total())
            
        