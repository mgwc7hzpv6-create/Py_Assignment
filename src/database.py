"""
Database management module for the DLMDSPWP01 assignment.

This module contains the DatabaseManager class, which creates a SQLite
database connection and stores Pandas DataFrames as database tables.
"""

from sqlalchemy import create_engine


class DatabaseManager:
    """
    Manage the SQLite database connection and store datasets as tables.

    This class creates a SQLAlchemy engine for a local SQLite database
    and provides a method for saving pandas DataFrames as database tables.
    """

    def __init__(self, database_name="assignment.db"):
        """
        Initialise the database manager.

        Parameters:
            database_name (str): Name of the SQLite database file.
        """
        self.database_name = database_name
        self.engine = create_engine(f"sqlite:///{self.database_name}")

    def save_dataframe(self, dataframe, table_name):
        """
        Save a pandas DataFrame as a table in the SQLite database.

        If a table with the same name already exists, it is replaced.

        Parameters:
            dataframe (pandas.DataFrame): Dataset to be stored.
            table_name (str): Name of the target database table.
        """
        dataframe.to_sql(
            name=table_name,
            con=self.engine,
            if_exists="replace",
            index=False
        )