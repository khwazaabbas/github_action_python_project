import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(4, 6) == 24

def test_divide():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)