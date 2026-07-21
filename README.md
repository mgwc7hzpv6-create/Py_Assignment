# DLMDSPWP01 – Ideal Function Selection

The program loads the provided training, ideal-function and test datasets, validates their structure,and stores them in a local SQLite database. It then selects the four best-fitting
ideal functions for the training data using the least squares criterion, maps the test points to those functions under the assignment's deviation threshold, and visualises the results.

## Project Structure

```text
DLMDSPWP01_assignment/
├── data/
│   ├── [train.csv]
│   ├── [ideal.csv]
│   └── [test.csv]
├── src/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── data_loader.py
│   ├── database.py
│   ├── least_squares.py
│   ├── test_mapper.py
│   └── visualiser.py
├── tests/
│   ├── test_data_loader.py
│   ├── test_least_squares.py
│   └── test_test_mapper.py
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

Python 3.10 or higher. The project depends on:

* pandas – loading and processing the tabular CSV data
* numpy – tolerance-based numerical comparison of x-values
* sqlalchemy – creating and writing to the SQLite database
* bokeh – visualising the functions and mapped test points
* pytest – unit tests

Install them with:

```bash
python -m pip install -r requirements.txt
```

## Running the Program

Place the provided CSV files in the `data/` folder and run:

```bash
python main.py
```

The program loads and validates the three datasets, stores them in the SQLite database, selects the best-fitting ideal function for each of the four training
functions, maps the test points, writes the results back to the database, and generates the Bokeh plots (in the `outputs/` folder).

## Database

Running the program creates a local SQLite database (`assignment.db`) containing the training data, the ideal functions, the mapped test results, the raw test
data, and a summary table of the selected best-fitting functions.

## Tests

Run the unit tests with:

```bash
pytest
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
