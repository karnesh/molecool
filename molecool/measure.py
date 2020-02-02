"""
    This module is for functions which perform measurements.
"""

import numpy as np
from .atom_data import atomic_weights

def calculate_distance(rA, rB):
    """
    Calculate the distance between two points.
        
    Parameters
    ----------
    rA, rB : np.ndarray
    The coordinates of each point.
        
    Returns
    -------
    distance : float
    The distance between the two points.
    """

    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    return distance


def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
