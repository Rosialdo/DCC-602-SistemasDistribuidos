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
        message_send = input( ) 

        sock.sendall(message_send.encode())

def handle_receive_message(sock):
    
    while True:
        message_receive = client_socket.recv(1) 

        print(message_receive.decode())

def handle_dos_attack(sock):

    while True:
        message_send = "F"*1

        sock.sendall(message_send.encode())

        time.sleep(0.00001)



#cria um objeto socket para o cliente usando TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    #incia uma conexão com o servidor, especificando a endereço IP e a porta do servidor
    client_socket.connect((server_host, server_port))
    if dos_attack:
        send_thread = threading.Thread(target=handle_dos_attack, args=(client_socket,))
    else:
        send_thread = threading.Thread(target=handle_send_message, args=(client_socket,))

    receive_thread = threading.Thread(target=handle_receive_message, args=(client_socket,))
    send_thread.start()
    receive_thread.start()
    send_thread.join()
    receive_thread.join()

    client_socket.close()
