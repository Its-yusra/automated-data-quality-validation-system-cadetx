import pandas as pd

from module2_clean.cleaning_summary import (
    calculate_dataset_summary
)


def test_dataset_summary():

    df = pd.DataFrame({
        "age": [20, 30, 40],
        "gender": [
            "male",
            "female",
            "male"
        ]
    })

    summary = calculate_dataset_summary(df)

    assert summary["rows"] == 3
    assert summary["columns"] == 2
    assert summary["missing_values"] == 0
    assert summary["duplicate_rows"] == 0


def test_dataset_summary_with_missing_value():

    df = pd.DataFrame({
        "age": [20, None, 40],
        "gender": [
            "male",
            "female",
            "male"
        ]
    })

    summary = calculate_dataset_summary(df)

    assert summary["missing_values"] == 1