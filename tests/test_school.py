import pytest
import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  
print(sys.path)
from source.school import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def empty_classroom():
    return Classroom(Teacher("Severus Snape"), [], "Potions")

@pytest.fixture
def classroom_with_students():
    students = [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]
    return Classroom(Teacher("Minerva McGonagall"), students, "Transfiguration")

def test_add_student(empty_classroom):
    empty_classroom.add_student(Student("Draco Malfoy"))
    assert len(empty_classroom.students) == 1

def test_add_student_raises_exception(classroom_with_students):
    with pytest.raises(TooManyStudents):
        classroom_with_students.add_student(Student("Neville Longbottom"))

def test_remove_student(classroom_with_students):
    classroom_with_students.remove_student("Hermione Granger")
    assert len(classroom_with_students.students) == 2

def test_change_teacher(classroom_with_students):
    new_teacher = Teacher("Horace Slughorn")
    classroom_with_students.change_teacher(new_teacher)
    assert classroom_with_students.teacher == new_teacher

@pytest.mark.parametrize("initial_students, expected_length", [([], 0), (["Harry Potter", "Ron Weasley"], 2)])
def test_initial_classroom_length(initial_students, expected_length):
    classroom = Classroom(Teacher("Albus Dumbledore"), [Student(name) for name in initial_students], "Defense Against the Dark Arts")
    assert len(classroom.students) == expected_length
