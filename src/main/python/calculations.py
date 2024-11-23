import numpy as np
import math


def calculate_energy(mass, velocity):
    velocity_vector = np.array([velocity.x, velocity.y])
    v = np.linalg.norm(velocity_vector)
    return mass * math.pow(v, 2) * 1 / 2
