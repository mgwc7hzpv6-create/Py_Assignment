"""
Test point mapping functionality for the DLMDSPWP01 assignment.

This module maps test data points to the selected ideal functions if their
deviation is within the allowed threshold defined by the assignment.
"""

from math import sqrt

import pandas as pd


class TestDataMapper:
    """
    Map test data points to selected ideal functions.

    The mapper applies the assignment rule that a test point may be assigned
    to an ideal function if its deviation does not exceed the maximum training
    deviation multiplied by the square root of two.
    """

    def calculate_allowed_deviation(self, max_absolute_deviation):
        """
        Calculate the maximum allowed deviation for a test point.

        The assignment requires the maximum training deviation to be multiplied
        by the square root of two.

        Parameters
        ----------
        max_absolute_deviation : float
            The maximum absolute deviation between a training function and
            its selected ideal function.

        Returns
        -------
        float
            The allowed deviation for mapping a test point.
        """
        return max_absolute_deviation * sqrt(2)

    def map_test_points(self, test_df, ideal_df, best_matches):
        """
        Map test points to selected ideal functions.

        A test point is mapped to an ideal function if the absolute deviation
        between the test point y-value and the ideal function y-value is less
        than or equal to the allowed deviation.

        If more than one selected ideal function satisfies the condition, the
        function with the smallest absolute deviation is selected.

        Parameters
        ----------
        test_df : pandas.DataFrame
            DataFrame containing the test points with columns x and y.
        ideal_df : pandas.DataFrame
            DataFrame containing the x-values and ideal function values.
        best_matches : pandas.DataFrame
            DataFrame containing the selected ideal functions and their maximum
            absolute deviations.

        Returns
        -------
        pandas.DataFrame
            DataFrame containing the successfully mapped test points.
        """
        mapped_points = []

        for _, test_row in test_df.iterrows():
            x_value = test_row["x"]
            test_y_value = test_row["y"]

            matching_ideal_rows = ideal_df[ideal_df["x"] == x_value]

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

            if candidate_matches:
                best_candidate = min(
                    candidate_matches,
                    key=lambda candidate: candidate["absolute_deviation"]
                )
                mapped_points.append(best_candidate)

        return pd.DataFrame(mapped_points)