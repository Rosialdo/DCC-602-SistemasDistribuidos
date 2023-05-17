import grpc
import click
import remote_control_pb2
import remote_control_pb2_grpc

@click.command()
@click.option('--server', default='localhost:50051', help='endereço do servidor')
def execute_command(server):
    # Cria um canal de comunicação gRPC com o servidor especificado
    channel = grpc.insecure_channel(server)
    
    # Cria um stub para chamar os métodos remotos do serviço
    stub = remote_control_pb2_grpc.RemoteControlStub(channel)
    
    while True:
        # Solicita ao usuário para digitar um comando
        command = input('Digite o comando desejado: ')
        
        # Chama o método ExecuteCommand do serviço remoto, passando o comando como parâmetro
        response = stub.ExecuteCommand(remote_control_pb2.CommandRequest(command=command))
        
        # Imprime a saída do comando
        print(response.output)

if __name__ == '__main__':
    # Executa a função execute_command quando o script é executado diretamente
    execute_command()
