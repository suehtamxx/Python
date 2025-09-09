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
    udp_ip_address = "127.0.0.2"
    udp_port_no = 6790
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip_address, udp_port_no))
    print('Servidor UDP iniciado, aguardando conexoes\n')
    
    while True:
        data, address = sock.recvfrom(1024)
        try:
            numero = int(data.decode('utf-8'))
            resultado = fatorial(numero)
            sock.sendto(str(resultado).encode('utf-8'), address)

            print(f'Recebido: {numero}, Enviado: {resultado}')

        except ValueError:
            sock.sendto('Erro: entrada invalida.'.encode('utf-8'), address)
            print(f'Erro: entrada invalida recebida de {address}')

        except Exception as e:
            sock.sendto(f'Erro: {str(e)}'.encode('utf-8'), address)
            print(f'Erro ao processar: {e}')

if __name__ == '__main__':
    main()