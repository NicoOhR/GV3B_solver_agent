import time
import sys
import numpy as np
from simulation_client import body_request, set_configuration
from calculations import calculate_energy, collision, escape, runtime
import scipy
from scipy import optimize

sys.path.append("./proto")

import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc


def main():
    server_address = "0.0.0.0:50051"
    body_configuration = np.array([200,0,-200,0])
    learning_rate = 0.1
    try:
        with grpc.insecure_channel(server_address) as channel:
            stub = simulation_pb2_grpc.SimStub(channel)
            with grpc.insecure_channel(server_address) as channel:
                stub = simulation_pb2_grpc.SimStub(channel)
                result = optimize.minimize(lambda c: runtime(c, stub), body_configuration, method='Nelder-Mead')
                optimal = result.x
                print(optimal)
                
    except KeyboardInterrupt:
        print("[Agent] Stopping Agent")


if __name__ == "__main__":
    main()
