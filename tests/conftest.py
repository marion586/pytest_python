import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  
print(sys.path)

import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10 , 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5,6)