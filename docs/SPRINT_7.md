# Sprint 7 — Data Consistency and Cleaning Quality

## Objective

The objective of Sprint 7 is to verify the quality of the cleaned dataset before it is passed to the validation module.

The sprint adds automated quality checks for missing values, duplicate rows, and selected numeric ranges.

## Input

The input dataset is:

`results/cleaned_data_v2.csv`

This dataset is produced after the missing-value handling implemented in Sprint 6.

## Quality Checks

The following checks were implemented:

1. Missing-value check
2. Duplicate-row check
3. Numeric range check
4. Overall cleaning quality check

## Missing-Value Check

The system calculates the total number of missing values remaining in the dataset.

The check passes when no missing values remain.

## Duplicate Check

The system checks the cleaned dataset for duplicate rows.

The check passes when no duplicate rows remain.

## Numeric Range Check

Selected numerical columns are checked against defined valid ranges.

The system reports the number of values outside the configured range.

Invalid values are reported rather than automatically deleted.

## Quality Report

The cleaning quality results are saved as:

`results/cleaning_quality_report.json`

The report contains:

* Dataset row count
* Dataset column count
* Missing-value result
* Duplicate result
* Numeric range results
* Overall quality status

## Final Cleaned Dataset

After the quality checks are completed, the dataset is saved as:

`results/final_cleaned_data.csv`

The original raw dataset remains unchanged.

## Testing

Unit tests were created for:

* Missing-value checking
* Duplicate checking
* Numeric range checking
* Overall quality report generation

Tests are executed using pytest.

## Sprint 7 Deliverables

* Cleaning quality validation script
* Final cleaned dataset
* Cleaning quality report
* Unit tests
* Sprint documentation

## Status

Sprint 7 data consistency and cleaning quality checks implemented.
