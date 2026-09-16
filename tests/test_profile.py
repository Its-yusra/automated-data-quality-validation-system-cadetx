import pandas as pd

from module1_profile.advanced_profiling import (
    analyze_missing_values,
    detect_outliers,
    identify_suspicious_columns,
    create_advanced_report
)


def create_test_dataframe():
    return pd.DataFrame({
        "patient_id": [1, 2, 3, 4, 5],
        "age": [20, 30, 40, 50, 1000],
        "gender": ["Male", "Female", "Male", None, "Female"],
        "email": [
            "a@test.com",
            "b@test.com",
            None,
            "d@test.com",
            "e@test.com"
        ]
    })


def test_missing_value_analysis():
    df = create_test_dataframe()

    result = analyze_missing_values(df)

    assert "gender" in result.index
    assert result.loc["gender", "missing_count"] == 1


def test_outlier_detection():
    df = create_test_dataframe()

    result = detect_outliers(df)

    assert "age" in result
    assert result["age"] >= 1


def test_suspicious_column_detection():
    df = create_test_dataframe()

    result = identify_suspicious_columns(df)

    columns = [item["column"] for item in result]

    assert "patient_id" in columns
    assert "email" in columns


def test_advanced_report():
    df = create_test_dataframe()

    report = create_advanced_report(df)

    assert "dataset" in report
    assert "missing_values" in report
    assert "column_types" in report
    assert "duplicate_rows" in report

