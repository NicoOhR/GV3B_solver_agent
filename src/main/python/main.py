import time
import sys

from simulation_client import body_request, set_configuration
from calculations import calculate_energy

sys.path.append("./proto")
import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc


body_configration = [
    {
        "bodyID": 1,
        "position": {"x": -150.0, "y": 0.0},
        "velocity": {"x": 0.0, "y": 15.0},
        "mass": 10.0,
    },
    {
        "bodyID": 2,
        "position": {"x": 200.0, "y": 0.0},
        "velocity": {"x": 0.0, "y": -15.0},
        "mass": 15.0,
    },
    {
        "bodyID": 3,
        "position": {"x": 0.0, "y": 0.0},
        "velocity": {"x": 0.0, "y": 0.0},
        "mass": 50.0,
    },
]


def main():
    server_address = "0.0.0.0:50051"
    energy = [[]]
    with grpc.insecure_channel(server_address) as channel:
        stub = simulation_pb2_grpc.SimStub(channel)
        set_configuration(stub, body_configration)
        while True:
            time.sleep(1)
            body_state = body_request(stub)
            if body_state:
                for body in body_state:
                    print(calculate_energy(body.mass, body.velocity))


if __name__ == "__main__":
    main()
