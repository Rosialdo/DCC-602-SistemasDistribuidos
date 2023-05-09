import socket
import threading

#handle_client_connection será executada em uma nova thread para cada cliente
def handle_client_connection(conn, addr):
    
    print(f"Nova conexão recebida de {addr[0]}:{addr[1]}")

    #incia um loop infinito para receber as mensagens do cliente
    while True:
        #recebe a mensagens do cliente por meio do soket
        data = conn.recv(1024)

        #se não houver mensagens o loop é interrompido
        if not data:
            break
        #converte a string recebida, que está em bytes, para string   
        message = data.decode()

        #inverte a string recebida
        response_reverse = message[::-1]

        #envia a string recebida, já invertida, de volta para o cliente e converte para bytes
        conn.sendall(response_reverse.encode())

    #printa a mensagem quando a conexão é encerrada
    print(f"A conexão com {addr[0]}:{addr[1]} foi encerrada.")

    #encerra a conexão com o cliente
    conn.close()

#startar o server
def start_server():
    #define o endereço IP que o servidor deve escutar
    server_host = ""
    #define a porta que o servidor deve escutar
    server_port = 5555

    #cria um objeto 'socket' para o servidor TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        #configura o socket para reutilizar endereços e portas locais após o encerramento do servidor, evitando o erro "Adress already in use"
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #associa o socket do servidor ao IP da porta passado
        server_socket.bind((server_host, server_port))

        #coloca o servidor em modo de escuta, permitndo que ele estabeleça conexões
        server_socket.listen()

        print(f"Servidor ouvindo na porta {server_port}...")

        #while infito para esperar por novas conexões dos clientes
        while True:
            #aguarda a conexão e retorna as informações de endereço, são um par: hostaddr, porta
            conn, addr = server_socket.accept() 

            #cria uma thread para o cliente que se conectou, ao criar a thread será executada a função 'handle_client_connection' e será passada como agurmento para a função 'conn' e 'adrr', contendo o endereço IP e porta
            client_thread = threading.Thread(target=handle_client_connection, args=(conn, addr))

            #inicia a thread com o novo cliente
            client_thread.start()

if __name__ == "__main__":
    start_server()
