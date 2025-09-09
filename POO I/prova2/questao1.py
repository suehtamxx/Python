class Maca():
    def __init__(self,id):
        self._id = id
    @property
    def id(self):
        return self._id
    @id.setter
    def ID(self,id):
        self._id = id
class Bandeija_de_maca():
    def __init__(self):
        self._lista = []
    @property
    def lista(self):
        return self._lista
    def adicionar_maca(self,maca):
        self._lista.append(maca)
    def lista_bandeija(self):
        for m in self.lista:
            print('Maca na bandeija: ', m.id)

m1 = Maca(1)
m2 = Maca(2)
bandeija = Bandeija_de_maca()
bandeija.adicionar_maca(m1)
bandeija.adicionar_maca(m2)
bandeija.lista_bandeija()
     
        