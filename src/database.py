"""
Database management.
This module contains the DatabaseManager class, which creates a SQLite
database connection and stores Pandas DataFrames as database tables.
"""
from sqlalchemy import create_engine

class DatabaseManager(object):
    """
    Manage the SQLite database connection and store datasets as tables.
    Creates a SQLAlchemy engine for a local SQLite database file.
    """

    def __init__(self, database_name="assignment.db"):
        """
        Initialise the database manager.
        database_name: name of the SQLite database file, defaults to assignment.db.
        """
        self.database_name = database_name
        self.engine = create_engine(f"sqlite:///{self.database_name}")

    def save_dataframe(self, dataframe, table_name):
        """
        Save a pandas DataFrame as a table in the SQLite database.
        dataframe: the dataset to store
        table_name: name of the target table.
        """
        # Replace the table if it already exists to avoid duplicate entries.
        dataframe.to_sql(
            name=table_name,
            con=self.engine,
            if_exists="replace",
            index=False
        )