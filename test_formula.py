import pytest
from formula import pitagoras

def test_pitagoras():
    assert pitagoras(3, 4) == 5.0, "Помилка для a=3, b=4"
