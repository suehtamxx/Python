import mysql.connector
from mysql.connector import Error

print('Entre com os dados conforme solicitado\n')
idclien = input('Id cliente:\n')
nome = input('Nome do cliente:\n')
valor = input('Valor que deve:\n')
porce = input('Porcentagem:\n')
dados = idclien + ',\'' + nome + '\',' + valor + ',' + porce  + ')'
declaracao = '''INSERT INTO tbl_clientes
(idcliente, nomecliente, valor, porcentagem)
VALUES('''
sql = declaracao + dados
             
