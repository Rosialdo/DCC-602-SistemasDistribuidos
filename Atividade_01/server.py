import socket

def criptografa_caesar(texto, chave):
    # Função para criptografar um texto usando a cifra de César com uma chave específica
    cifrado = ""
    for letra in texto:
        if letra.isalpha():  # Verifica se a letra é um caractere alfabético
            codigo = ord(letra) + chave  # Obtém o código numérico da letra e aplica a chave de deslocamento
            if letra.isupper():  # Verifica se a letra é maiúscula
                if codigo > ord('Z'):  # Verifica se o código excede o valor do 'Z' maiúsculo
                    codigo -= 26  # Se exceder, faz um loop de volta ao 'A' maiúsculo
                elif codigo < ord('A'):  # Verifica se o código é menor que o valor do 'A' maiúsculo
                    codigo += 26  # Se for, faz um loop para trás ao 'Z' maiúsculo
            elif letra.islower():  # Verifica se a letra é minúscula
                if codigo > ord('z'):  # Verifica se o código excede o valor do 'z' minúsculo
                    codigo -= 26  # Se exceder, faz um loop de volta ao 'a' minúsculo
                elif codigo < ord('a'):  # Verifica se o código é menor que o valor do 'a' minúsculo
                    codigo += 26  # Se for, faz um loop para trás ao 'z' minúsculo
            cifrado += chr(codigo)  # Adiciona a letra criptografada à string cifrado
        else:
            cifrado += letra  # Se não for uma letra alfabética, mantém o caractere original
    return cifrado

def main():
    host = '127.0.0.1'  # Endereço IP do servidor
    porta = 12345  # Porta de conexão do servidor
    
    chave = 3  # Chave para criptografia Caesar
    
    s = socket.socket()  # Cria um objeto de socket
    s.bind((host, porta))  # Associa o socket ao endereço IP e à porta
    s.listen(1)  # Habilita o socket para receber conexões
    
    print(f"Servidor rodando em {host}:{porta}")
    
    conn, endereco = s.accept()  # Aceita a conexão do cliente e obtém o objeto de conexão e o endereço do cliente
    
    print(f"Conectado a {endereco}")
    
    while True:
        dados = conn.recv(1024).decode()  # Recebe os dados enviados pelo cliente e decodifica-os em texto
        if not dados:
            break  # Se não houver dados recebidos, encerra o loop
        texto = criptografa_caesar(dados, chave)  # Criptografa os dados recebidos usando a cifra de César
        print(f"Mensagem recebida: {dados}")  # Exibe a mensagem recebida do cliente
        conn.send(texto.encode())  # Envia a mensagem criptografada de volta para o cliente
    
    conn.close()  # Encerra a conexão com o cliente

if __name__ == '__main__':
    main()
