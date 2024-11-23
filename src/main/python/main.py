import time
import sys

from simulation_client import body_request
from calculations import calculate_energy

sys.path.append("./proto")
import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc


def main():
    server_address = "0.0.0.0:50051"
    energy = [[]]
    with grpc.insecure_channel(server_address) as channel:
        body_request(server_address, channel, True)
        while True:
            time.sleep(2)
            body_state = body_request(server_address, channel, False)
            if body_state:
                for body in body_state:
                    print(calculate_energy(body.mass, body.velocity))


if __name__ == "__main__":
    main()
