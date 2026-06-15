## Requirements

The project uses the following Python packages:

- pandas for loading and processing tabular CSV data
- SQLAlchemy for creating and writing to the SQLite database
- Bokeh for visualising the selected functions and mapped test data
- pytest for unit testing

# DLMDSPWP01 Python Assignment

This repository contains the Python implementation for the DLMDSPWP01 written assignment. The program loads the provided training, ideal function and test datasets, validates their structure and stores them in a local SQLite database.

In later stages, the implementation will select the four best-fitting ideal functions using the least squares method and map test data points to the selected functions based on the assignment's deviation criterion.

## Project Structure

```text
DLMDSPWP01_assignment/
├── data/
│   ├── train.csv
│   ├── ideal.csv
│   └── test.csv
├── src/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── data_loader.py
│   └── database.py
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

The project uses the following Python packages:

* pandas for loading and processing tabular CSV data
* SQLAlchemy for creating and writing to the SQLite database
* Bokeh for visualising the selected functions and mapped test data
* pytest for unit testing

Install the required Python packages with:

```bash
python -m pip install -r requirements.txt
```

## Current Workflow

The current workflow performs the following steps:

1. Loads the provided CSV datasets.
2. Validates the expected column structures.
3. Stores the validated datasets in a local SQLite database.
4. Creates the database tables `training_data`, `ideal_functions` and `test_data`.

## Running the Program

Place the provided CSV files in the `data/` folder and run:

```bash
python main.py
```

Expected output:

```text
Data loading and database storage completed successfully.
Training data shape: (400, 5)
Ideal functions data shape: (400, 51)
Test data shape: (100, 2)
Program completed without validation errors.
Program execution finished.
```
