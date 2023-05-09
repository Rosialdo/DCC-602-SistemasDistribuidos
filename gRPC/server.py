import grpc
import subprocess
import remote_control_pb2
import remote_control_pb2_grpc
from concurrent import futures


class RemoteControlServicer(remote_control_pb2_grpc.RemoteControlServicer):
    def ExecuteCommand(self, request, context):
        try:
            output = subprocess.check_output(request.command, shell=True)
            return remote_control_pb2.ExecuteCommandResponse(output=output.decode())
        except subprocess.CalledProcessError as e:
            return remote_control_pb2.ExecuteCommandResponse(output=e.output.decode())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    remote_control_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
