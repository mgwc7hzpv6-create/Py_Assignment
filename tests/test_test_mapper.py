"""
Unit tests for the test point mapping functionality.
"""

from math import sqrt

from src.test_mapper import TestDataMapper


def test_calculate_allowed_deviation():
    """
    Test that the allowed deviation follows the square-root-of-two rule.
    """
    test_mapper = TestDataMapper()

    result = test_mapper.calculate_allowed_deviation(2)

    assert result == 2 * sqrt(2)