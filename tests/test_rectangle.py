

def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(10 , 20)
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(10 , 20)
    assert my_rectangle.perimeter() == (10 *2) + (20 * 2)

def test_not_equal(my_rectangle , weird_rectangle):
    assert my_rectangle != weird_rectangle