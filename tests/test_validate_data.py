
import pandas as pd

from module3_validate.validate_data import (
    validate_required_columns,
    validate_missing_values,
    validate_duplicates,
    validate_numeric_ranges,
    generate_validation_report
)


def test_required_columns_pass():
    df = pd.DataFrame({
        "encounter_id": [1],
        "patient_nbr": [10],
        "race": ["caucasian"],
        "gender": ["female"],
        "age": ["[50-60)"],
        "time_in_hospital": [3],
        "readmitted": ["NO"]
    })

    result = validate_required_columns(df)
    assert result["passed"] is True


def test_missing_values_detected():
    df = pd.DataFrame({"age": [20, None]})

    result = validate_missing_values(df)

    assert result["total_missing_values"] == 1
    assert result["passed"] is False


def test_duplicates_detected():
    df = pd.DataFrame({"id": [1, 1, 2]})

    result = validate_duplicates(df)

    assert result["duplicate_rows"] == 1
    assert result["passed"] is False


def test_numeric_range_detected():
    df = pd.DataFrame({
        "time_in_hospital": [3, 20]
    })

    result = validate_numeric_ranges(df)

    assert result["time_in_hospital"]["invalid_values"] == 1
    assert result["time_in_hospital"]["passed"] is False


def test_complete_validation_report():
    df = pd.DataFrame({
        "encounter_id": [1],
        "patient_nbr": [10],
        "race": ["caucasian"],
        "gender": ["female"],
        "age": ["[50-60)"],
        "time_in_hospital": [3],
        "readmitted": ["NO"]
    })

    report = generate_validation_report(df)

    assert report["dataset_rows"] == 1
    assert report["overall_validation_passed"] is True
