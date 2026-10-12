
from pathlib import Path
import json
import pandas as pd

DATA_PATH = Path("results/final_cleaned_data.csv")
RESULTS_PATH = Path("results")
REPORT_PATH = RESULTS_PATH / "validation_report.json"

REQUIRED_COLUMNS = [
    "encounter_id",
    "patient_nbr",
    "race",
    "gender",
    "age",
    "time_in_hospital",
    "readmitted"
]

NUMERIC_RULES = {
    "time_in_hospital": (1, 14),
    "num_lab_procedures": (0, 200),
    "num_procedures": (0, 10),
    "num_medications": (0, 100),
    "number_outpatient": (0, 100),
    "number_emergency": (0, 100),
    "number_inpatient": (0, 100),
    "number_diagnoses": (1, 20)
}


def validate_required_columns(df):
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    return {
        "required_columns": REQUIRED_COLUMNS,
        "missing_columns": missing_columns,
        "passed": len(missing_columns) == 0
    }


def validate_missing_values(df):
    missing = {
        column: int(count)
        for column, count in df.isna().sum().items()
        if count > 0
    }

    return {
        "columns_with_missing_values": missing,
        "total_missing_values": int(df.isna().sum().sum()),
        "passed": len(missing) == 0
    }


def validate_duplicates(df):
    duplicate_count = int(df.duplicated().sum())

    return {
        "duplicate_rows": duplicate_count,
        "passed": duplicate_count == 0
    }


def validate_numeric_ranges(df):
    results = {}

    for column, (minimum, maximum) in NUMERIC_RULES.items():
        if column not in df.columns:
            continue

        values = pd.to_numeric(df[column], errors="coerce")

        invalid_mask = (
            values.notna()
            & ((values < minimum) | (values > maximum))
        )

        invalid_count = int(invalid_mask.sum())

        results[column] = {
            "minimum_allowed": minimum,
            "maximum_allowed": maximum,
            "invalid_values": invalid_count,
            "passed": invalid_count == 0
        }

    return results


def generate_validation_report(df):
    required = validate_required_columns(df)
    missing = validate_missing_values(df)
    duplicates = validate_duplicates(df)
    numeric = validate_numeric_ranges(df)

    numeric_passed = all(
        item["passed"] for item in numeric.values()
    )

    overall_passed = (
        required["passed"]
        and missing["passed"]
        and duplicates["passed"]
        and numeric_passed
    )

    return {
        "dataset_rows": int(len(df)),
        "dataset_columns": int(len(df.columns)),
        "required_columns_check": required,
        "missing_values_check": missing,
        "duplicate_check": duplicates,
        "numeric_range_checks": numeric,
        "overall_validation_passed": overall_passed
    }


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}. "
            "Complete Sprint 8 first."
        )

    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    report = generate_validation_report(df)

    with open(REPORT_PATH, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("Sprint 9 validation completed.")
    print(f"Dataset rows: {report['dataset_rows']}")
    print(f"Dataset columns: {report['dataset_columns']}")
    print(
        "Overall validation passed:",
        report["overall_validation_passed"]
    )
    print(f"Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
