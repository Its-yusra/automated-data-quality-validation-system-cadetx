# Sprint 8 — Module 2 Finalization

## Objective

The objective of Sprint 8 is to finalize the Clean module by generating a complete before-and-after cleaning summary and verifying the final cleaned dataset.

## Input

The original dataset is:

`data/raw/diabetic_data.csv`

The final dataset is:

`results/final_cleaned_data.csv`

## Final Cleaning Summary

A final summary is generated to compare the original and cleaned datasets.

The summary includes:

- Original row count
- Final row count
- Original column count
- Final column count
- Missing values
- Duplicate rows
- Numeric column count
- Categorical column count
- Rows removed during cleaning

## Output

The final cleaning summary is saved as:

`results/final_cleaning_summary.json`

The final cleaned dataset is:

`results/final_cleaned_data.csv`

## Module 2 Workflow

The complete cleaning workflow is:

1. Load the raw dataset.
2. Perform basic cleaning.
3. Handle missing values.
4. Validate cleaning quality.
5. Generate the final cleaned dataset.
6. Generate the final cleaning summary.

## Testing

Unit tests were added for the final cleaning summary functionality.

The complete project test suite was also executed using pytest.

## Data Integrity

The original raw dataset is not modified.

All cleaned outputs are saved separately in the results directory.

## Sprint 8 Deliverables

- Final cleaning summary script
- Final cleaning summary JSON
- Final cleaned dataset
- Unit tests
- Sprint documentation

## Module 2 Status

The Module 2 Clean workflow has been implemented through the current sprint and is ready to be used as the input for the validation stage.