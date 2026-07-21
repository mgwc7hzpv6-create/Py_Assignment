"""
Least squares selection of the best-fitting ideal functions.
Each training function is compared against all available ideal functions
and the one with the lowest sum of squared errors is selected.
"""

import pandas as pd

def calculate_sum_of_squared_errors(actual_values, predicted_values):
    """
    Calculate the sum of squared errors between two series of values.
    actual_values: observed y-values from the training data.
    predicted_values: corresponding y-values from an ideal function.
    return: sum of squared errors as a float.
    """
    errors = actual_values - predicted_values
    squared_errors = errors ** 2
    return squared_errors.sum()

def calculate_max_absolute_deviation(actual_values, predicted_values):
    """
    Calculate the largest absolute deviation between two functions.
    actual_values: observed y-values from the training data.
    predicted_values: corresponding y-values from an ideal function.
    return: maximum absolute deviation as a float.
    """
    deviations = (actual_values - predicted_values).abs()
    return deviations.max()


def find_best_ideal_functions(training_df, ideal_df):
    """
    Find the best-fitting ideal function for each training function.
    The best-fit is the ideal function with the lowest sum of squared errors.
    training_df: DataFrame containing x-values and training y-values.
    ideal_df: DataFrame containing x-values and ideal function y-values.
    return: DataFrame with the best ideal function for each training function.
    """
    training_y_columns = [column for column in training_df.columns if column.startswith("y")]
    ideal_y_columns = [column for column in ideal_df.columns if column.startswith("y")]
    results = []

    for training_column in training_y_columns:
        best_ideal_column = None
        lowest_sse = float("inf") # start high so any real SSE will replace it
        best_max_deviation = None

        for ideal_column in ideal_y_columns:
            sse = calculate_sum_of_squared_errors(
                training_df[training_column],
                ideal_df[ideal_column]
            )

            # Keep track of ideal function with the lowest SSE so far.
            if sse < lowest_sse:
                lowest_sse = sse
                best_ideal_column = ideal_column
                best_max_deviation = calculate_max_absolute_deviation(
                    training_df[training_column],
                    ideal_df[ideal_column]
                )
        
        # additional error metrics for reporting purposes
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