import sys
import time

sys.path.append("./proto")

import grpc
from proto import simulation_pb2
from proto import simulation_pb2_grpc


def set_configuration(bodies, stub):
    """
    Calls the SetConfiguration RPC to set the simulation configuration.
    """
    print("making configuration")
    sim_state = simulation_pb2.SimState(
        bodies=[
            simulation_pb2.BodyAttributes(
                bodyID=body["bodyID"],
                position=simulation_pb2.Vec2D(
                    x=body["position"]["x"], y=body["position"]["y"]
                ),
                velocity=simulation_pb2.Vec2D(
                    x=body["velocity"]["x"], y=body["velocity"]["y"]
                ),
                mass=body["mass"],
            )
            for body in bodies
        ]
    )
    response = stub.SetConfiguration(sim_state)
    print("Configuration Valid:", response.succeeded)


def body_request(stub):
    """
    Requests the location, velocity, and mass of bodies in the current simulation
    """
    request = simulation_pb2.SimCurrentStateReq()
    try:
        response = stub.StateReply(request)
        return response.bodies
    except grpc.RpcError as e:
        print(f"gRPC call failed: {e.code()}: {e.details()}")


if __name__ == "__main__":
    server_address = "0.0.0.0:50051"
    body_history = []
    bodies1 = [
        {
            "bodyID": 1,
            "position": {"x": -200.0, "y": 0.0},
            "velocity": {"x": 20.0, "y": 1.0},
            "mass": 10.0,
        },
        {
            "bodyID": 2,
            "position": {"x": 200.0, "y": 5.0},
            "velocity": {"x": -20.0, "y": -1.0},
            "mass": 20.0,
        },
    ]
    bodies2 = [
        {
            "bodyID": 1,
            "position": {"x": -200.0, "y": -100.0},
            "velocity": {"x": 20.0, "y": 1.0},
            "mass": 10.0,
        },
        {
            "bodyID": 2,
            "position": {"x": 200.0, "y": 100.0},
            "velocity": {"x": -20.0, "y": -1.0},
            "mass": 20.0,
        },
    ]

    with grpc.insecure_channel(server_address) as channel:
        stub = simulation_pb2_grpc.SimStub(channel)
        set_configuration(stub, bodies1)
        while True:
            time.sleep(5)
            body_state = body_request(stub)
            set_configuration(stub, bodies2)
            print(f"{body_state}")
            body_history.append(body_state)
