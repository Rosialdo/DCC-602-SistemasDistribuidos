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
    s.connect((host, porta))  # Conecta ao servidor usando o endereço IP e a porta
    
    while True:
        mensagem = input("Digite a mensagem: ")  # Solicita ao usuário que digite uma mensagem
        s.send(mensagem.encode())  # Envia a mensagem para o servidor após codificá-la em bytes
        texto = s.recv(1024).decode()  # Recebe a resposta do servidor e decodifica-a em texto
        texto_descriptografado = criptografa_caesar(texto, -chave)  # Descriptografa a mensagem recebida
        print(f"Resposta do servidor: {texto_descriptografado}")  # Exibe a resposta do servidor
    
    s.close()  # Fecha a conexão com o servidor

if __name__ == '__main__':
    main()
