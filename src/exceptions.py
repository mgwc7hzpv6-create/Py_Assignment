"""
Custom exception classes.
This module defines exception types used to handle validation errors.
"""

class DataValidationError(Exception):
    """
    Custom exception for dataset validation errors.
    raises: when a dataset is missing columns or has an invalid format
    """
    pass