"""
Unit tests for the least squares functionality.
"""
import unittest
import pandas as pd

from src.least_squares import (
    calculate_max_absolute_deviation,
    calculate_sum_of_squared_errors,
    find_best_ideal_functions,
)


class UnitTestLeastSquares(unittest.TestCase):

    def test_calculate_sum_of_squared_errors(self):
        """
        test sum of squared errors with known values.
        actual: [1, 2, 3], predicted: [1, 3, 5]
        errors are 0, 1, 2 so squared sum is 0 + 1 + 4 = 5
        """
        # differences are 0, 1, 2 so the result is easy to check by hand
        actual_values = pd.Series([1, 2, 3])
        predicted_values = pd.Series([1, 3, 5])

        result = calculate_sum_of_squared_errors(actual_values, predicted_values)

        self.assertEqual(result, 5, "sum of squared errors should be 5")

    def test_calculate_max_absolute_deviation(self):
        """
        test that the largest deviation is picked correctly.
        actual: [1, 2, 3], predicted: [1, 3, 5]
        deviations are 0, 1, 2 so the maximum is 2
        """
        # same input as above, largest gap between actual and predicted is 2
        actual_values = pd.Series([1, 2, 3])
        predicted_values = pd.Series([1, 3, 5])

        result = calculate_max_absolute_deviation(actual_values, predicted_values)

        self.assertEqual(result, 2, "maximum absolute deviation should be 2")


class UnitTestFindBestIdealFunctions(unittest.TestCase):

    def test_selects_lowest_sse_function(self):
        """
        With one training function and two candidates, the candidate
        that matches exactly (SSE = 0) must be chosen over the other.
        """
        training_df = pd.DataFrame({
            "x": [0, 1, 2],
            "y1": [0, 1, 2],   # identical to ideal y1
        })
        ideal_df = pd.DataFrame({
            "x": [0, 1, 2],
            "y1": [0, 1, 2],   # perfect match  -> SSE 0
            "y2": [5, 5, 5],   # poor match     -> high SSE
        })

        result = find_best_ideal_functions(training_df, ideal_df)

        self.assertEqual(
            result.loc[0, "best_ideal_function"], "y1",
            "the exact-match ideal function should be selected"
        )
        self.assertEqual(
            result.loc[0, "sum_of_squared_errors"], 0,
            "the SSE of an exact match should be zero"
        )


if __name__ == "__main__":
    unittest.main()