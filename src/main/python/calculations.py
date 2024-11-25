import numpy as np
import math
import itertools
from simulation_client import body_request, set_configuration
import time


def collision(bodies):
    """
    Returns true if body positions are within radii of one another
    """
    combinations = itertools.combinations(bodies, 2)
    collision_flag = False
    for combination in combinations:
        b1, b2 = combination
        print(type(b1.position.y))
        vec1 = np.array([b1.position.x, b1.position.y])
        vec2 = np.array([b2.position.x, b2.position.y])
        distance = np.linalg.norm(vec1 - vec2)
        if round(distance, 2) <= 80.0:
            collision_flag = True

    return collision_flag


def escape(bodies):
    """
    Returns true if a body is no longer effect by the gravitational force of one of the others
    """
    combinations = itertools.combinations(bodies, 2)
    distance_flag = False
    for combination in combinations:
        b1, b2 = combination
        vec1 = np.array([b1.position.x, b1.position.y])
        vec2 = np.array([b2.position.x, b2.position.y])
        distance = np.linalg.norm(vec1 - vec2)
        g_f = (b1.mass * b2.mass) / (distance**2)
        if round(g_f, 5) == 0:
            distance_flag = True
    return distance_flag


def runtime(initial_configuration, stub):
    """
    Run the simulation with the passed in initial conditions until a failstate is achieved
    """
    set_configuration(initial_configuration, stub)
    start_time = time.time()
    while True:
        time.sleep(0.1)
        req = body_request(stub)
        if not req or not req.bodies:
            continue
        bodies = req.bodies
        if escape(bodies) or collision(bodies):
            break
    end_time = time.time()
    return end_time - start_time


def calculate_energy(mass, velocity):
    """
    Probably unnecessary energy of body function
    """
    velocity_vector = np.array([velocity.x, velocity.y])
    v = np.linalg.norm(velocity_vector)
    return mass * (v**2) * 1 / 2
