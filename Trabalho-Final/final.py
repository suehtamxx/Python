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
            print("Aviso: Preço do jogo não pode ser negativo. Ajustado para 0.")
            self._preco = 0.0
        else:
            self._preco = value

    def __str__(self):
        return f'Nome: {self.nome} | Plataforma: {self.plataforma} | Preço: R${self.preco:.2f}'


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

# --- Classes de Pessoa e Funções ---
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
        print(f'--- Perfil de {self.nome} ---\nEmail: {self.email}\nID: {self.id_pessoa}\n')


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
            print("Aviso: Saldo não pode ser negativo. Ajustado para 0.")
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
            print('Quantidade inválida para compra.\n')
            return False
        total_a_pagar = jogo.preco * quantidade
        if self.saldo < total_a_pagar:
            print('Saldo insuficiente para comprar o jogo.\n')
            return False
        
        self.saldo -= total_a_pagar
        self.jogos_comprados.extend([jogo] * quantidade)
        print(f'Cliente {self.nome} comprou {quantidade} cópia(s) de {jogo.nome}. Saldo atual: R${self.saldo:.2f}\n')
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
            print(f'O cliente {self.nome} não possui jogos.\n')
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
            print("Aviso: Salário não pode ser negativo. Ajustado para 0.")
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
        print(f'Cargo: {self.cargo}\nSalário: R${self.salario:.2f}\n')

class Gerente(Funcionario): 
    def __init__(self, id_pessoa, nome, email, senha, cargo, salario, minha_loja):
        super().__init__(id_pessoa, nome, email, senha, cargo, salario, minha_loja)
    
    def aprovar_desconto(self, jogo, percentual):
        if 0 <= percentual <= 100:
            desconto = jogo.preco * (percentual / 100)
            jogo.preco -= desconto
            print(f"Desconto de {percentual}% aplicado em '{jogo.nome}'. Novo preço: R${jogo.preco:.2f}")
        else:
            print("Percentual fora do intervalo permitido.")


    
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
            print(f'{jogo} | Chaves disponíveis: {qtd}')

        print("\n--- Jogos Físicos ---")
        for jogo, qtd in self.jogos_fisicos.items():
            print(f'{jogo} | Estoque: {qtd}')

    def adicionar_jogo_estoque(self, jogo, quantidade):
        if isinstance(jogo, JogoDigital):
            estoque = self.jogos_digitais
        elif isinstance(jogo, JogoFisico):
            estoque = self.jogos_fisicos
        else:
            print("Tipo de jogo desconhecido.")
            return

        estoque[jogo] = estoque.get(jogo, 0) + quantidade
        print(f'Jogo "{jogo.nome}" adicionado ao estoque. Total: {estoque[jogo]} unidades.\n')

    def remover_jogo_estoque(self, jogo, quantidade):
        if isinstance(jogo, JogoDigital):
            estoque = self.jogos_digitais
        elif isinstance(jogo, JogoFisico):
            estoque = self.jogos_fisicos
        else:
            print("Tipo de jogo inválido.")
            return False

        if jogo not in estoque or estoque[jogo] < quantidade:
            print("Estoque insuficiente ou jogo não encontrado.")
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
            print("Erro: O comprador não é um Cliente válido.")
            return False

        estoque = self.jogos_digitais if isinstance(jogo, JogoDigital) else self.jogos_fisicos

        if jogo not in estoque or estoque[jogo] < quantidade:
            print(f"Erro: Jogo '{jogo.nome}' indisponível ou quantidade insuficiente.")
            return False

        if cliente.comprar(jogo, quantidade):
            self.saldo += (jogo.preco * quantidade)
            self.remover_jogo_estoque(jogo, quantidade)
            print(f"Venda realizada: {quantidade}x '{jogo.nome}' para {cliente.nome}")
            self._historico.append((jogo.nome, quantidade, cliente.nome))
            return True
        return False
    
    def adicionar_jogo(self):
        print("\nAdicionando jogo na loja\n")
        nome_jogo = input("Nome do jogo: ")
        plataforma = input("Plataforma: ")
        preco = float(input("Preço de custo para a loja: "))
        tipo_jogo = input("Tipo (digital/fisico): ")
        qtd = int(input("Quantidade: "))

        novo_jogo = None
        if tipo_jogo.lower() == "digital":
            tamanho_gb = float(input("Tamanho em GB: "))
            novo_jogo = JogoDigital(nome_jogo, plataforma, preco, tamanho_gb)
        elif tipo_jogo.lower() == "fisico":
            novo_jogo = JogoFisico(nome_jogo, plataforma, preco)
        else:
            print("Tipo inválido.")
        if novo_jogo:
            return novo_jogo,qtd
        else:
            return None
    def buscar_jogo_por_nome(self, nome, tipo):
        tipo = tipo.lower()
        if tipo == "digital":
            for jogo in self.jogos_digitais:
                if jogo.nome == nome:
                    return jogo
        elif tipo == "fisico":
            for jogo in self.jogos_fisicos:
                if jogo.nome == nome:
                    return jogo
        return None
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    def imprimir_historico(self):
        print("\n--- Histórico de Vendas ---")
        for jogo, quantidade, comprador in self._historico:
            print(f"Jogo: {jogo} | Quantidade: {quantidade} | Comprador: {comprador}")

# Classes que implementam Logar
Logar.register(Pessoa)
Logar.register(Funcionario)
Logar.register(Gerente)

# Classes que implementam Compravel
Compravel.register(Loja)
Compravel.register(Cliente)

#Listas de Clientes, Funcionários e Lojas
clientes = []
funcionarios = []
lojas_registradas = []

def verificar_nome_e_cargo(string):
    if string.isalpha() == False:
        return False
    return True
def verificar_salario(salario):
    if salario.isnumeric() == False:
        return False
    return True
        
def exibir_menu_principal():
    print("\n--- Menu Principal da Loja de Jogos ---")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Funcionário")
    print("3. Cadastrar Gerente")
    print("4. Cadastrar Loja")
    print("5. Entrar como Cliente")
    print("6. Entrar como Funcionário")
    print("7. Entrar como Gerente")
    print("0. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    print("\n--- Início do Sistema ---")

    while True:
        opcao_menu = exibir_menu_principal()

        if opcao_menu == '1': #Cliente
            print("\n--- Cadastro de Cliente ---")
            nome = input("Nome: ")
            if verificar_nome_e_cargo(nome):
                email = input("E-mail: ")
                senha = input("Senha: ")
                id_cliente = int(input("ID: "))
                if any(clientes.id_pessoa == id_cliente for clientes in clientes):
                    print('Erro: ID/Cliente ja cadastrado.')
                else:
                    novo_cliente = Cliente(id_cliente, nome, email, senha)
                    clientes.append(novo_cliente)
                    print("Cliente cadastrado com sucesso!")
            else:
                print('Erro: Nome deve ser uma string.')

        elif opcao_menu == '2': #Funcionario
            if lojas_registradas == []:
                print("\nNenhuma loja cadastrada, não é possivel cadastrar um funcionário.\n")
            else:
                print("\n--- Cadastro de Funcionário ---")
                nome = input("Nome: ")
                if verificar_nome_e_cargo(nome):
                    email = input("E-mail: ")
                    senha = input("Senha: ")
                    cargo = input("Cargo: ")
                    if verificar_nome_e_cargo(cargo):
                        salario_str = input("Salário: ")
                        if verificar_salario(salario_str):
                            salario = float(salario_str)
                            
                            id_funcionario = int(input("ID: "))
                            if any(funcionarios.id_pessoa == id_funcionario for funcionarios in funcionarios):
                                print('Erro: ID/Funcionario ja cadastrado.')
                            else:     
                                for loja_existente in lojas_registradas:
                                    print(f"Nome: {loja_existente.nome}, ID: {loja_existente.id_loja}")
                                    
                                id_loja_selecionada = int(input("Qual ID da loja que trabalha?\n"))
                                
                                loja_encontrada = next((u for u in lojas_registradas if u.id_loja == id_loja_selecionada), None)

                                if loja_encontrada is None: 
                                    print('Loja não encontrada')
                                else:
                                    novo_func = Funcionario(id_funcionario, nome, email, senha, cargo, salario, loja_encontrada.nome)
                                    loja_encontrada.adicionar_funcionario(novo_func)
                                    funcionarios.append(novo_func)
                                    print("Funcionário cadastrado com sucesso!")
                        else:
                            print('Erro: Salário deve ser um número.')
                    else:
                        print('Erro: Cargo deve ser uma string.')
                else:
                    print('Erro: Nome deve ser uma string.')
        elif opcao_menu == '3': # Gerente
            if lojas_registradas == []:
                print("\nNenhuma loja cadastrada, não é possível cadastrar um gerente.\n")
            else:
                print("\n--- Cadastro de Gerente ---")
                nome = input("Nome: ")
                if verificar_nome_e_cargo(nome): 
                    email = input("E-mail: ")
                    senha = input("Senha: ")
                    salario_str = input("Salário: ") 
                    if verificar_salario(salario_str):
                        salario = float(salario_str) 
    
                        id_gerente = int(input("ID: "))
                        if any(func.id_pessoa == id_gerente for func in funcionarios):
                            print('Erro: ID/Gerente já cadastrado.')
                        else:
                            for loja_existente in lojas_registradas:
                                print(f"Nome: {loja_existente.nome}, ID: {loja_existente.id_loja}")
                    
                            id_loja_selecionada = int(input("Qual o ID da loja que trabalha?\n"))

                            loja_encontrada = next((u for u in lojas_registradas if u.id_loja == id_loja_selecionada), None)

                            if loja_encontrada is None: 
                                print('Loja não encontrada')
                            else:
                                novo_gerente = Gerente(id_gerente, nome, email, senha, 'Gerente', salario, loja_encontrada.nome)
                                loja_encontrada.adicionar_funcionario(novo_gerente) 
                                funcionarios.append(novo_gerente) 
                                print("Gerente cadastrado com sucesso!")
                    else:
                        print('Erro: Salário deve ser um número válido.')
                else:
                    print('Erro: Nome deve ser uma string válida.')
        elif opcao_menu == '4': #Loja
            print("\n--- Cadastro de Loja ---")
            nome = input("Nome da loja: ")
            if verificar_nome_e_cargo(nome):
                endereco = input("Endereço da loja: ")
                telefone = input("Telefone da loja: ")
                id_loja = int(input("ID da loja: "))
                if any(lojas.id_loja == id_loja for lojas in lojas_registradas):
                    print('Erro: ID/Loja ja cadastrado.')
                else:     
                    nova_loja = Loja(id_loja, nome, endereco, telefone)
                    lojas_registradas.append(nova_loja)
                    print("Loja cadastrada com sucesso!")
            else:
                print('Erro: Nome deve ser uma string.')
        elif opcao_menu == '5':  # Cliente
            if clientes == []: 
                print("\nNenhum cliente cadastrado, não é possível entrar.\n")
            else:
                email = input("Email do Cliente: ")
                senha = input("Senha: ")

            #busca o cliente pelo email e verifica a instância para garantir que é um objeto Cliente
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
                        opc = input("Escolha uma opção: ")

                        if opc == '1':
                            cliente_logado.imprimir_perfil()
                            print(f'Saldo: R${cliente_logado.saldo:.2f}')
                        elif opc == '2':
                            try:
                                valor = float(input("Quanto quer adicionar ao saldo? "))
                                cliente_logado.adicionar_saldo(valor)

                            except ValueError:
                                print("Valor inválido. Por favor, digite um número.")
                        elif opc == '3':
                            print("\n--- Compra de Jogos ---")
                            if lojas_registradas == []: 
                                print("\nNenhuma loja cadastrada, não é possível comprar um jogo.\n")
                            else:
                                print("\n--- Lojas Disponíveis ---")
                                for loja_disp in lojas_registradas:
                                    print(f"Nome: {loja_disp.nome}, ID: {loja_disp.id_loja}")
                            
                                try:
                                    id_loja_selecionada = int(input("Digite o ID da loja onde deseja comprar: "))
                                except ValueError:
                                    print("ID de loja inválido. Digite um número.")
                                    continue

                                loja_alvo = next((l for l in lojas_registradas if l.id_loja == id_loja_selecionada), None)

                                if loja_alvo is None:
                                    print("Loja não encontrada.")
                                else:
                                    tipo = input('Vai comprar jogo digital ou físico? [digital/fisico]: ').strip().lower()

                                    if tipo == 'digital':
                                        if not loja_alvo.jogos_digitais:
                                            print('A loja não possui jogos digitais disponíveis.')
                                        else:
                                            print(f"\n--- Jogos Digitais disponíveis na {loja_alvo.nome} ---")
                                            for jogo, qtd in loja_alvo.jogos_digitais.items():
                                                print(f'{jogo.nome} | Plataforma: {jogo.plataforma} | Preço: R${jogo.preco:.2f} | Chaves: {qtd}')
                                            
                                            nome_jogo = input("Nome do jogo para comprar: ")
                                            jogo = next((j for j in loja_alvo.jogos_digitais if j.nome.lower() == nome_jogo.lower()), None)

                                            if not jogo:
                                                print("Jogo não encontrado.")
                                            else:
                                                try:
                                                    qtd = int(input(f"Quantidade de '{jogo.nome}' que deseja comprar: "))
                                                    if qtd <= 0:
                                                        print("A quantidade deve ser positiva.")
                                                    else:
                                                        loja_alvo.vender_para_cliente(jogo, qtd, cliente_logado)
                                                except ValueError:
                                                    print("Quantidade inválida.")
                                    
                                    elif tipo == 'fisico':
                                        if not loja_alvo.jogos_fisicos:
                                            print('A loja não possui jogos físicos disponíveis.')
                                        else:
                                            print(f"\n--- Jogos Físicos disponíveis na {loja_alvo.nome} ---")
                                            for jogo, qtd in loja_alvo.jogos_fisicos.items():
                                                print(f'{jogo.nome} | Plataforma: {jogo.plataforma} | Preço: R${jogo.preco:.2f} | Estoque: {qtd}')
                                            
                                            nome_jogo = input("Nome do jogo para comprar: ")
                                            jogo = next((j for j in loja_alvo.jogos_fisicos if j.nome.lower() == nome_jogo.lower()), None)

                                            if not jogo:
                                                print("Jogo não encontrado.")
                                            else:
                                                try:
                                                    qtd = int(input(f"Quantidade de '{jogo.nome}' que deseja comprar: "))
                                                    if qtd <= 0:
                                                        print("A quantidade deve ser positiva.")
                                                    else:
                                                        loja_alvo.vender_para_cliente(jogo, qtd, cliente_logado)
                                                except ValueError:
                                                    print("Quantidade inválida.")
                                    
                                    else:
                                        print("Tipo inválido. Digite 'digital' ou 'fisico'.")

                        elif opc == '4':
                            cliente_logado.imprimir_jogos_comprados()
                        elif opc == '0':
                            print("Saindo do menu do cliente.")
                            break
                        else:
                            print("Opção inválida. Por favor, escolha uma opção válida.")
                else:
                    print("Login de Cliente falhou. Email ou senha incorretos.")
            else:
                print("Cliente não encontrado.")
        elif opcao_menu == '6':  # Funcionário
            if funcionarios == []:
                print("\nNenhum funcionário cadastrado, não é possivel entrar.\n")
            else:
                email = input("Email do Funcionário: ")
                senha = input("Senha: ")
                if not any(f for f in funcionarios if isinstance(f, Funcionario) and f.email == email):
                    print('Funcionario nao encontrado')
                else:
                    func_logado = next((f for f in funcionarios if isinstance(f, Funcionario) and f.email == email), None)
                    minha_loja = next((l for l in lojas_registradas if l.nome == func_logado.minha_loja), None)
                    if func_logado and func_logado.fazer_login(email, senha):
                        while True:
                            print(f"\n--- Menu Funcionário ({func_logado.nome}) ---")
                            print("1. Ver perfil")
                            print("2. Ver jogos em estoque da loja")
                            print("3. Adicionar jogo para o estoque da Loja")
                            print("0. Voltar")
                            opc = input("Escolha uma opção: ")

                            if opc == '1':
                                func_logado.imprimir_perfil()
                            elif opc == '2':
                                minha_loja.imprimir_jogos_estoque()
                            elif opc == '3':
                                novo_jogo,qtd = minha_loja.adicionar_jogo()
                                if novo_jogo != None:
                                    minha_loja.adicionar_jogo_estoque(novo_jogo, qtd)
                                else:
                                    print("Erro ao adicionar jogo.")
                            elif opc == '0':
                                break
                            else:
                                print("Opção inválida.")
                    else:
                        print("Login de Funcionário falhou.")

        elif opcao_menu == '7':  # Gerente
            if funcionarios == []:
                print("\nNenhum funcionario cadastrado, não é possivel entrar.\n")
            else:
                email = input("Email do Gerente: ")
                senha = input("Senha: ")
                if not any(isinstance(f, Gerente) and f.email == email for f in funcionarios):
                    print("Gerente nao cadastrado.")
                else:
                    gerente_logado = next((f for f in funcionarios if isinstance(f, Gerente) and f.email == email), None)
                    minha_loja = next((l for l in lojas_registradas if l.nome == gerente_logado.minha_loja), None)
                    if gerente_logado and gerente_logado.fazer_login(email, senha):
                        while True:
                            print(f"\n--- Menu Gerente ({gerente_logado.nome}) ---")
                            print("1. Ver perfil")
                            print("2. Ver jogos em estoque")
                            print("3. Aprovar desconto em jogo")
                            print("4. Ver saldo da loja")
                            print("5. Ver historico de vendas")
                            print("6. Adicionar jogo para o estoque da Loja")
                            print("0. Voltar")
                            opc = input("Escolha uma opção: ")

                            if opc == '1':
                                gerente_logado.imprimir_perfil()
                            elif opc == '2':
                                minha_loja.imprimir_jogos_estoque()
                            elif opc == '3':
                                nome_jogo = input("Nome do jogo: ")
                                tipo_jogo = input("Tipo do jogo (digital ou fisico): ").strip().lower()

                                if minha_loja.jogos_digitais == {} and minha_loja.jogos_fisicos == {}:
                                    print("Nenhum jogo cadastrado no estoque da loja.")
                                elif tipo_jogo == "digital":
                                    jogo = next((j for j in minha_loja.jogos_digitais if j.nome.lower() == nome_jogo.lower()), None)
                                    if jogo:
                                        try:
                                            perc = float(input("Percentual de desconto: "))
                                            gerente_logado.aprovar_desconto(jogo, perc)
                                        except ValueError:
                                            print("Percentual inválido.")
                                    else:
                                        print("Jogo digital não encontrado.")
                                elif tipo_jogo == "fisico":
                                    jogo = next((j for j in minha_loja.jogos_fisicos if j.nome.lower() == nome_jogo.lower()), None)
                                    if jogo:
                                        try:
                                            perc = float(input("Percentual de desconto: "))
                                            gerente_logado.aprovar_desconto(jogo, perc)
                                        except ValueError:
                                            print("Percentual inválido.")
                                    else:
                                        print("Jogo físico não encontrado.")
                                else:
                                    print("Tipo inválido. Digite 'digital' ou 'fisico'.")

                            elif opc == '4':
                                print(f'Saldo da Loja: R${minha_loja.saldo:.2f}')
                            elif opc == '5':
                                minha_loja.imprimir_historico()
                            elif opc == '6':
                                novo_jogo,qtd = minha_loja.adicionar_jogo()
                                if novo_jogo != None:
                                    minha_loja.adicionar_jogo_estoque(novo_jogo, qtd)
                                else:
                                    print("Erro ao adicionar jogo.")
                            elif opc == '0':
                                break
                            else:
                                print("Opção inválida.")
                    else:
                        print("Login de Gerente falhou.")

        elif opcao_menu == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida.")
