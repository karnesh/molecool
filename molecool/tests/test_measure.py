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

def test_calculate_distance_typeerror():
    
    
    r1 = [1, 0, 0]
    r2 = [2, 0, 0]
    with pytest.raises(TypeError):
        calculated_distance = molecool.calculate_distance(r1, r2)

def test_calculate_angle():
    """Test the calculate_angle function"""
        
    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_value = 90
            
    calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)
    assert expected_value == calculated_value

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
    
    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)
    
    expected_center = np.array([1,1,1])
    
    assert np.array_equal(center_of_mass, expected_center)

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [(np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45), (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ), (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
                                                    ])
def test_calculate_angle_many(p1, p2, p3, expected_angle):
    
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)
    
    assert expected_angle == pytest.approx(calculated_angle), F'{calculated_angle} {expected_angle}'
