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


def body_request(stub):
    """
    Requests the location, velocity, and mass of bodies in the current simulation
    """
    request = simulation_pb2.SimCurrentStateReq()
    try:
        response = stub.StateReply(request)
        return response
    except grpc.RpcError as e:
        print(f"gRPC call failed: {e.code()}: {e.details()}")
