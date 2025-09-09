import abc

class Emprestavel(abc.ABC):
    @abc.abstractmethod
    def obter_info(self):
        """ retornar informaçoes sobre a midia"""
        pass
    def verificar_disponibilidade(self):
        """ verifica se a midia ta disponivel para emprestimo"""
        pass
    
class Midia(abc.ABC):
    def __init__(self,titulo,autor,disponivel):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = disponivel 
    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def disponivel(self):
        return self._disponivel
    @titulo.setter
    def titulo(self,titulo):
        self._titulo = titulo
    @autor.setter
    def autor(self,autor):
        self._autor = autor
    @disponivel.setter
    def disponivel(self,disponivel):
        self._disponivel = disponivel

class EBook(Midia):
    def __init__(self,titulo,autor,formato):
        super().__init__(titulo,autor,disponivel=True)
        self._formato = formato
    @property
    def formato(self):
        return self._formato
    @formato.setter
    def formato(self,formato):
        self._formato = formato
    
    def obter_info(self):
        """ metodo da interface emprestavel para retornar informaçoes sobre a midia"""
        return f'Titulo: {self._titulo}\nAutor: {self._autor}\nFormato: {self._formato}'
    def verificar_disponibilidade(self):
        """ verifica se a midia ta disponivel para emprestimo"""
        if self._disponivel == True:
            return True
        else:
            return False
class AudioBook(Midia):
    def __init__(self,titulo,autor,duracao):
        super().__init__(titulo,autor,disponivel=True)
        self._duracao = duracao
    @property
    def duracao(self):
        return self._duracao
    @duracao.setter
    def duracao(self,duracao):
        self._duracao = duracao
    
    def obter_info(self):
        """ metodo da interface emprestavel para retornar informaçoes sobre a midia"""
        return f'Titulo: {self._titulo}\nAutor: {self._autor}\nDuracao: {self._duracao}'
    def verificar_disponibilidade(self):
        """ verifica se a midia ta disponivel para emprestimo"""
        if self._disponivel == True:
            return True
        else:
            return False

class RevistaDigital(Midia):
    def __init__(self,titulo,edicao,ano_publicacao):
        super().__init__(titulo,None,disponivel=True)
        self._edicao = edicao
        self._ano_publicacao = ano_publicacao
    @property
    def edicao(self):
        return self._edicao
    @property
    def ano_publicacao(self):
        return self._ano_publicacao
    @edicao.setter
    def edicao(self,edicao):
        self._edicao = edicao
    @ano_publicacao.setter
    def ano_publicacao(self,ano_publicacao):
        self._ano_publicacao = ano_publicacao
    
    def obter_info(self):
        """ metodo da interface emprestavel para retornar informaçoes sobre a midia"""
        return f'Titulo: {self._titulo}\nEdicao: {self._edicao}\nAno: {self._ano_publicacao}'
    def verificar_disponibilidade(self):
        """ verifica se a midia ta disponivel para emprestimo"""
        if self._disponivel == True:
            return True
        else:
            return False

class Biblioteca():
    def __init__(self):
        self.emprestados = []

    def emprestar_midia(self,midia):
        if isinstance(midia,Emprestavel):
            if midia.verificar_disponibilidade() == True:
                midia.disponivel = False
                self.emprestados.append(midia)
            else:
                print('Midia indisponivel')
        else:
            print('classe nao implementa Emprestavel')
    def devolver_midia(self,midia):
        if isinstance(midia,Emprestavel):
            if midia.verificar_disponibilidade() == False:
                midia.disponivel = True
                self.emprestados.remove(midia)
            else:
                print('Nao ha midia para devolver\n')
        else:
            print('classe nao implementa Emprestavel')
    def listar_itens_emprestados(self):
        for midia in self.emprestados:
            print(midia.obter_info())
            print('')

Emprestavel.register(EBook)
Emprestavel.register(AudioBook)
Emprestavel.register(RevistaDigital)

bib = Biblioteca()

ebook = EBook('Harry Potter','JK Rowling','PDF')
audiobook = AudioBook('O Senhor dos Aneis','JRR Tolkien',360)
revista = RevistaDigital('National Geographic',150,2023)

bib.emprestar_midia(ebook)
bib.emprestar_midia(audiobook)
bib.emprestar_midia(revista)
print('Todos emprestados\n')
bib.listar_itens_emprestados()

bib.devolver_midia(ebook)
print('agora sem o que foi devolvido\n')
bib.listar_itens_emprestados()