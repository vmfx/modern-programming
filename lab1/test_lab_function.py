import pytest
from lab_function import count_digits

def test_count_digits():
    # Перевірка для числа 5
    assert count_digits(5) == 1
    
    # Перевірка для числа 1234
    assert count_digits(1234) == 4
    
    # Перевірка для числа 0
    assert count_digits(0) == 1
    
