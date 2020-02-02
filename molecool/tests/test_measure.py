"""
    Unit and regression test for the measure module.
    """

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np

def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect."""
    
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])
    
    expected_distance = 1
    
    calculated_distance = molecool.calculate_distance(r1, r2)
    
    assert expected_distance == calculated_distance
