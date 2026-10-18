
# Sprint 10 — Validation Reporting

## Objective
Identify invalid records and generate a validation summary
without modifying the source dataset.

## Input
`results/final_cleaned_data.csv`

## Validation Rules
- Required columns must exist.
- Rows with missing values are flagged.
- Numeric values are checked against configured ranges.
- Duplicate rows are flagged.

## Outputs
- `results/invalid_records.csv`
- `results/validation_summary.json`

## Tests
```bash
pytest tests/test_validation_details.py -v
pytest -v
```

## Expected Outcome
Invalid records are saved separately with their validation
errors, and a JSON report summarizes validation results.
