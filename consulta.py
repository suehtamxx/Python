import mysql.connector
from mysql.connector import Error
from datetime import datetime
from decimal import Decimal
op = 0

def conect():
    try:
        global con
        con = mysql.connector.connect(
            host='localhost',
            database='db_devedores',
            user='root',
            password='fhjyz0402'
        )
        if con.is_connected():
            print('Conectado com sucesso\n')
    except Error as erro:
        print('Falha ao conectar no MySQL:', erro)

def cadastrar_cliente():
    nome = input('Nome do cliente:\n')

    try:
        conect()
        declaracao = 'INSERT INTO clientes (nome, quantidade_emprestimos) VALUES (%s, %s)'
        valores = (nome, 0)

        cursor = con.cursor()
        cursor.execute(declaracao, valores)
        con.commit()
        print(f'Cliente "{nome}" cadastrado com sucesso!')

    except Error as erro:
        print(f'Erro ao cadastrar cliente: {erro}')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def cadastrar_emprestimo():
    try:
        conect()
        mostrar_clientes()
        id_cliente = int(input('ID do cliente para o empréstimo:\n'))
        valor = float(input('Valor do empréstimo:\n'))
        juros = float(input('Porcentagem de juros (%):\n'))
        data_raw = input('Data do empréstimo (formato: dd/mm/aa): ')
        valor += valor * (juros/100)
        try:
            data_formatada = datetime.strptime(data_raw, "%d/%m/%y").strftime("%Y-%m-%d")
        except ValueError:
            print("Data inválida! Use o formato correto (ex: 20/01/25).")
            return

        declaracao = '''
            INSERT INTO emprestimos (id_cliente, valor, juros, data_emprestimo)
            VALUES (%s, %s, %s, %s)
        '''
        valores = (id_cliente, valor, juros, data_formatada)

        cursor = con.cursor()
        cursor.execute(declaracao, valores)

        # Atualizar quantidade de empréstimos na tabela clientes
        atualizar = 'UPDATE clientes SET quantidade_emprestimos = quantidade_emprestimos + 1 WHERE id = %s'
        cursor.execute(atualizar, (id_cliente,))
        
        con.commit()
        print('Empréstimo cadastrado com sucesso!')

    except Error as erro:
        print(f'Erro ao cadastrar empréstimo: {erro}')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def mostrar_clientes(conn=None):
    try:
        if not conn:
            conect()
            conn = con
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        resultados = cursor.fetchall()

        print('\n📋 Clientes:')
        for cliente in resultados:
            print(f'ID: {cliente[0]} | Nome: {cliente[1]} | Qtd. Empréstimos: {cliente[2]}')
    except Error as erro:
        print(f'Erro ao consultar clientes: {erro}')
    finally:
        if conn and conn.is_connected() and conn != con:  # Fecha só se for diferente da conexão principal
            conn.close()


def mostrar_emprestimos():
    try:
        conect()
        cursor = con.cursor()
        cursor.execute('''
            SELECT e.id, c.nome, e.valor, e.juros, e.data_emprestimo
            FROM emprestimos e
            JOIN clientes c ON c.id = e.id_cliente
        ''')
        emprestimos = cursor.fetchall()

        print('\n📋 Empréstimos:')
        for emp in emprestimos:
            print(f'ID: {emp[0]} | Cliente: {emp[1]} | Valor: R${emp[2]} | Juros: {emp[3]}% | Data: {emp[4]}')

    except Error as erro:
        print(f'Erro ao consultar empréstimos: {erro}')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def pagar_emprestimo():
    mostrar_emprestimos()
    emprestimo_id = int(input('ID do empréstimo que será pago:\n'))
    valor_pago = Decimal(input('Valor pago:\n'))

    try:
        conect()
        cursor = con.cursor()

        # Buscar valor atual do empréstimo
        cursor.execute('SELECT valor, id_cliente FROM emprestimos WHERE id = %s', (emprestimo_id,))
        resultado = cursor.fetchone()

        if not resultado:
            print("Empréstimo não encontrado.")
            return

        valor_atual, id_cliente = resultado
        novo_valor = valor_atual - valor_pago

        # Atualizar valor
        cursor.execute('UPDATE emprestimos SET valor = %s WHERE id = %s', (novo_valor, emprestimo_id))

        # Se zerou ou quitou, decrementa na tabela clientes
        if novo_valor <= 0:
            cursor.execute('''
                UPDATE clientes
                SET quantidade_emprestimos = quantidade_emprestimos - 1
                WHERE id = %s
            ''', (id_cliente,))
            print("Empréstimo quitado!")

        con.commit()
        print("Pagamento registrado com sucesso.")

    except Error as erro:
        print(f'Erro ao atualizar empréstimo: {erro}')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# MENU PRINCIPAL
if __name__ == '__main__':
    while op != -1:
        try:
            op = int(input('''
===== MENU =====
1 - Cadastrar Cliente
2 - Cadastrar Empréstimo
3 - Mostrar Clientes
4 - Mostrar Empréstimos
5 - Pagar Empréstimo
-1 - Sair
Escolha: '''))
        except ValueError:
            print("Digite uma opção válida!\n")
            continue

        if op == 1:
            cadastrar_cliente()
        elif op == 2:
            cadastrar_emprestimo()
        elif op == 3:
            mostrar_clientes()
        elif op == 4:
            mostrar_emprestimos()
        elif op == 5:
            pagar_emprestimo()
        elif op == -1:
            print('Saindo... 👋')
