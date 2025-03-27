import pytest
from src import calculator

def test_add():
    assert calculator.add(5, 3) == 8

def test_add_wrong():
    assert calculator.add_wrong(5, 3) == 8

def test_subtract():
    assert calculator.subtract(5,3)== 2

def test_multiply_wrong():
    assert calculator.multiply_wrong(5,3)== 15

def test_divide():
    assert calculator.divide(15,3)== 5

