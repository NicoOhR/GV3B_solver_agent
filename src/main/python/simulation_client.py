import sys
import time

sys.path.append("./proto")

import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc


def body_request(server_address, channel):
    stub = simulation_pb2_grpc.SimStub(channel)
    request = simulation_pb2.SimReq(reset=True)
    try:
        response = stub.Replies(request)
        # print("Response received:")
        # for body in response.bodies:
        #    print(f"Velocity: x={body.velocity.x}, y={body.velocity.y}")
        #    print(f"Position: x={body.position.x}, y={body.position.y}")
        return response.bodies
    except grpc.RpcError as e:
        print(f"gRPC call failed: {e.code()}: {e.details()}")


if __name__ == "__main__":
    server_address = "0.0.0.0:50051"
    with grpc.insecure_channel(server_address) as channel:
        while True:
            time.sleep(5)
            print(f"{body_request(server_address, channel)}")
