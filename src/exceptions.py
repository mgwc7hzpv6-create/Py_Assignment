"""
Custom exception classes for the DLMDSPWP01 assignment.

This module defines exception types used to handle validation errors
in a controlled and assignment-specific way.
"""

class DataValidationError(Exception):
    """
    Raised when an input dataset does not match the expected structure.

    This custom exception is used for validation errors such as missing
    columns, inconsistent x-values or invalid dataset formats.
    """
    pass