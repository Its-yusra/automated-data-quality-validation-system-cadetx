
# Sprint 9 — Data Validation Rules

## Objective
Implement automated validation checks for the cleaned healthcare dataset.

## Validation Checks
- Required columns
- Missing values
- Duplicate rows
- Numeric value ranges

## Input
`results/final_cleaned_data.csv`

## Output
`results/validation_report.json`

## Testing
Run the validation tests:

```bash
pytest tests/test_validate_data.py -v
```

Run the complete test suite:

```bash
pytest -v
```

## Expected Outcome
The system generates a JSON validation report containing
individual check results and an overall pass/fail status.
