import time
import sys

from simulation_client import body_request, set_configuration
from calculations import calculate_energy, collision, escape, runtime

sys.path.append("./proto")

import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc


body_configuration = [
    {
        "bodyID": 1,
        "position": {"x": -150.0, "y": 10.0},
        "velocity": {"x": 0.0, "y": 0.0},
        "mass": 10.0,
    },
    {
        "bodyID": 2,
        "position": {"x": 200.0, "y": 1.0},
        "velocity": {"x": 0.0, "y": 0.0},
        "mass": 10.0,
    },
    {
        "bodyID": 3,
        "position": {"x": 1.0, "y": 1.0},
        "velocity": {"x": 0.0, "y": 0.0},
        "mass": 10.0,
    },
]


def main():
    server_address = "0.0.0.0:50051"

    try:
        with grpc.insecure_channel(server_address) as channel:
            stub = simulation_pb2_grpc.SimStub(channel)
            print(runtime(body_configuration, stub))
    except KeyboardInterrupt:
        print("[Agent] Stopping Agent")


if __name__ == "__main__":
    main()
