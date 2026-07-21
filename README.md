# Project Overview

This repository contains the Python implementation for the DLMDSPWP01 written assignment. The program loads the provided training, ideal function and test datasets, validates their structure and stores them in a local SQLite database.

In later stages, the implementation will select the four best-fitting ideal functions using the least squares method and map test data points to the selected functions based on the assignment's deviation criterion.

# Project Structure

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

# Requirements

Python 3.10 or higher is required.

The project uses the following Python packages:

* pandas for loading and processing tabular CSV data
* sqlalchemy for creating and writing to the SQLite database
* numpy for numerical operations including least squares calculations
* bokeh for visualising the selected functions and mapped test data
* pytest for unit testing


# Installation

Install the required Python packages with:

```bash
python -m pip install -r requirements.txt
```

# Workflow

The current workflow performs the following steps:

1. Loads the three provided CSV datasets from the data folder.
2. Validates the expected column structures and in case of malformed input raises errors.
3. Stores the validated datasets in a local SQLite database (assignment.db).
4. Selects the four ideal functions that best fit the training data using the least squares criterion.
5. Loads test data and maps each point to one of the four chosen ideal functions, provided the deviation does not exceed the  maximum training deviation for that function multiplied by √2.
6. Saves the mapping results (x, y, delta y, ideal function number) to the database.
7. Generates Bokeh visualisations of the training data, chosen ideal functions, test points and their deviations, saved as an HTML file in the project root.
8. Creates the database tables `training_data`, `ideal_functions` and `test_data`.

# Running the Program

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
