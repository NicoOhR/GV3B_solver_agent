import sys

sys.path.append("./proto")

import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc


def simulation_client():
    server_address = "0.0.0.0:50051"
    with grpc.insecure_channel(server_address) as channel:
        stub = simulation_pb2_grpc.SimStub(channel)
        request = simulation_pb2.SimReq()
        try:
            response = stub.Replies(request)
            print("Response received:")
            for body in response.bodies:
                print(f"Velocity: x={body.velocity.x}, y={body.velocity.y}")
                print(f"Position: x={body.position.x}, y={body.position.y}")
        except grpc.RpcError as e:
            print(f"gRPC call failed: {e.code()}: {e.details()}")


if __name__ == "__main__":
    simulation_client()
