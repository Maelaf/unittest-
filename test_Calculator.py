from Calculator import Calculator
import pytest
def test_add():
    x=3
    y=5
    result=Calculator()

    assert result.add(x,y) == x+y 