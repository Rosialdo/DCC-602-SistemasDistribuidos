import grpc
import click
import remote_control_pb2
import remote_control_pb2_grpc


@click.command()
@click.option('--host', default='localhost', help='Remote control server host.')
@click.option('--port', default=50051, help='Remote control server port.')
@click.argument('command', nargs=-1)
def execute_command(host, port, command):
    command_str = ' '.join(command)
    with grpc.insecure_channel(f'{host}:{port}') as channel:
        stub = remote_control_pb2_grpc.RemoteControlStub(channel)
        response = stub.ExecuteCommand(remote_control_pb2.ExecuteCommandRequest(command=command_str))
        print(response.output)


if __name__ == '__main__':
    execute_command()
