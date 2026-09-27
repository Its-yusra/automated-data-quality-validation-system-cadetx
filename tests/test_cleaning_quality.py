import pandas as pd

from module2_clean.validate_cleaning import (
    check_missing_values,
    check_duplicates,
    check_numeric_ranges,
    generate_quality_report
)


def test_missing_values_check():

    df = pd.DataFrame({
        "age": [20, 30, 40]
    })

    result = check_missing_values(df)

    assert result["total_missing_values"] == 0
    assert result["passed"] is True


def test_duplicate_check():

    df = pd.DataFrame({
        "id": [1, 2, 3]
    })

    result = check_duplicates(df)

    assert result["duplicate_rows"] == 0
    assert result["passed"] is True


def test_numeric_range_check():

    df = pd.DataFrame({
        "time_in_hospital": [2, 5, 10]
    })

    result = check_numeric_ranges(df)

    assert result["time_in_hospital"]["invalid_values"] == 0
    assert result["time_in_hospital"]["passed"] is True


def test_quality_report():

    df = pd.DataFrame({
        "time_in_hospital": [2, 5, 10],
        "age": [20, 30, 40]
    })

    report = generate_quality_report(df)

    assert report["dataset_rows"] == 3
    assert report["dataset_columns"] == 2
    assert report["overall_quality_check_passed"] is True