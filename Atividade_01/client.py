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
    s.connect((host, porta))
    
    while True:
        mensagem = input("Digite a mensagem: ")
        s.send(mensagem.encode())
        texto = s.recv(1024).decode()
        texto_descriptografado = criptografa_caesar(texto, -chave) # descriptografa a mensagem recebida
        print(f"Resposta do servidor: {texto_descriptografado}")
    
    s.close()

if __name__ == '__main__':
    main()

