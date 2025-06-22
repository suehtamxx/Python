import abc
# --- Interfaces (ABCs) ---
class Compravel(abc.ABC):
    @abc.abstractmethod
    def comprar(self, jogo, quantidade):
        pass

class Logar(abc.ABC):
    @abc.abstractmethod
    def fazer_login(self, email, senha):
        pass

# --- Classes de Jogo ---
class Jogo():
    def __init__(self, nome, plataforma, preco):
        self._nome = nome
        self._plataforma = plataforma
        self._preco = preco

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def plataforma(self):
        return self._plataforma
    @plataforma.setter
    def plataforma(self, value):
        self._plataforma = value

    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, value):
        if value < 0:
            print("Aviso: Preco do jogo nao pode ser negativo. Ajustado para 0.")
            self._preco = 0.0
        else:
            self._preco = value

    def __str__(self):
        return f'Nome: {self.nome} | Plataforma: {self.plataforma} | Preco: R${self.preco:.2f}'


class JogoDigital(Jogo): 
    def __init__(self, nome, plataforma, preco, tamanho_gb):
        super().__init__(nome, plataforma, preco)
        self._tamanho_gb = tamanho_gb
        
    @property
    def tamanho_gb(self):
        return self._tamanho_gb
    @tamanho_gb.setter
    def tamanho_gb(self, value):
        self._tamanho_gb = value

class JogoFisico(Jogo):
    def __init__(self, nome, plataforma, preco):
        super().__init__(nome, plataforma, preco)

# --- Classes de Pessoa e Funcões ---
class Pessoa(): 
    def __init__(self, id_pessoa, nome, email, senha):
        self._id_pessoa = id_pessoa
        self._nome = nome
        self._email = email
        self._senha = senha

    @property
    def id_pessoa(self):
        return self._id_pessoa
    @id_pessoa.setter
    def id_pessoa(self, value):
        self._id_pessoa = value
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, value):
        self._senha = value

    def fazer_login(self, email, senha): 
        if email == self.email and senha == self.senha:
            print(f'Login de {self.nome} efetuado com sucesso!')
            return True
        else:
            print('Email ou senha incorretos!')
            return False

    def imprimir_perfil(self):
        print(f'Nome: {self.nome}\nEmail: {self.email}\nID: {self.id_pessoa}\n')


class Cliente(Pessoa): 
    def __init__(self, id_pessoa, nome, email, senha, saldo=0.0):
        super().__init__(id_pessoa, nome, email, senha)
        self._saldo = saldo
        self._jogos_comprados = [] 

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, value):
        if value < 0:
            print("Aviso: Saldo nao pode ser negativo. Ajustado para 0.")
            self._saldo = 0.0
        else:
            self._saldo = value

    @property
    def jogos_comprados(self):
        return self._jogos_comprados
    @jogos_comprados.setter
    def jogos_comprados(self, value):
        self._jogos_comprados = value

    def comprar(self, jogo, quantidade=1): 
        if quantidade <= 0:
            print('Quantidade invalida para compra.\n')
            return False
        total_a_pagar = jogo.preco * quantidade
        if self.saldo < total_a_pagar:
            print('Saldo insuficiente para comprar o jogo.\n')
            return False
        
        self.saldo -= total_a_pagar
        self.jogos_comprados.extend([jogo] * quantidade)
        print(f'Cliente {self.nome} comprou {quantidade} copia(s) de {jogo.nome}. Saldo atual: R${self.saldo:.2f}\n')
        return True
    
    def adicionar_saldo(self, valor):
        if valor <= 0:
            print("Erro: Valor para adicionar saldo deve ser maior que zero.")
            return False
        self.saldo += valor
        print(f'R${valor:.2f} adicionado ao saldo de {self.nome}. Saldo atual: R${self.saldo:.2f}.')
        return True

    def imprimir_jogos_comprados(self):
        if not self.jogos_comprados:
            print(f'O cliente {self.nome} nao possui jogos.\n')
            return
        print(f'\n--- Jogos de {self.nome} ---')
        for jogo in self.jogos_comprados:
            print(f'- {jogo.nome} ({jogo.plataforma})')

class Funcionario(Pessoa):
    def __init__(self, id_pessoa, nome, email, senha, cargo, salario, minha_loja):
        super().__init__(id_pessoa, nome, email, senha)
        self._cargo = cargo
        self._salario = salario
        self._minha_loja = minha_loja
    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, value):
        if value < 0:
            print("Aviso: Salario nao pode ser negativo. Ajustado para 0.")
            self._salario = 0.0
        else:
            self._salario = value
    @property
    def minha_loja(self):
        return self._minha_loja
    @minha_loja.setter
    def minha_loja(self, value):
        self._minha_loja = value
    def imprimir_perfil(self):
        super().imprimir_perfil()
        print(f'Cargo: {self.cargo}\nSalario: R${self.salario:.2f}\n')

class Gerente(Funcionario): 
    def __init__(self, id_pessoa, nome, email, senha, cargo, salario, minha_loja):
        super().__init__(id_pessoa, nome, email, senha, cargo, salario, minha_loja)
    
    def aprovar_desconto(self, jogo, percentual):
        if 0 <= percentual <= 100:
            desconto = jogo.preco * (percentual / 100)
            jogo.preco -= desconto
            print(f"Desconto de {percentual}% aplicado em '{jogo.nome}'. Novo preco: R${jogo.preco:.2f}")
        else:
            print("Percentual fora do intervalo permitido.")
    def imprimir_perfil(self):
        return super().imprimir_perfil()

    
class Loja(): 
    def __init__(self, id_loja, nome, endereco, telefone, saldo_inicial=0.0):
        self._id_loja = id_loja
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._saldo = saldo_inicial 
        self._jogos_digitais = {}  
        self._jogos_fisicos = {}    
        self._funcionarios = []
        self._historico = []

    @property
    def id_loja(self): 
        return self._id_loja
    @id_loja.setter
    def id_loja(self, value): 
        self._id_loja = value

    @property
    def nome(self): 
        return self._nome
    @nome.setter
    def nome(self, value): 
        self._nome = value

    @property
    def endereco(self): 
        return self._endereco
    @endereco.setter
    def endereco(self, value): 
        self._endereco = value

    @property
    def telefone(self): 
        return self._telefone
    @telefone.setter
    def telefone(self, value): 
        self._telefone = value

    @property
    def saldo(self): 
        return self._saldo
    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    @property
    def jogos_digitais(self): 
        return self._jogos_digitais
    @property
    def jogos_fisicos(self): 
        return self._jogos_fisicos

    @property
    def funcionarios(self): 
        return self._funcionarios
    @funcionarios.setter
    def funcionarios(self, value): 
        self._funcionarios = value
        
    def imprimir_jogos_estoque(self):
        if not self.jogos_digitais and not self.jogos_fisicos:
            print("Nenhum jogo cadastrado no estoque.")
            return

        print("\n--- Jogos Digitais ---")
        for jogo, qtd in self.jogos_digitais.items():
            print(f'{jogo} | Chaves disponiveis: {qtd}')

        print("\n--- Jogos Fisicos ---")
        for jogo, qtd in self.jogos_fisicos.items():
            print(f'{jogo} | Estoque: {qtd}')

    def adicionar_jogo_estoque(self, jogo, quantidade):
        if jogo is None or quantidade <= 0:
            print("Nao foi possivel adicionar o jogo: dados invalidos.")
            return

        estoque_alvo = None
        
        if isinstance(jogo, JogoDigital):
            estoque_alvo = self.jogos_digitais
        elif isinstance(jogo, JogoFisico):
            estoque_alvo = self.jogos_fisicos
        else:
            print("Erro: Tipo de jogo desconhecido. Nao foi possivel adicionar ao estoque.")
            return

        jogo_existente_encontrado = None
        for jogo_existente in estoque_alvo.keys():
           
            if isinstance(jogo, JogoDigital) and isinstance(jogo_existente, JogoDigital):
                if (jogo_existente.nome == jogo.nome and 
                    jogo_existente.plataforma == jogo.plataforma):
                    jogo_existente_encontrado = jogo_existente
                    break
            
            elif isinstance(jogo, JogoFisico) and isinstance(jogo_existente, JogoFisico):
                if (jogo_existente.nome == jogo.nome and 
                    jogo_existente.plataforma == jogo.plataforma):
                    jogo_existente_encontrado = jogo_existente
                    break

        if jogo_existente_encontrado:
           
            estoque_alvo[jogo_existente_encontrado] += quantidade
            print(f'Jogo "{jogo.nome}" (Tipo: {type(jogo).__name__.replace("Jogo", "")}) ja cadastrado. Adicionada(s) {quantidade} unidade(s). Total no estoque: {estoque_alvo[jogo_existente_encontrado]} unidades.\n')
        else:
          
            estoque_alvo[jogo] = quantidade
            print(f'Novo jogo "{jogo.nome}" (Tipo: {type(jogo).__name__.replace("Jogo", "")}) adicionado ao estoque com {quantidade} unidade(s).\n')

    def remover_jogo_estoque(self, jogo, quantidade):
        if isinstance(jogo, JogoDigital):
            estoque = self.jogos_digitais
        elif isinstance(jogo, JogoFisico):
            estoque = self.jogos_fisicos
        else:
            print("Tipo de jogo invalido.")
            return False

        if jogo not in estoque or estoque[jogo] < quantidade:
            print("Estoque insuficiente ou jogo nao encontrado.")
            return False

        estoque[jogo] -= quantidade
        if estoque[jogo] == 0:
            del estoque[jogo]
            print(f'Jogo "{jogo.nome}" esgotado e removido do estoque.\n')
        else:
            print(f'{quantidade} unidade(s) removida(s) de "{jogo.nome}". Restante: {estoque[jogo]}.\n')
        return True
    
    def vender_para_cliente(self, jogo, quantidade, cliente):
        if not isinstance(cliente, Cliente):
            print("Erro: O comprador nao eh um Cliente valido.")
            return False

        estoque = self.jogos_digitais if isinstance(jogo, JogoDigital) else self.jogos_fisicos

        if jogo not in estoque or estoque[jogo] < quantidade:
            print(f"Erro: Jogo '{jogo.nome}' indisponivel ou quantidade insuficiente.")
            return False

        if cliente.comprar(jogo, quantidade):
            self.saldo += (jogo.preco * quantidade)
            self.remover_jogo_estoque(jogo, quantidade)
            print(f"Venda realizada: {quantidade}x '{jogo.nome}' para {cliente.nome}")
            self._historico.append((jogo.nome, quantidade, cliente.nome))
            return True
        return False
    
    def adicionar_jogo(self):
        try:
            print("\nAdicionando jogo na loja\n")
            nome_jogo = input("Nome do jogo: ").lower()
            plataforma = input("Plataforma: ").lower()
            if plataforma == 'pc': 
                tipo_jogo_str = 'digital'
            else:
                tipo_jogo_str = input("Tipo de jogo (digital/fisico): ").lower()
            preco = float(input("Preco de custo para a loja: "))
            if preco <= 0:
                print("Erro: O preco de custo deve ser maior que zero.")
                return None,0

            qtd = int(input("Quantidade: "))
            if qtd <= 0:
                print("Erro: A quantidade deve ser maior que zero.")
                return None,0
            novo_jogo = None
            if tipo_jogo_str == "digital":
                tamanho_gb = float(input("Tamanho em GB: "))
                if tamanho_gb <= 0:
                    print("Erro: O tamanho em GB deve ser maior que zero.")
                    return None,0
                novo_jogo = JogoDigital(nome_jogo, plataforma, preco, tamanho_gb)
            elif tipo_jogo_str == "fisico":
                novo_jogo = JogoFisico(nome_jogo, plataforma, preco)
            else:
                print("Tipo de jogo invalido. Por favor, digite 'digital' ou 'fisico'.")
                return None,0

            return novo_jogo, qtd
        except ValueError:
            print("Entrada invalida. Certifique-se de digitar números para preco, quantidade e tamanho.")
            return None,0

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    def imprimir_historico(self):
        print("\n--- Historico de Vendas ---")
        for jogo, quantidade, comprador in self._historico:
            print(f"Jogo: {jogo} | Quantidade: {quantidade} | Comprador: {comprador}")
    def imprimir_funcionarios(self):
        if self.funcionarios == []:
            print("Nenhum funcionario cadastrado.\n")
        else:
            print("\n--- Funcionarios da Loja ---")
            for funcionario in self.funcionarios:
                print(f'Nome: {funcionario.nome} | Cargo: {funcionario.cargo} | ID: {funcionario.id_pessoa}\n')

# Classes que implementam Logar
Logar.register(Cliente)
Logar.register(Funcionario)
Logar.register(Gerente)

# Classes que implementam Compravel
Compravel.register(Loja)
Compravel.register(Cliente)

def verificar_nome_e_cargo(string):
    """
    Verifica se a string contem apenas letras apos remover espacos e nao eh vazia.
    Usada para nomes, cargos, nomes de loja, enderecos e telefones.
    """
    if not isinstance(string, str) or not string.strip(): #verifica se eh string e nao esta vazia ou so com espacos
        return False

    if string.replace(" ", "").isalpha() == False:
        return False
    return True

def verificar_salario(salario_str):
    """
    Verifica se a string pode ser convertida para um número float e se eh positiva.
    """
    try:
        salario = float(salario_str)
        return salario > 0
    except ValueError:
        return False

def verificar_id(id_str):
    """
    Verifica se a string pode ser convertida para um número inteiro positivo.
    """
    try:
        id_val = int(id_str)
        return id_val > 0
    except ValueError:
        return False
       

def exibir_menu_principal():
    print("\n--- Menu Principal da Loja de Jogos ---")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Funcionario")
    print("3. Cadastrar Gerente")
    print("4. Cadastrar Loja")
    print("5. Entrar como Cliente")
    print("6. Entrar como Funcionario")
    print("7. Entrar como Gerente")
    print("8. Imprimir Funcionarios de uma Loja")
    print("0. Sair")
    return input("Escolha uma opcao: ")

if __name__ == "__main__":
    print("\n--- Inicio do Sistema ---")

    clientes = []
    lojas_registradas = []
    g_funcionarios = []

    while True:
        opcao_menu = exibir_menu_principal()

        # Opcao 1: Cadastrar Cliente
        if opcao_menu == '1':
            print("\n--- Cadastro de Cliente ---")
            nome = input("Nome: ")
            if not verificar_nome_e_cargo(nome):
                print('Erro: Nome invalido. Deve conter apenas letras e nao ser vazio.')
                continue
            
            email = input("E-mail: ")
            if not email.strip():
                print('Erro: E-mail nao pode ser vazio.')
                continue

            senha = input("Senha: ")
            if not senha.strip():
                print('Erro: Senha nao pode ser vazia.')
                continue
            
            id_cliente_str = input("ID: ")
            if not verificar_id(id_cliente_str):
                print('Erro: ID invalido. Deve ser um numero inteiro positivo.')
                continue
            id_cliente = int(id_cliente_str)

            if any(c.id_pessoa == id_cliente for c in clientes):
                print('Erro: ID/Cliente ja cadastrado.')
            else:
                novo_cliente = Cliente(id_cliente, nome, email, senha)
                clientes.append(novo_cliente)
                print("Cliente cadastrado com sucesso!")

        # Opcao 2: Cadastrar Funcionario
        elif opcao_menu == '2': 
            if not lojas_registradas:
                print("\nNenhuma loja cadastrada, nao eh possivel cadastrar um funcionario.\n")
                continue
            
            print("\n--- Cadastro de Funcionario ---")
            print("\n--- Lojas Disponiveis ---")
            for loja_disp in lojas_registradas:
                print(f"Nome: {loja_disp.nome}, ID: {loja_disp.id_loja}")
            
            id_loja_selecionada_str = input("Qual ID da loja que o funcionario trabalha?\n")
            if not verificar_id(id_loja_selecionada_str):
                print("Erro: ID de loja invalido. Digite um numero inteiro positivo.")
                continue
            id_loja_selecionada = int(id_loja_selecionada_str)

            loja_encontrada = next((l for l in lojas_registradas if l.id_loja == id_loja_selecionada), None)

            if loja_encontrada is None:
                print('Loja nao encontrada.')
            else:
                id_funcionario_str = input("ID do Funcionario: ")
                if not verificar_id(id_funcionario_str):
                    print("Erro: ID de funcionario invalido. Digite um número inteiro positivo.")
                    continue
                id_funcionario = int(id_funcionario_str)

                if any(f.id_pessoa == id_funcionario for f in loja_encontrada.funcionarios):
                     print('Erro: ID/Funcionario ja cadastrado nesta loja.')
                else:
                    nome = input("Nome: ")
                    if not verificar_nome_e_cargo(nome):
                        print('Erro: Nome invalido. Deve conter apenas letras e nao ser vazio.')
                        continue
                    
                    email = input("E-mail: ")
                    if not email.strip():
                        print('Erro: E-mail nao pode ser vazio.')
                        continue

                    senha = input("Senha: ")
                    if not senha.strip():
                        print('Erro: Senha nao pode ser vazia.')
                        continue

                    cargo = input("Cargo: ")
                    if not verificar_nome_e_cargo(cargo): 
                        print('Erro: Cargo invalido. Deve conter apenas letras e nao ser vazio.')
                        continue 
                    
                    salario_str = input("Salario: ")
                    if not verificar_salario(salario_str):
                        print('Erro: Salario invalido. Deve ser um número positivo.')
                        continue
                    salario = float(salario_str)
                    
                    novo_func = Funcionario(id_funcionario, nome, email, senha, cargo, salario, loja_encontrada.nome)
                    loja_encontrada.adicionar_funcionario(novo_func) 
                    g_funcionarios.append(novo_func) 
                    print("Funcionario cadastrado com sucesso!")

        # Opcao 3: Cadastrar Gerente
        elif opcao_menu == '3': 
            if not lojas_registradas: 
                print("\nNenhuma loja cadastrada, nao eh possivel cadastrar um gerente.\n")
                continue
            
            print("\n--- Cadastro de Gerente ---")
            print("\n--- Lojas Disponiveis ---")
            for loja_disp in lojas_registradas:
                print(f"Nome: {loja_disp.nome}, ID: {loja_disp.id_loja}")
            
            id_loja_selecionada_str = input("Qual ID da loja que o gerente trabalhara?\n")
            if not verificar_id(id_loja_selecionada_str):
                print("Erro: ID de loja invalido. Digite um número inteiro positivo.")
                continue
            id_loja_selecionada = int(id_loja_selecionada_str)

            loja_encontrada = next((l for l in lojas_registradas if l.id_loja == id_loja_selecionada), None)

            if loja_encontrada is None:
                print('Loja nao encontrada.')
            else:
                id_gerente_str = input("ID do Gerente: ")
                if not verificar_id(id_gerente_str):
                    print("Erro: ID de gerente invalido. Digite um número inteiro positivo.")
                    continue
                id_gerente = int(id_gerente_str)

                if any(p.id_pessoa == id_gerente for p in loja_encontrada.funcionarios):
                     print('Erro: ID/Gerente ja cadastrado nesta loja.')
                else:
                    nome = input("Nome: ")
                    if not verificar_nome_e_cargo(nome):
                        print('Erro: Nome invalido. Deve conter apenas letras e nao ser vazio.')
                        continue
                    
                    email = input("E-mail: ")
                    if not email.strip():
                        print('Erro: E-mail nao pode ser vazio.')
                        continue

                    senha = input("Senha: ")
                    if not senha.strip():
                        print('Erro: Senha nao pode ser vazia.')
                        continue
                    
                    salario_str = input("Salario: ") 
                    if not verificar_salario(salario_str):
                        print('Erro: Salario invalido. Deve ser um número positivo.')
                        continue
                    salario = float(salario_str)
                    
                    novo_gerente = Gerente(id_gerente, nome, email, senha, 'Gerente', salario, loja_encontrada.nome) 
                    loja_encontrada.adicionar_funcionario(novo_gerente) 
                    g_funcionarios.append(novo_gerente) 
                    print("Gerente cadastrado com sucesso!")
        
        # Opcao 4: Cadastrar Loja
        elif opcao_menu == '4': 
            print("\n--- Cadastro de Loja ---")
            nome = input("Nome da loja: ")
            if not verificar_nome_e_cargo(nome): 
                print('Erro: Nome da loja invalido. Nao pode ser vazio e deve conter apenas letras.')
                continue
            
            endereco = input("Endereco da loja: ")
            if not endereco.strip():
                print('Erro: Endereco da loja nao pode ser vazio.')
                continue

            telefone = input("Telefone da loja: ")
            if not telefone.strip():
                print('Erro: Telefone da loja nao pode ser vazio.')
                continue
            
            id_loja_str = input("ID da loja: ")
            if not verificar_id(id_loja_str):
                print('Erro: ID invalido. Deve ser um número inteiro positivo.')
                continue
            id_loja = int(id_loja_str)

            if any(l.id_loja == id_loja for l in lojas_registradas):
                print('Erro: ID/Loja ja cadastrada.')
            else: 
                nova_loja = Loja(id_loja, nome, endereco, telefone) 
                lojas_registradas.append(nova_loja)
                print("Loja cadastrada com sucesso!")
        
        # Opcao 5: Entrar como Cliente
        elif opcao_menu == '5': 
            if not clientes: 
                print("\nNenhum cliente cadastrado, nao eh possivel entrar.\n")
                continue
            
            email = input("Email do Cliente: ")
            if not email.strip():
                print('Erro: E-mail nao pode ser vazio.')
                continue

            senha = input("Senha: ")
            if not senha.strip():
                print('Erro: Senha nao pode ser vazia.')
                continue

            cliente_logado = next((c for c in clientes if isinstance(c, Cliente) and c.email == email), None)

            if cliente_logado: 
                if cliente_logado.fazer_login(email, senha):
                    while True:
                        print(f"\n--- Menu Cliente ({cliente_logado.nome}) ---")
                        print("1. Ver perfil")
                        print("2. Adicionar Saldo")
                        print("3. Comprar Jogo")
                        print("4. Ver meus jogos")
                        print("0. Voltar")
                        opc = input("Escolha uma opcao: ")

                        if opc == '1':
                            cliente_logado.imprimir_perfil()
                            print(f'Saldo: R${cliente_logado.saldo:.2f}')
                        elif opc == '2':
                            valor_str = input("Quanto quer adicionar ao saldo? ")
                            try:
                                valor = float(valor_str)
                                if valor > 0:
                                    cliente_logado.adicionar_saldo(valor)
                                    print(f"Saldo atualizado: R${cliente_logado.saldo:.2f}")
                                else:
                                    print("O valor a ser adicionado deve ser positivo.")
                            except ValueError:
                                print("Valor invalido. Por favor, digite um número.")
                        elif opc == '3':
                            print("\n--- Compra de Jogos ---")
                            if not lojas_registradas: 
                                print("\nNenhuma loja cadastrada, nao eh possivel comprar um jogo.\n")
                                continue
                            
                            print("\n--- Lojas Disponiveis ---")
                            for loja_disp in lojas_registradas:
                                print(f"Nome: {loja_disp.nome}, ID: {loja_disp.id_loja}")
                            
                            id_loja_selecionada_str = input("Digite o ID da loja onde deseja comprar: ")
                            if not verificar_id(id_loja_selecionada_str):
                                print("ID de loja invalido. Digite um número inteiro positivo.")
                                continue
                            id_loja_selecionada = int(id_loja_selecionada_str)

                            loja_alvo = next((l for l in lojas_registradas if l.id_loja == id_loja_selecionada), None)

                            if loja_alvo is None:
                                print("Loja nao encontrada.")
                            else:
                                tipo = input('Vai comprar jogo digital ou fisico? [digital/fisico]: ').strip().lower()

                                if tipo == 'digital':
                                    if not loja_alvo.jogos_digitais:
                                        print('A loja nao possui jogos digitais disponiveis.')
                                    else:
                                        print(f"\n--- Jogos Digitais disponiveis na {loja_alvo.nome} ---")
                                        for jogo, qtd_estoque in loja_alvo.jogos_digitais.items():
                                            print(f'{jogo.nome} | Plataforma: {jogo.plataforma} | Preco: R${jogo.preco:.2f} | Chaves: {qtd_estoque}')
                                        
                                        nome_jogo = input("Nome do jogo para comprar: ")
                                        jogo_para_comprar = next((j for j in loja_alvo.jogos_digitais.keys() if j.nome.lower() == nome_jogo.lower()), None)

                                        if not jogo_para_comprar:
                                            print("Jogo digital nao encontrado.")
                                        else:
                                            qtd_compra_str = input(f"Quantidade de '{jogo_para_comprar.nome}' que deseja comprar: ")
                                            try:
                                                qtd_compra = int(qtd_compra_str)
                                                if qtd_compra <= 0:
                                                    print("A quantidade deve ser positiva.")
                                                else:
                                                    loja_alvo.vender_para_cliente(jogo_para_comprar, qtd_compra, cliente_logado)
                                            except ValueError:
                                                print("Quantidade invalida. Por favor, digite um número inteiro.")
                                        
                                elif tipo == 'fisico':
                                    if not loja_alvo.jogos_fisicos:
                                        print('A loja nao possui jogos fisicos disponiveis.')
                                    else:
                                        print(f"\n--- Jogos Fisicos disponiveis na {loja_alvo.nome} ---")
                                        for jogo, qtd_estoque in loja_alvo.jogos_fisicos.items():
                                            print(f'{jogo.nome} | Plataforma: {jogo.plataforma} | Preco: R${jogo.preco:.2f} | Estoque: {qtd_estoque}')
                                        
                                        nome_jogo = input("Nome do jogo para comprar: ")
                                        jogo_para_comprar = next((j for j in loja_alvo.jogos_fisicos.keys() if j.nome.lower() == nome_jogo.lower()), None)

                                        if not jogo_para_comprar:
                                            print("Jogo fisico nao encontrado.")
                                        else:
                                            qtd_compra_str = input(f"Quantidade de '{jogo_para_comprar.nome}' que deseja comprar: ")
                                            try:
                                                qtd_compra = int(qtd_compra_str)
                                                if qtd_compra <= 0:
                                                    print("A quantidade deve ser positiva.")
                                                else:
                                                    loja_alvo.vender_para_cliente(jogo_para_comprar, qtd_compra, cliente_logado)
                                            except ValueError:
                                                print("Quantidade invalida. Por favor, digite um número inteiro.")
                                        
                                else:
                                    print("Tipo invalido. Digite 'digital' ou 'fisico'.")

                        elif opc == '4':
                            cliente_logado.imprimir_jogos_comprados()
                        elif opc == '0':
                            print("Saindo do menu do cliente.")
                            break
                        else:
                            print("Opcao invalida. Por favor, escolha uma opcao valida.")
                else:
                    print("Login de Cliente falhou. E-mail ou senha incorretos.")
            else:
                print("Cliente nao encontrado.")
        
        # Opcao 6: Entrar como Funcionario
        elif opcao_menu == '6':
            if not g_funcionarios:
                print("\nNenhum funcionario cadastrado, nao eh possivel entrar.\n")
                continue
            
            email = input("E-mail do Funcionario: ")
            if not email.strip():
                print('Erro: E-mail nao pode ser vazio.')
                continue

            senha = input("Senha: ")
            if not senha.strip():
                print('Erro: Senha nao pode ser vazia.')
                continue
            
            func_logado = next((f for f in g_funcionarios if isinstance(f, Funcionario) and not isinstance(f, Gerente) and f.email == email), None)
            
            if func_logado:     
                minha_loja = next((l for l in lojas_registradas if l.nome == func_logado.minha_loja), None)
                
                if minha_loja is None:
                    print("Erro: A loja do funcionario nao foi encontrada. Contate o administrador.")
                    continue 

                if func_logado.fazer_login(email, senha):
                    while True:
                        print(f"\n--- Menu Funcionario ({func_logado.nome}) na Loja {minha_loja.nome} ---")
                        print("1. Ver perfil")
                        print("2. Ver jogos em estoque da loja")
                        print("3. Adicionar jogo para o estoque da Loja")
                        print("0. Voltar")
                        opc = input("Escolha uma opcao: ")

                        if opc == '1':
                            func_logado.imprimir_perfil()
                        elif opc == '2':
                            if not minha_loja.jogos_digitais and not minha_loja.jogos_fisicos:
                                print('Nenhum jogo cadastrado no estoque desta loja.')
                            else:
                                print(f'\n--- Estoque de Jogos na {minha_loja.nome} ---')
                                print('\n--- Jogos Digitais ---')
                                if not minha_loja.jogos_digitais:
                                    print('Nenhum jogo digital.')
                                else:
                                    for jogo, qtd in minha_loja.jogos_digitais.items():
                                        print(f'  {jogo.nome} | Plataforma: {jogo.plataforma} | Preco: R${jogo.preco:.2f} | Chaves: {qtd}')
                                print('\n--- Jogos Fisicos ---')
                                if not minha_loja.jogos_fisicos:
                                    print('Nenhum jogo fisico.')
                                else:
                                    for jogo, qtd in minha_loja.jogos_fisicos.items():
                                        print(f'  {jogo.nome} | Plataforma: {jogo.plataforma} | Preco: R${jogo.preco:.2f} | Estoque: {qtd}')
        
                        elif opc == '3':
                            novo_jogo, qtd = minha_loja.adicionar_jogo() 
                            if novo_jogo: 
                                minha_loja.adicionar_jogo_estoque(novo_jogo, qtd)
                            else:
                                print("Nao foi possivel adicionar o jogo devido a dados invalidos ou erro.")
                        elif opc == '0':
                            print("Saindo do menu do funcionario.")
                            break
                        else:
                            print("Opcao invalida.")
                else:
                    print("Login de Funcionario falhou. E-mail ou senha incorretos.")
            else:
                print("Funcionario nao encontrado ou nao eh um funcionario valido.")
        
        # Opcao 7: Entrar como Gerente
        elif opcao_menu == '7': 
            if not g_funcionarios:
                print("\nNenhum funcionario ou gerente cadastrado, nao eh possivel entrar.\n")
                continue
            
            email = input("E-mail do Gerente: ")
            if not email.strip():
                print('Erro: E-mail nao pode ser vazio.')
                continue

            senha = input("Senha: ")
            if not senha.strip():
                print('Erro: Senha nao pode ser vazia.')
                continue
            gerente_logado = next((f for f in g_funcionarios if isinstance(f, Gerente) and f.email == email), None)
            
            if gerente_logado:
                minha_loja = next((l for l in lojas_registradas if l.nome == gerente_logado.minha_loja), None)
                
                if minha_loja is None:
                    print("Erro: A loja do gerente nao foi encontrada. Contate o administrador.")
                    continue

                if gerente_logado.fazer_login(email, senha):
                    while True:
                        print(f"\n--- Menu Gerente ({gerente_logado.nome}) na Loja {minha_loja.nome} ---")
                        print("1. Ver perfil")
                        print("2. Ver jogos em estoque")
                        print("3. Aprovar desconto em jogo")
                        print("4. Ver saldo da loja")
                        print("5. Ver historico de vendas")
                        print("6. Adicionar jogo para o estoque da Loja")
                        print("0. Voltar")
                        opc = input("Escolha uma opcao: ")

                        if opc == '1':
                            gerente_logado.imprimir_perfil()
                        elif opc == '2':
                            if not minha_loja.jogos_digitais and not minha_loja.jogos_fisicos:
                                print('Nenhum jogo cadastrado no estoque desta loja.')
                            else:
                                print(f'\n--- Estoque de Jogos na {minha_loja.nome} ---')
                                print('\n--- Jogos Digitais ---')
                                if not minha_loja.jogos_digitais:
                                    print('Nenhum jogo digital.')
                                else:
                                    for jogo, qtd in minha_loja.jogos_digitais.items():
                                        print(f'  {jogo.nome} | Plataforma: {jogo.plataforma} | Preco: R${jogo.preco:.2f} | Chaves: {qtd}')
                                print('\n--- Jogos Fisicos ---')
                                if not minha_loja.jogos_fisicos:
                                    print('Nenhum jogo fisico.')
                                else:
                                    for jogo, qtd in minha_loja.jogos_fisicos.items():
                                        print(f'  {jogo.nome} | Plataforma: {jogo.plataforma} | Preco: R${jogo.preco:.2f} | Estoque: {qtd}')
                        elif opc == '3':
                            nome_jogo_desc = input("Nome do jogo para aplicar desconto: ")
                            tipo_jogo_desc = input("Tipo do jogo (digital ou fisico): ").strip().lower()

                            jogo_para_desconto = None
                            if tipo_jogo_desc == "digital":
                                jogo_para_desconto = next((j for j in minha_loja.jogos_digitais.keys() if j.nome.lower() == nome_jogo_desc.lower()), None)
                                if not jogo_para_desconto:
                                    print("Jogo digital nao encontrado.")
                            elif tipo_jogo_desc == "fisico":
                                jogo_para_desconto = next((j for j in minha_loja.jogos_fisicos.keys() if j.nome.lower() == nome_jogo_desc.lower()), None)
                                if not jogo_para_desconto:
                                    print("Jogo fisico nao encontrado.")
                            else:
                                print("Tipo invalido. Digite 'digital' ou 'fisico'.")
                                continue

                            if jogo_para_desconto:
                                perc_str = input("Percentual de desconto (ex: 10 para 10%): ")
                                try:
                                    perc = float(perc_str)
                                    if 0 <= perc <= 100: 
                                        gerente_logado.aprovar_desconto(jogo_para_desconto, perc)
                                        print(f"Desconto de {perc}% aplicado a '{jogo_para_desconto.nome}'. Novo preco: R${jogo_para_desconto.preco:.2f}")
                                    else:
                                        print("Percentual de desconto invalido. Deve ser entre 0 e 100.")
                                except ValueError:
                                    print("Percentual invalido. Por favor, digite um número.")

                        elif opc == '4':
                            print(f'Saldo da Loja: R${minha_loja.saldo:.2f}')
                        elif opc == '5':                      
                            if not minha_loja.historico_vendas: 
                                print('Nao ha historico de vendas para esta loja.')
                            else:
                                minha_loja.imprimir_historico_vendas() 
                        elif opc == '6':
                            novo_jogo, qtd = minha_loja.adicionar_jogo()
                            if novo_jogo:
                                minha_loja.adicionar_jogo_estoque(novo_jogo, qtd)
                            else:
                                print("Nao foi possivel adicionar o jogo devido a dados invalidos ou erro.")
                        elif opc == '0':
                            print("Saindo do menu do gerente.")
                            break
                        else:
                            print("Opcao invalida.")
                else:
                    print("Login de Gerente falhou. E-mail ou senha incorretos.")
            else:
                print("Gerente nao encontrado ou nao eh um gerente valido.")

        # Opcao 8: Imprimir Funcionarios de uma Loja
        elif opcao_menu == '8':
            if not lojas_registradas:
                print("\nNenhuma loja cadastrada para imprimir funcionarios.\n")
                continue
            
            print("\n--- Lojas Disponiveis ---")
            for l_disp in lojas_registradas:
                print(f'Nome: {l_disp.nome}, ID: {l_disp.id_loja}')
            
            id_loja_selecionada_str = input("ID da loja para ver funcionarios: ")
            if not verificar_id(id_loja_selecionada_str):
                print('Erro: ID da loja invalido. Digite um número inteiro positivo.')
                continue
            id_loja_selecionada = int(id_loja_selecionada_str)

            loja_alvo_func = next((l for l in lojas_registradas if l.id_loja == id_loja_selecionada), None)
            
            if loja_alvo_func:
                if not loja_alvo_func.funcionarios:
                    print(f"A loja '{loja_alvo_func.nome}' nao possui funcionarios cadastrados.")
                else:
                    loja_alvo_func.imprimir_funcionarios()
            else:
                print("Loja nao cadastrada.")
        
        # Opcao 0: Sair
        elif opcao_menu == '0':
            print("Saindo do sistema. Ate mais!")
            break
        
        # Opcao Invalida
        else:
            print("Opcao invalida. Por favor, escolha uma opcao entre 0 e 8.")
