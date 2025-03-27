import pytest
from src import calculator


def test_divide():
    with pytest.raises(ValueError) as exc:
        calculator.divide(5, 0)
    assert str(exc.value) == "Cannot divide by zero"


def test_divide_2():
    with pytest.raises(NameError) as exc:
        calculator.divide(5, 0)
    