# Sprint 5 — Module 2: Clean

## Objective

The objective of Sprint 5 is to start the Clean module of the Automated Data Quality and Validation System.

The module prepares the healthcare dataset for further validation by applying basic and consistent data-cleaning operations.

## Dataset

Dataset: UCI Diabetes 130-US Hospitals Dataset

Input file:

`data/raw/diabetic_data.csv`

## Cleaning Tasks

The following cleaning operations were implemented:

1. Missing-value representation handling
2. Schema inference
3. String whitespace cleaning
4. Categorical value normalization
5. Numeric column conversion
6. Duplicate row detection and removal
7. Cleaning activity logging

## Input

The cleaning module reads:

`data/raw/diabetic_data.csv`

The `?` values are interpreted as missing values.

## Output

The module generates:

`results/cleaned_data.csv`

and

`results/cleaning_log.json`

## Schema Inference

The cleaning process records:

* Column data type
* Number of missing values
* Number of unique values

## String Cleaning

Leading and trailing whitespace is removed from string values.

## Categorical Normalization

String-based categorical values are normalized to lowercase to improve consistency.

## Numeric Normalization

Selected numeric columns are converted to numeric data types using safe conversion.

## Duplicate Handling

Duplicate rows are detected and removed.

The number of removed duplicate rows is recorded in the cleaning log.

## Cleaning Log

The cleaning log records:

* Original number of rows
* Original number of columns
* Final number of rows
* Final number of columns
* Missing values before cleaning
* Missing values after cleaning
* Number of duplicates removed
* Numeric columns converted
* Cleaning operations performed

## Testing

Unit tests were created for:

* String cleaning
* Categorical normalization
* Numeric conversion
* Duplicate removal

Tests are executed using pytest.

## Sprint 5 Deliverables

* Module 2 cleaning script
* Cleaned dataset
* Cleaning log
* Unit tests
* Sprint 5 documentation

## Status

Sprint 5 Module 2 basic cleaning implementation completed.
