from pathlib import Path
import json
import pandas as pd


DATA_PATH = Path("results/cleaned_data_v2.csv")
RESULTS_PATH = Path("results")

FINAL_DATA_PATH = RESULTS_PATH / "final_cleaned_data.csv"
QUALITY_REPORT_PATH = RESULTS_PATH / "cleaning_quality_report.json"


def check_missing_values(df):
    total_missing = int(df.isna().sum().sum())

    return {
        "total_missing_values": total_missing,
        "passed": total_missing == 0
    }


def check_duplicates(df):
    duplicate_count = int(df.duplicated().sum())

    return {
        "duplicate_rows": duplicate_count,
        "passed": duplicate_count == 0
    }


def check_numeric_ranges(df):
    checks = {}

    range_rules = {
        "time_in_hospital": (1, 14),
        "num_lab_procedures": (0, 200),
        "num_procedures": (0, 10),
        "num_medications": (0, 100),
        "number_outpatient": (0, 100),
        "number_emergency": (0, 100),
        "number_inpatient": (0, 100),
        "number_diagnoses": (1, 20)
    }

    for column, (minimum, maximum) in range_rules.items():

        if column not in df.columns:
            continue

        invalid_count = int(
            (
                (df[column] < minimum) |
                (df[column] > maximum)
            ).sum()
        )

        checks[column] = {
            "minimum_allowed": minimum,
            "maximum_allowed": maximum,
            "invalid_values": invalid_count,
            "passed": invalid_count == 0
        }

    return checks


def generate_quality_report(df):

    missing_check = check_missing_values(df)

    duplicate_check = check_duplicates(df)

    numeric_range_check = check_numeric_ranges(df)

    all_range_checks_passed = all(
        item["passed"]
        for item in numeric_range_check.values()
    )

    overall_passed = (
        missing_check["passed"]
        and duplicate_check["passed"]
        and all_range_checks_passed
    )

    return {
        "dataset_rows": int(len(df)),
        "dataset_columns": int(len(df.columns)),
        "missing_values_check": missing_check,
        "duplicate_check": duplicate_check,
        "numeric_range_check": numeric_range_check,
        "overall_quality_check_passed": overall_passed
    }


def save_report(report):

    RESULTS_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        QUALITY_REPORT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


def main():

    if not DATA_PATH.exists():

        print(
            f"Dataset not found: {DATA_PATH}"
        )

        return

    df = pd.read_csv(DATA_PATH)

    report = generate_quality_report(df)

    save_report(report)

    df.to_csv(
        FINAL_DATA_PATH,
        index=False
    )

    print("Cleaning quality validation completed.")

    print(
        f"Missing values: "
        f"{report['missing_values_check']['total_missing_values']}"
    )

    print(
        f"Duplicate rows: "
        f"{report['duplicate_check']['duplicate_rows']}"
    )

    print(
        f"Overall quality check passed: "
        f"{report['overall_quality_check_passed']}"
    )

    print(
        f"Quality report saved to: "
        f"{QUALITY_REPORT_PATH}"
    )

    print(
        f"Final cleaned dataset saved to: "
        f"{FINAL_DATA_PATH}"
    )


if __name__ == "__main__":
    main()