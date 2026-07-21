"""
Data loading.
This module contains classes for loading CSV files, checking file
existence and validating required dataset columns.
"""

from pathlib import Path
import pandas as pd
from src.exceptions import DataValidationError

class BaseDataHandler (object):
    """
    Base class for handling input data files.
    Stores the file path and checks the file exists before loading.
    """

    def __init__(self, file_path):
        """
        Initialise the data handler with a file path.
        file_path: path to the input file.
        """
        self.file_path = Path(file_path)

    def validate_file_exists(self):
        """
        Check whether the input file exists.
        raises:FileNotFoundError: If the file does not exist.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

class CSVDataLoader(BaseDataHandler):
    """
    Load and validate CSV datasets.
    Inherits file path storage and existence validation from BaseDataHandler.
    """

    def __init__(self,file_path):
        """
        Initialise the CSV data loader.
        file path: path to the CSV file.
        """
        super().__init__(file_path)

    def load_csv(self, expected_columns):
        """
        Load a CSV file and validate its columns.
        expected_columns: list of required column names
        return: validated pandas DataFrame
        raises: DataValidationError if required columns are missing
        """
        self.validate_file_exists()

        data = pd.read_csv(self.file_path)

        missing_columns = [
            column for column in expected_columns
            if column not in data.columns
        ]

        if missing_columns:
            # Missing columns will cause errors later so raise here instead.
            raise DataValidationError(
                f"Missing required columns in {self.file_path.name}: "
                f"{missing_columns}"
            )

        return data
    
    def load_csv_line_by_line(self, expected_columns):          
        """
        Load a CSV file row by row using an generator.
        expected_columns: list of required column names.
        yields: one pandas series per row
        raises: DataValidationError: If required columns are missing.
        """
        self.validate_file_exists()

        data = pd.read_csv(self.file_path)

        missing_columns = [
            column for column in expected_columns
            if column not in data.columns
        ]

        if missing_columns:
            raise DataValidationError(
                f"Missing required columns in {self.file_path.name}: "
                f"{missing_columns}"
            )
        # underscore discards the row index since only the values are needed.
        for _, row in data.iterrows():
            yield row