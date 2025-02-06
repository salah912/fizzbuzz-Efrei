import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("n, expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
    (31, "31"),
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected