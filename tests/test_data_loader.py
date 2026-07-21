"""
Unit tests for the data loader functionality.
"""

import unittest
import tempfile
import os
import pandas as pd
from src.data_loader import CSVDataLoader
from src.exceptions import DataValidationError


class UnitTestCSVDataLoader(unittest.TestCase):

    def test_missing_file_raises_file_not_found(self):
        """
        A non-existent path must raise the standard FileNotFoundError.
        """
        loader = CSVDataLoader("does_not_exist.csv")
        with self.assertRaises(FileNotFoundError):
            loader.load_csv(["x", "y"])

    def test_missing_columns_raises_validation_error(self):
        """
        A CSV without the required columns must raise DataValidationError.
        """
        # write a temporary CSV missing the 'y' column
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".csv", delete=False
        ) as temp_file:
            temp_file.write("x\n1\n2\n")
            temp_path = temp_file.name

        try:
            loader = CSVDataLoader(temp_path)
            with self.assertRaises(DataValidationError):
                loader.load_csv(["x", "y"])
        finally:
            os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()