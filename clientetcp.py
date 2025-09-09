import socket
HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST,PORT))
        print('Conexao estabelecida\n')
        
        numero_str = input("Digite um numero para calcular o fatorial: ")
        print(f'Enviando "{numero_str}" para o servidor...')
        s.sendall(numero_str.encode('utf-8'))

        data = s.recv(4096)
        print(f'Resposta do servidor: {data.decode("utf-8")}')
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Fechando o socket")
        s.close()
