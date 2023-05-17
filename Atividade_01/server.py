import socket

def criptografa_caesar(texto, chave):
    cifrado = ""
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra) + chave
            if letra.isupper():
                if codigo > ord('Z'):
                    codigo -= 26
                elif codigo < ord('A'):
                    codigo += 26
            elif letra.islower():
                if codigo > ord('z'):
                    codigo -= 26
                elif codigo < ord('a'):
                    codigo += 26
            cifrado += chr(codigo)
        else:
            cifrado += letra
    return cifrado

def main():
    host = '127.0.0.1'
    porta = 12345
    
    chave = 3 # chave para criptografia Caesar
    
    s = socket.socket()
    s.bind((host, porta))
    s.listen(1)
    
    print(f"Servidor rodando em {host}:{porta}")
    
    conn, endereco = s.accept()
    print(f"Conectado a {endereco}")
    
    while True:
        dados = conn.recv(1024).decode()
        if not dados:
            break
        texto = criptografa_caesar(dados, chave)
        print(f"Mensagem recebida: {dados}")
        conn.send(texto.encode())
    
    conn.close()

if __name__ == '__main__':
    main()

