
from pathlib import Path
import json

import pandas as pd

from module3_validate.validate_data import (
    DATA_PATH,
    REQUIRED_COLUMNS,
    NUMERIC_RULES
)

RESULTS_PATH = Path("results")

INVALID_RECORDS_PATH = RESULTS_PATH / "invalid_records.csv"
SUMMARY_PATH = RESULTS_PATH / "validation_summary.json"


def identify_invalid_records(df):
    """Return rows that fail one or more validation rules."""
    errors = pd.Series("", index=df.index, dtype="object")

    # Required columns must exist in the dataset.
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Required columns are missing: {missing_columns}"
        )

    # Flag rows containing missing values.
    missing_mask = df.isna().any(axis=1)
    errors.loc[missing_mask] += "Missing values; "

    # Flag rows with invalid numeric values.
    for column, (minimum, maximum) in NUMERIC_RULES.items():
        if column not in df.columns:
            continue

        values = pd.to_numeric(df[column], errors="coerce")

        invalid_mask = (
            values.notna()
            & ((values < minimum) | (values > maximum))
        )

        errors.loc[invalid_mask] += (
            f"{column} outside allowed range; "
        )

    # Flag every row belonging to a duplicate group.
    duplicate_mask = df.duplicated(keep=False)
    errors.loc[duplicate_mask] += "Duplicate row; "

    invalid_mask = errors.ne("")

    invalid_records = df.loc[invalid_mask].copy()
    invalid_records.insert(
        0,
        "source_row_index",
        df.index[invalid_mask]
    )
    invalid_records["validation_errors"] = (
        errors.loc[invalid_mask].str.rstrip("; ")
    )

    return invalid_records


def create_validation_summary(df, invalid_records):
    total_rows = len(df)
    invalid_rows = len(invalid_records)
    valid_rows = total_rows - invalid_rows

    error_counts = {
        "rows_with_missing_values": int(
            df.isna().any(axis=1).sum()
        ),
        "duplicate_rows": int(
            df.duplicated(keep=False).sum()
        ),
        "numeric_range_violations": {}
    }

    for column, (minimum, maximum) in NUMERIC_RULES.items():
        if column not in df.columns:
            continue

        values = pd.to_numeric(df[column], errors="coerce")
        invalid_mask = (
            values.notna()
            & ((values < minimum) | (values > maximum))
        )

        error_counts["numeric_range_violations"][column] = int(
            invalid_mask.sum()
        )

    return {
        "input_dataset": str(DATA_PATH),
        "total_rows": int(total_rows),
        "valid_rows": int(valid_rows),
        "invalid_rows": int(invalid_rows),
        "validation_passed": invalid_rows == 0,
        "error_counts": error_counts,
        "invalid_records_file": str(INVALID_RECORDS_PATH)
    }


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Input dataset not found: {DATA_PATH}. "
            "Complete Sprint 8 before running Sprint 10."
        )

    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    invalid_records = identify_invalid_records(df)

    invalid_records.to_csv(
        INVALID_RECORDS_PATH,
        index=False
    )

    summary = create_validation_summary(df, invalid_records)

    with open(SUMMARY_PATH, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("Sprint 10 validation reporting completed.")
    print(f"Total rows: {summary['total_rows']}")
    print(f"Valid rows: {summary['valid_rows']}")
    print(f"Invalid rows: {summary['invalid_rows']}")
    print(f"Validation passed: {summary['validation_passed']}")
    print(f"Invalid records: {INVALID_RECORDS_PATH}")
    print(f"Summary report: {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
