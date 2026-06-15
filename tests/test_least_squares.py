"""
Unit tests for the least squares functionality.
"""

import pandas as pd

from src.least_squares import (
    calculate_max_absolute_deviation,
    calculate_sum_of_squared_errors,
)


def test_calculate_sum_of_squared_errors():
    """
    Test that the sum of squared errors is calculated correctly.
    """
    actual_values = pd.Series([1, 2, 3])
    predicted_values = pd.Series([1, 3, 5])

    result = calculate_sum_of_squared_errors(
        actual_values,
        predicted_values
    )

    assert result == 5


def test_calculate_max_absolute_deviation():
    """
    Test that the maximum absolute deviation is calculated correctly.
    """
    actual_values = pd.Series([1, 2, 3])
    predicted_values = pd.Series([1, 3, 5])

    result = calculate_max_absolute_deviation(
        actual_values,
        predicted_values
    )

    assert result == 2