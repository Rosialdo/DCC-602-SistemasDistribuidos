import subprocess
import grpc
import remote_control_pb2
import remote_control_pb2_grpc
from concurrent import futures
import logging

# Configuração básica do registro de log
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Implementação do serviço gRPC
class RemoteControlServicer(remote_control_pb2_grpc.RemoteControlServicer):
    def ExecuteCommand(self, request, context):
        command = request.command
        logging.info(f'Command received: {command}')  # Registra o comando recebido no log
        output = subprocess.check_output(request.command, shell=True)  # Executa o comando no sistema operacional
        return remote_control_pb2.CommandResponse(output=output.decode('utf-8'))  # Retorna a saída do comando

# Função para iniciar o servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Cria um servidor gRPC
    remote_control_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)  # Registra o serviço no servidor
    server.add_insecure_port('[::]:50051')  # Configura a porta em que o servidor irá escutar as conexões
    server.start()  # Inicia o servidor
    server.wait_for_termination()  # Aguarda as chamadas de procedimento remoto

if __name__ == '__main__':
    serve()  # Inicia o servidor quando o script é executado diretamente
