import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  
print(sys.path)

import source.shapes as shapes


@pytest.mark.parametrize("side_length ,  expected_area",[(5,25), (4,16),(9,81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length , expected_perimeter" , [(3,12) , (4,16) , (5,20)])
def test_multiple_permeters(side_length ,expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter