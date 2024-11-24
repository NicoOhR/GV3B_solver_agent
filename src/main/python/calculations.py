import numpy as np
import math
import itertools


def collision(bodies):
    """
    If body positions are within radius of one another we fail the cost function
    """
    combinations = itertools.combinations(bodies, 2)
    collision_flag = False
    for combination in combinations:
        b1, b2 = combination
        vec1 = np.array([b1.position.x, b1.position.y])
        vec2 = np.array([b2.position.x, b2.position.y])
        distance = np.linalg.norm(vec1 - vec2)
        print(distance)
        if round(distance, 2) <= 80.0:
            collision_flag = True

    return collision_flag


def too_far():
    """
    if a body is no longer effect by the gravitational force of the others,
    we fail the cost function
    """


def cost(energies):
    """
    R^n -> R
    Cost function optimizing for a steady amount of energy in our system
    the theory being that we can use the deviation of the time series energy
    minimizing for that we get a stable system
    If the simulation failed (i.e. collision, sent off) we return a maximum amount
    """


def calculate_energy(mass, velocity):
    velocity_vector = np.array([velocity.x, velocity.y])
    v = np.linalg.norm(velocity_vector)
    return mass * (v**2) * 1 / 2
