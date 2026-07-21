"""
Test point mapping functionality.
This module maps test data points to the selected ideal functions if their
deviation is within the allowed threshold defined by the assignment.
"""

from math import sqrt
import pandas as pd
import numpy as np

class TestDataMapper:
    """
    Map test data points to selected ideal functions.
    A test point is assigned to an ideal function if its deviation does not
    exceed the maximum training deviation multiplied by sqrt(2).
    """

    def calculate_allowed_deviation(self, max_absolute_deviation):
        """
        Calculate the maximum allowed deviation for a test point.
        max_absolute_deviation: largest deviation between training and ideal function.
        return: allowed deviation as a float.
        """
        return max_absolute_deviation * sqrt(2)

    def map_test_points(self, test_df, ideal_df, best_matches):
        """
        Map each test point to one of the four selected ideal functions.
        test_df: DataFrame containing the test points with columns x and y.
        ideal_df: DataFrame containing the x-values and ideal function y-values.
        best_matches: DataFrame containing the four selected ideal functions.
        return: DataFrame containing the successfully mapped test points.
        """
        mapped_points = []

        for _, test_row in test_df.iterrows():
            x_value = test_row["x"]
            test_y_value = test_row["y"]

            # use np.isclose instead of == because float x-values may not match exactly.
            matching_ideal_rows = ideal_df[np.isclose(ideal_df["x"], x_value)]

            # skip test points where no matching x-value exists in the ideal function.
            if matching_ideal_rows.empty:
                continue

            ideal_row = matching_ideal_rows.iloc[0]
            candidate_matches = []

            for _, match_row in best_matches.iterrows():
                training_function = match_row["training_function"]
                ideal_function = match_row["best_ideal_function"]
                max_absolute_deviation = match_row["max_absolute_deviation"]

                ideal_y_value = ideal_row[ideal_function]
                delta_y = test_y_value - ideal_y_value
                absolute_deviation = abs(delta_y)

                allowed_deviation = self.calculate_allowed_deviation(
                    max_absolute_deviation
                )
            
                # add to candidates if deviation is within the sqrt(2) threshold.
                if absolute_deviation <= allowed_deviation:
                    candidate_matches.append({
                        "x": x_value,
                        "y": test_y_value,
                        "training_function": training_function,
                        "ideal_function": ideal_function,
                        "ideal_function_number": int(
                            ideal_function.replace("y", "")
                        ),
                        "delta_y": delta_y,
                        "absolute_deviation": absolute_deviation,
                        "maximum_allowed_deviation": allowed_deviation
                    })

            # if multiple ideal functions qualify, pick the closest one. 
            if candidate_matches:
                best_candidate = min(
                    candidate_matches,
                    key=lambda candidate: candidate["absolute_deviation"]
                )
                mapped_points.append(best_candidate)

        result_df = pd.DataFrame(mapped_points)
        if result_df.empty:
            # Ensure all expected columns exist even when nothing maps.
            return pd.DataFrame(columns=[
                "x", "y", "training_function", "ideal_function",
                "ideal_function_number", "delta_y",
                "absolute_deviation", "maximum_allowed_deviation"
            ])
        return result_df