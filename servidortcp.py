import socket

def fatorial(n):
    if n < 0:
        return "Erro: fatorial nao definido para numeros negativos"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print('Conectado com', addr)
        while True:
            data = conn.recv(1024)
            if not data: 
                break
            try:
                numero = int(data.decode('utf-8'))
                resultado = fatorial(numero)
                conn.sendall(str(resultado).encode('utf-8'))
                print(f'Recebido: {numero}, Enviado: {resultado}')
            except ValueError:
                conn.sendall('Erro: entrada invalida.'.encode('utf-8'))
                print(f'Erro: entrada invalida recebida de {(addr)}')
            except Exception as e:
                conn.sendall(f'Erro: {str(e)}'.encode('utf-8'))
                print(f'Erro ao processar: {e}')
            