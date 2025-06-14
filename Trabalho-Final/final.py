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

class Vendavel(abc.ABC): # Interface para Jogos (que podem ser vendidos)
    @abc.abstractmethod
    def calcular_preco_final(self):
        pass

    @abc.abstractmethod
    def obter_info_venda(self):
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

    def obter_info(self):
        return f"Título: {self.nome}, Plataforma: {self.plataforma}, Preço: R${self.preco:.2f}"

    def calcular_preco_final(self): 
        return self.preco

    def obter_info_venda(self): 
        return f"Título: {self.nome}, Preço: R${self.calcular_preco_final():.2f}"

class JogoDigital(Jogo): 
    def __init__(self, nome, plataforma, preco, tamanho_gb):
        super().__init__(nome, plataforma, preco)
        self._tamanho_gb = tamanho_gb
        self._chaves_disponiveis = 100 # Simula um estoque grande de chaves digitais

    @property
    def tamanho_gb(self):
        return self._tamanho_gb
    @tamanho_gb.setter
    def tamanho_gb(self, value):
        self._tamanho_gb = value

    @property
    def chaves_disponiveis(self):
        return self._chaves_disponiveis
    @chaves_disponiveis.setter
    def chaves_disponiveis(self, value):
        self._chaves_disponiveis = value

    def entregar_chave(self):
        if self.chaves_disponiveis <= 0:
            print(f"Erro: Não há chaves de ativação disponíveis para {self.nome}.")
            return False
        self.chaves_disponiveis -= 1
        print(f"Chave digital de {self.nome} entregue.")
        return True

    def obter_info_venda(self): # Sobrescreve para incluir info digital
        return f"{super().obter_info_venda()} (Digital, {self.tamanho_gb}GB, Estoque: {self.chaves_disponiveis} chaves)"

class JogoFisico(Jogo):
    def __init__(self, nome, plataforma, preco):
        super().__init__(nome, plataforma, preco)

    def decrementar_estoque(self):
        if self.estoque_unidades <= 0:
            print(f"Erro: Estoque físico de {self.nome} esgotado.")
            return False
        self.estoque_unidades -= 1
        print(f"Estoque físico de {self.nome} decrementado.")
        return True

    def obter_info_venda(self): # Sobrescreve para incluir info física
        return f"{super().obter_info_venda()} (Físico, Estoque: {self.estoque_unidades} unidades)"

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
        print(f'--- Perfil de {self.nome} ---\nEmail: {self.email} ---\n ID: {self.id_pessoa}\n')


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
        print(f'Gerente {self.nome} aprovou desconto de {percentual}% para {jogo.nome}.')
        return jogo.aplicar_desconto(percentual)
    
class Loja(): 
    def __init__(self, id_loja, nome, endereco, telefone, saldo_inicial=0.0):
        self._id_loja = id_loja
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._saldo = saldo_inicial 
        self._jogos_estoque = {} 
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
        if value < 0:
            print("Aviso: Saldo da loja não pode ser negativo. Ajustado para 0.")
            self._saldo = 0.0
        else:
            self._saldo = value

    @property
    def jogos_estoque(self):
        return self._jogos_estoque
    @jogos_estoque.setter
    def jogos_estoque(self, value):
        self._jogos_estoque = value
    @property
    def funcionarios(self):
        return self._funcionarios
    @funcionarios.setter
    def funcionarios(self, value):
        self._funcionarios = value
        
    def imprimir_jogos_estoque(self):
        if not self.jogos_estoque:
            print('Nenhum jogo cadastrado no estoque da loja.\n')
            return
        print('\n--- Jogos em Estoque na Loja ---')
        for jogo, quantidade in self.jogos_estoque.items():
            print(f'Título: {jogo.nome} | Plataforma: {jogo.plataforma} | Preço: R${jogo.preco:.2f} | Estoque: {quantidade}')

    def adicionar_jogo_estoque(self, jogo, quantidade):
        if jogo in self.jogos_estoque:
            self.jogos_estoque[jogo] += quantidade
        else:
            self.jogos_estoque[jogo] = quantidade
        print(f'Jogo "{jogo.nome}" adicionado ao estoque da loja. Estoque atual: {self.jogos_estoque[jogo]}\n')

    def remover_jogo_estoque(self, jogo, quantidade):
        if jogo not in self.jogos_estoque:
            print('Erro: Jogo não cadastrado no estoque da loja.\n')
            return False
        if self.jogos_estoque[jogo] < quantidade:
            print(f'Erro: Quantidade ({quantidade}) indisponível em estoque para "{jogo.nome}". Disponível: {self.jogos_estoque[jogo]}.\n')
            return False
        
        self.jogos_estoque[jogo] -= quantidade
        if self.jogos_estoque[jogo] == 0:
            del self.jogos_estoque[jogo]
            print(f'Jogo "{jogo.nome}" esgotado e removido do estoque.\n')
        else:
            print(f'{quantidade} cópia(s) de "{jogo.nome}" removida(s) do estoque. Restante: {self.jogos_estoque[jogo]}.\n')
        return True
    
    def vender_para_cliente(self, jogo, quantidade, cliente):
        """A Loja vende jogos para um Cliente."""
        if not isinstance(cliente, Cliente):
            print("Erro: O comprador não é um Cliente válido.")
            return False
        
        if jogo not in self.jogos_estoque or self.jogos_estoque[jogo] < quantidade:
            print(f"Erro: Jogo '{jogo.nome}' indisponível ou quantidade ({quantidade}) não em estoque da loja.")
            return False
        
        if cliente.comprar(jogo, quantidade): 
            self.saldo += (jogo.preco * quantidade) 
            self.remover_jogo_estoque(jogo, quantidade) 
            
            print(f"Loja vendeu {quantidade} cópia(s) de '{jogo.nome}' para {cliente.nome}. Saldo da Loja: R${self.saldo:.2f}.\n")
            self._historico.append((jogo.nome, quantidade, cliente.nome))
            return True
        return False 
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

# Classes que implementam Vendavel
Vendavel.register(Jogo)
Vendavel.register(JogoDigital)
Vendavel.register(JogoFisico)

#Listas de Clientes, Funcionários e Lojas
clientes = []
funcionarios = []
lojas_registradas = []


def exibir_menu_principal():
    print("\n--- Menu Principal da Loja de Jogos ---")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Funcionário")
    print("3. Cadastrar Gerente")
    print("4. Cadastrar Loja")
    print("5. Entrar como Cliente")
    print("6. Entrar como Funcionário")
    print("7. Entrar como Gerente")
    print("8. Menu da Loja (Admin)")
    print("0. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    print("\n--- Início do Sistema ---")

    while True:
        opcao_menu = exibir_menu_principal()

        if opcao_menu == '1': #Cliente
            print("\n--- Cadastro de Cliente ---")
            nome = input("Nome: ")
            email = input("E-mail: ")
            senha = input("Senha: ")
            if clientes == []:
                id_cliente = 1
            else:
                id_cliente = len(clientes) + 1
            novo_cliente = Cliente(id_cliente, nome, email, senha)
            clientes.append(novo_cliente)
            print("Cliente cadastrado com sucesso!")

        elif opcao_menu == '2': #Funcionario
            if lojas_registradas == []:
                print("\nNenhuma loja cadastrada, não é possivel cadastrar um funcionário.\n")
            else:
                print("\n--- Cadastro de Funcionário ---")
                nome = input("Nome: ")
                email = input("E-mail: ")
                senha = input("Senha: ")
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))
                if funcionarios == []:
                    id_funcionario = 1
                else:
                    id_funcionario = len(funcionarios) + 1
                    
                for loja in lojas_registradas:
                    print(f"Nome: {loja.nome}, ID: {loja.id_loja}")
                loja = int(input("Qual ID da loja que trabalha?\n"))
                if not any(u for u in lojas_registradas if u.id_loja == loja):
                    print('Loja nao encontrada')
                else:
                    loja = next((u for u in lojas_registradas if u.id_loja == loja), None)
                    if isinstance(loja, Loja):
                        novo_func = Funcionario(id_funcionario, nome, email, senha, cargo, salario, loja.nome)
                        loja.adicionar_funcionario(novo_func)
                    else:
                        print('Loja nao encontrada')
                    funcionarios.append(novo_func)
                    print("Funcionário cadastrado com sucesso!")
        elif opcao_menu == '3': #Gerente
            if lojas_registradas == []:
                print("\nNenhuma loja cadastrada, não é possivel cadastrar um gerente.\n")
            else:
                print("\n--- Cadastro de Gerente ---")
                nome = input("Nome: ")
                email = input("E-mail: ")
                senha = input("Senha: ")
                salario = float(input("Salário: "))
                if funcionarios == []:
                    id_funcionario = 1
                else:
                    id_funcionario = len(funcionarios) + 1
                for loja, i in lojas_registradas:
                    print(f"Nome: {loja.nome}, ID: {i}")
                loja = int(input("Qual o ID da loja que trabalha?\n"))
                if not any(u for u in lojas_registradas if u.id_loja == loja):
                    print('Loja nao encontrada')
                else:
                    loja = next((u for u in lojas_registradas if u.id_loja == loja), None)
                    if isinstance(loja, Loja):
                        novo_func = Gerente(id_funcionario, nome, email, senha,'Gerente', salario, loja.nome)
                        loja.adicionar_funcionario(novo_func)
                    else:
                        print('Loja nao encontrada')
                    funcionarios.append(novo_func)
                    print("Gerente cadastrado com sucesso!")
        elif opcao_menu == '4': #Loja
            print("\n--- Cadastro de Loja ---")
            nome = input("Nome da loja: ")
            endereco = input("Endereço da loja: ")
            telefone = input("Telefone da loja: ")
            if lojas_registradas == []:
                id_loja = 1
            else:
                id_loja = len(lojas_registradas) + 1
                
            nova_loja = Loja(id_loja, nome, endereco, telefone)
            lojas_registradas.append(nova_loja)
            print("Loja cadastrada com sucesso!")
        elif opcao_menu == '5':  # Cliente
            if clientes == []:
                print("\nNenhum cliente cadastrado, não é possivel entrar.\n")
            else:
                email = input("Email do Cliente: ")
                senha = input("Senha: ")
                if not any(c for c in clientes if isinstance(c, Cliente) and c.email == email):
                    print('Cliente nao encontrado')
                else:
                    cliente_logado = next((c for c in clientes if isinstance(c, Cliente) and c.email == email), None)
                    if cliente_logado and cliente_logado.fazer_login(email, senha):
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
                                    print("Valor inválido.")
                            elif opc == '3':
                                print("\n--- Compra de Jogos ---")          
                                if lojas_registradas == []:
                                    print("\nNenhuma loja cadastrada, não é possivel comprar um jogo.\n")
                                else:
                                    print("\n--- Lojas ---")
                                    for loja in lojas_registradas:
                                        print(f"{loja.nome}, ID: {loja.id_loja}")
                                    loja = int(input("Digite o ID da loja onde deseja comprar: "))
                                    if not any(u for u in lojas_registradas if u.id_loja == loja):
                                        print("Loja nao encontrada.")
                                    else:
                                        loja = next((u for u in lojas_registradas if u.id_loja == loja), None)
                                        if isinstance(loja, Loja):
                                            if(loja.jogos_estoque == {}):
                                                print("Nenhum jogo cadastrado na loja.")
                                            else:
                                                loja.imprimir_jogos_estoque()
                                                nome_jogo = input("Nome do jogo para comprar: ")
                                                if not any(j for j in loja.jogos_estoque if j.nome == nome_jogo):
                                                    print("Jogo nao encontrado.")
                                                else:
                                                    qtd = input("Qual quantidade?: ")
                                                    jogo = next((j for j in loja.jogos_estoque if j.nome == nome_jogo), None)
                                                    loja.vender_para_cliente(jogo, qtd, cliente_logado)             
                                        else:
                                            print("Loja nao encontrada.")
                            elif opc == '4':
                                cliente_logado.imprimir_jogos_comprados()
                            elif opc == '0':
                                break
                            else:
                                print("Opção inválida.")
                    else:
                        print("Login de Cliente falhou.")

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
                                print("\nAdicionando jogo na loja:\n")
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
                                    minha_loja.adicionar_jogo_estoque(novo_jogo, qtd)
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
                            print("0. Voltar")
                            opc = input("Escolha uma opção: ")

                            if opc == '1':
                                gerente_logado.imprimir_perfil()
                            elif opc == '2':
                                minha_loja.imprimir_jogos_estoque()
                            elif opc == '3':
                                nome_jogo = input("Nome do jogo: ")
                                if not minha_loja.jogos_estoque:
                                    print("Nenhum jogo cadastrado no estoque da loja.")
                                elif not any(j for j in minha_loja.jogos_estoque if j.nome == nome_jogo):
                                    print("Jogo nao cadastrado no estoque da loja.")
                                else:
                                    jogo = next((j for j in minha_loja.jogos_estoque if j.nome == nome_jogo), None)
                                    if jogo:
                                        try:
                                            perc = float(input("Percentual de desconto: "))
                                            gerente_logado.aprovar_desconto(jogo, perc)
                                        except ValueError:
                                            print("Percentual inválido.")
                                    else:
                                        print("Jogo não encontrado.")
                            elif opc == '4':
                                print(f'Saldo da Loja: R${minha_loja.saldo:.2f}')
                            elif opc == '5':
                                minha_loja.imprimir_historico()
                            elif opc == '0':
                                break
                            else:
                                print("Opção inválida.")
                    else:
                        print("Login de Gerente falhou.")

        elif opcao_menu == '8':  # Menu da loja (Admin)
            while True:
                print("\n--- Menu da Loja (Admin) ---")
                print("1. Ver estoque")
                print("2. Ver saldo da loja")
                print("0. Voltar")
                opc = input("Escolha uma opção: ")
                if opc == '1':
                    minha_loja.imprimir_jogos_estoque()
                elif opc == '2':
                    print(f'Saldo da Loja: R${minha_loja.saldo:.2f}')
                elif opc == '0':
                    break
                else:
                    print("Opção inválida.")

        elif opcao_menu == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida.")
