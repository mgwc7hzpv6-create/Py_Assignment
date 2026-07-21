"""
Unit tests for the test point mapping functionality.
"""
import unittest
from math import sqrt
import pandas as pd
from src.test_mapper import TestDataMapper

class UnitTestTestDataMapper(unittest.TestCase):

    def test_calculate_allowed_deviation(self):
        '''
        test that the sqrt(2) threshold rule is applied correctly.
        max deviation of 2 should give an allowed deviation of 2 * sqrt(2)
        '''
        test_mapper = TestDataMapper()

        result = test_mapper.calculate_allowed_deviation(2)

        self.assertEqual(result, 2 * sqrt(2), "allowed deviation should be 2 * sqrt(2)")

    def test_map_test_points_within_threshold(self):
        '''
        test that a point close enough to an ideal function gets mapped.
        test point y=2.0 matches ideal y=2.0 exactly so deviation is zero.
        '''
        # deviation is zero here so the point should always be mapped
        test_mapper = TestDataMapper()

        test_df = pd.DataFrame({"x": [1.0], "y": [2.0]})
        ideal_df = pd.DataFrame({"x": [1.0], "y1": [2.0]})
        best_matches = pd.DataFrame({
            "training_function": ["y1"],
            "best_ideal_function": ["y1"],
            "max_absolute_deviation": [1.0]
        })

        result = test_mapper.map_test_points(test_df, ideal_df, best_matches)

        self.assertEqual(len(result), 1, "one test point should be mapped")

    def test_map_test_points_outside_threshold(self):
        '''
        test that a point too far from all ideal functions is not mapped.
        test point y=100.0 is far from ideal y=2.0 so deviation is 98.
        '''
        # deviation of 98 is way above the allowed threshold of 1 * sqrt(2)
        test_mapper = TestDataMapper()

        test_df = pd.DataFrame({"x": [1.0], "y": [100.0]})
        ideal_df = pd.DataFrame({"x": [1.0], "y1": [2.0]})
        best_matches = pd.DataFrame({
            "training_function": ["y1"],
            "best_ideal_function": ["y1"],
            "max_absolute_deviation": [1.0]
        })

        result = test_mapper.map_test_points(test_df, ideal_df, best_matches)

        self.assertEqual(len(result), 0, "no test points should be mapped")


if __name__ == "__main__":
    unittest.main()