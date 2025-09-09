import socket
import sys

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

def main():
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    
    print('Servidor UDP iniciado, aguardando conexoes\n')
    
    while True:
        data, address = sock.recvfrom(4096)
        try:
            numero = int(data.decode('utf-8'))
            resultado = fatorial(numero)
            sock.sendto(str(resultado).encode('utf-8'), address)
            print(f'Recebido: {numero}, Enviado: {resultado}')
        except ValueError:
            sock.sendto('Erro: entrada invalida.'.endcode('utf-8'), address)
            print(f'Erro: entrada invalida recebida de {address}')
        except Exception as e:
            sock.sendto(f'Erro: {str(e)}'.encode('utf-8'), address)
            print(f'Erro ao processar: {e}')
if __name__ == '__main__':
    main()