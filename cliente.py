import socket
import sys

def main():
    udp_ip_address = "127.0.0.2"
    udp_port_no = 6790
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        numero_str = input("Digite um numero para calcular o fatorial: ")
        
        print(f'Enviando "{numero_str}" para o servidor...')
        sock.sendto(numero_str.encode('utf-8'), (udp_ip_address, udp_port_no))

        data, server = sock.recvfrom(4096)
        print(f'Resposta do servidor: {data.decode("utf-8")}')
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Fechando o socket")
        sock.close()

if __name__ == '__main__':
    main()