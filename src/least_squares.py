"""
Least squares functionality for selecting best-fitting ideal functions.

This module compares each training function with all available ideal functions
and selects the ideal function with the smallest sum of squared errors.
"""

import pandas as pd


def calculate_sum_of_squared_errors(actual_values, predicted_values):
    """
    Calculate the sum of squared errors between two series of values.

    Parameters
    ----------
    actual_values : pandas.Series
        The observed y-values from the training data.
    predicted_values : pandas.Series
        The corresponding y-values from an ideal function.

    Returns
    -------
    float
        The sum of squared errors.
    """
    errors = actual_values - predicted_values
    squared_errors = errors ** 2
    return squared_errors.sum()


def calculate_max_absolute_deviation(actual_values, predicted_values):
    """
    Calculate the largest absolute deviation between two functions.

    Parameters
    ----------
    actual_values : pandas.Series
        The observed y-values from the training data.
    predicted_values : pandas.Series
        The corresponding y-values from an ideal function.

    Returns
    -------
    float
        The maximum absolute deviation.
    """
    deviations = (actual_values - predicted_values).abs()
    return deviations.max()


def find_best_ideal_functions(training_df, ideal_df):
    """
    Find the best-fitting ideal function for each training function.

    The best-fitting ideal function is the one with the lowest sum of squared
    errors compared with the respective training function.

    Parameters
    ----------
    training_df : pandas.DataFrame
        DataFrame containing x-values and training y-values.
    ideal_df : pandas.DataFrame
        DataFrame containing x-values and ideal function y-values.

    Returns
    -------
    pandas.DataFrame
        A table containing the best ideal function for each training function.
    """
    training_y_columns = [column for column in training_df.columns if column.startswith("y")]
    ideal_y_columns = [column for column in ideal_df.columns if column.startswith("y")]

    results = []

    for training_column in training_y_columns:
        best_ideal_column = None
        lowest_sse = float("inf")
        best_max_deviation = None

        for ideal_column in ideal_y_columns:
            sse = calculate_sum_of_squared_errors(
                training_df[training_column],
                ideal_df[ideal_column]
            )

            if sse < lowest_sse:
                lowest_sse = sse
                best_ideal_column = ideal_column
                best_max_deviation = calculate_max_absolute_deviation(
                    training_df[training_column],
                    ideal_df[ideal_column]
                )

        mse = lowest_sse / len(training_df)
        rmse = mse ** 0.5

        results.append({
            "training_function": training_column,
            "best_ideal_function": best_ideal_column,
            "sum_of_squared_errors": lowest_sse,
            "mean_squared_error": mse,
            "root_mean_squared_error": rmse,
            "max_absolute_deviation": best_max_deviation
        })

    return pd.DataFrame(results)