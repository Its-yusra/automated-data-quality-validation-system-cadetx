import pandas as pd

from module2_clean.handle_missing import (
    generate_missing_value_report,
    fill_missing_values
)


def test_missing_value_report():

    df = pd.DataFrame({
        "age": [20, None, 30],
        "gender": ["male", "female", None]
    })

    report = generate_missing_value_report(df)

    assert report["age"]["missing_values"] == 1
    assert report["gender"]["missing_values"] == 1


def test_fill_missing_values():

    df = pd.DataFrame({
        "age": [20, None, 30],
        "gender": ["male", "female", None]
    })

    result, numerical, categorical = fill_missing_values(df)

    assert result["age"].isna().sum() == 0
    assert result["gender"].isna().sum() == 0

    assert "age" in numerical
    assert "gender" in categorical