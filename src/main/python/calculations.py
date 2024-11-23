import numpy as np
import math


def calculate_energy(mass, velocity):
    v = np.linalg.norm(velocity)
    return mass * math.pow(v, 2) * 1 / 2
