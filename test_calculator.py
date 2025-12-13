"""
unit tests for the calculator functions
"""
# import pytest
from calculator import get_numbers, add_numbers, multiply_numbers
from unittest.mock import patch


def test_add_numbers_positive():
    # test addition with positive numbers
    assert add_numbers([1, 2, 3]) == 6
    assert add_numbers([10, 20]) == 30


def test_add_numbers_negative():
    # test addition with negative numbers
    assert add_numbers([-1, -2, -3]) == -6
    assert add_numbers([10, -5]) == 5


def test_add_numbers_single():
    # test addition with single number
    assert add_numbers([5]) == 5


def test_add_numbers_empty():
    # test addition with empty list
    assert add_numbers([]) == 0


def test_multiply_numbers_positive():
    # test multiplication with positive numbers
    assert multiply_numbers([2, 3, 4]) == 24
    assert multiply_numbers([2, 10]) == 20


def test_multiply_numbers_by_zero():
    # test multiplication with 0
    assert multiply_numbers([2, 0]) == 0
    assert multiply_numbers([1, 2, 0]) == 0


def test_multiply_numbers_single():
    # test multiplication with single number
    assert multiply_numbers([1]) == 1
    assert multiply_numbers([5]) == 5


def test_multiply_numbers_negative():
    # test multiplication with negative numbers
    assert multiply_numbers([2, -10]) == -20
    assert multiply_numbers([-4, -4]) == 16


@patch('builtins.input', side_effect=['5', '10', 'done'])
def test_get_numbers_valid(mock_input):
    # test getting valid numbers from user
    result = get_numbers()
    assert result == [5.0, 10.0]


@patch('builtins.input', side_effect=['5', 'abc', '10', 'done'])
def test_get_numbers_with_invalid(mock_input):
    # test getting numbers with invalid input
    result = get_numbers()
    assert result == [5.0, 10.0]