# Sprint 6 — Module 2: Clean

## Objective

The objective of Sprint 6 is to extend the Clean module by analyzing and handling missing values in the cleaned healthcare dataset.

## Input Dataset

The input for this sprint is:

`results/cleaned_data.csv`

## Missing Value Analysis

A missing-value report was generated for every column.

The report contains:

* Missing-value count
* Missing-value percentage

The report is saved as:

`results/missing_value_report.json`

## Missing Value Handling

Two basic strategies were implemented.

### Numerical Columns

Missing values in numerical columns are replaced using the column median.

### Categorical Columns

Missing values in categorical columns are replaced using the most frequent value (mode).

These strategies are implemented through the cleaning module and are applied only when missing values are present.

## Output

The missing-value-cleaned dataset is saved as:

`results/cleaned_data_v2.csv`

## Testing

Unit tests were added for:

* Missing-value report generation
* Numerical missing-value handling
* Categorical missing-value handling

Tests are executed using pytest.

## Sprint 6 Deliverables

* Missing-value handling module
* Missing-value report
* Missing-value-cleaned dataset
* Unit tests
* Sprint documentation

## Status

Sprint 6 Module 2 missing-value analysis and handling completed.
