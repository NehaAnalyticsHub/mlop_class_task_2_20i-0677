import pytest
from main import StudentsInMLOps

@pytest.fixture
def student_instance():
    return StudentsInMLOps()

def test_enroll_students(student_instance):
    student_instance.enrollStudents(10)
    assert student_instance.getTotalStrength() == 10

def test_drop_students(student_instance):
    student_instance.enrollStudents(10)
    student_instance.dropStudents(5)
    assert student_instance.getTotalStrength() == 5

def test_get_class_name(student_instance):
    assert student_instance.getClassName() == "StudentsInMLOps"
