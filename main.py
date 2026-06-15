"""
Main execution module for the DLMDSPWP01 assignment.

This module coordinates the program workflow:
loading the provided CSV datasets, validating their structure,
storing them in a local SQLite database, selecting the best-fitting
ideal functions using the least squares method, mapping test points
to the selected ideal functions, and creating visualisations.
"""

from pathlib import Path

from src.data_loader import CSVDataLoader
from src.database import DatabaseManager
from src.exceptions import DataValidationError
from src.least_squares import find_best_ideal_functions
from src.test_mapper import TestDataMapper
from src.visualiser import Visualiser


def run_workflow():
    """
    Execute the assignment workflow.

    This workflow loads the training, ideal function and test datasets,
    validates their required columns, stores them in a SQLite database,
    identifies the best-fitting ideal functions for the training data,
    maps test points to the selected ideal functions, and creates Bokeh
    visualisations.
    """

    # Define the expected column structures for the input datasets.
    train_columns = ["x", "y1", "y2", "y3", "y4"]
    ideal_columns = ["x"] + [f"y{i}" for i in range(1, 51)]
    test_columns = ["x", "y"]

    # Load and validate the provided CSV datasets.
    train_data = CSVDataLoader("data/train.csv").load_csv(train_columns)
    ideal_data = CSVDataLoader("data/ideal.csv").load_csv(ideal_columns)
    test_data = CSVDataLoader("data/test.csv").load_csv(test_columns)

    # Store the validated datasets in the SQLite database.
    database = DatabaseManager("assignment.db")
    database.save_dataframe(train_data, "training_data")
    database.save_dataframe(ideal_data, "ideal_functions")
    database.save_dataframe(test_data, "test_data")

    # Identify the best-fitting ideal function for each training function.
    best_matches = find_best_ideal_functions(train_data, ideal_data)

    # Map test points to the selected ideal functions.
    test_mapper = TestDataMapper()
    mapped_test_points = test_mapper.map_test_points(
        test_data,
        ideal_data,
        best_matches
    )

    # Store the analytical results in the SQLite database.
    database.save_dataframe(best_matches, "best_matches")
    database.save_dataframe(mapped_test_points, "mapped_test_points")

    # Export the analytical results as CSV files for easier inspection.
    output_directory = Path("outputs")
    output_directory.mkdir(exist_ok=True)

    best_matches.to_csv(output_directory / "best_matches.csv", index=False)
    mapped_test_points.to_csv(
        output_directory / "mapped_test_points.csv",
        index=False
    )

    # Create Bokeh visualisations for the selected ideal functions.
    visualiser = Visualiser()

    for _, match_row in best_matches.iterrows():
        visualiser.plot_training_and_ideal_function(
            train_data=train_data,
            ideal_data=ideal_data,
            mapped_test_points=mapped_test_points,
            training_function=match_row["training_function"],
            ideal_function=match_row["best_ideal_function"]
        )

    print("Data loading and database storage completed successfully.")
    print(f"Training data shape: {train_data.shape}")
    print(f"Ideal functions data shape: {ideal_data.shape}")
    print(f"Test data shape: {test_data.shape}")

    print("\nBest-fitting ideal functions:")
    print(best_matches.to_string(index=False))

    print("\nMapped test points:")
    print(mapped_test_points.to_string(index=False))

    print("\nResults saved to:")
    print("SQLite table: best_matches")
    print("SQLite table: mapped_test_points")
    print("CSV file: outputs/best_matches.csv")
    print("CSV file: outputs/mapped_test_points.csv")
    print("Bokeh plots: outputs/plots")

    print(f"\nNumber of mapped test points: {len(mapped_test_points)}")


def main():
    """
    Run the workflow and handle expected exceptions.

    The try-except-else-finally structure follows the exception handling
    pattern introduced in the course material.
    """
    try:
        run_workflow()

    except FileNotFoundError as error:
        print(f"File error: {error}")

    except DataValidationError as error:
        print(f"Data validation error: {error}")

    else:
        print("Program completed without validation errors.")

    finally:
        print("Program execution finished.")


if __name__ == "__main__":
    main()