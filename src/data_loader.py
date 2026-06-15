"""
Data loading module for the DLMDSPWP01 assignment.

This module contains classes for loading CSV files, checking file
existence and validating required dataset columns.
"""

from pathlib import Path
import pandas as pd
from src.exceptions import DataValidationError


class BaseDataHandler:
    """
    Base class for handling input data files.

    The class stores the path to an input file and provides a reusable
    method for checking whether the file exists.
    """

    def __init__(self, file_path):
        """
        Initialise the data handler with a file path.

        Parameters:
            file_path (str): Path to the input file.
        """
        self.file_path = Path(file_path)

    def validate_file_exists(self):
        """
        Check whether the input file exists.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")


class CSVDataLoader(BaseDataHandler):
    """
    Load and validate CSV datasets.

    This class inherits file validation functionality from BaseDataHandler
    and extends it with CSV-specific loading and column validation.
    """

    def load_csv(self, expected_columns):
        """
        Load a CSV file into a pandas DataFrame and validate its columns.

        Parameters:
            expected_columns (list): Required column names for the dataset.

        Returns:
            pandas.DataFrame: Loaded and validated dataset.

        Raises:
            DataValidationError: If required columns are missing.
        """
        self.validate_file_exists()

        data = pd.read_csv(self.file_path)

        missing_columns = [
            column for column in expected_columns
            if column not in data.columns
        ]

        if missing_columns:
            # Raise a user-defined exception when the dataset does not
            # contain the columns required for the assignment workflow.
            raise DataValidationError(
                f"Missing required columns in {self.file_path.name}: "
                f"{missing_columns}"
            )

        return data