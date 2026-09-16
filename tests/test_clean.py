import pandas as pd

from module2_clean.clean_data import (
    clean_strings,
    normalize_categorical_values,
    normalize_numeric_columns,
    remove_duplicates
)


def test_clean_strings():

    df = pd.DataFrame({
        "name": [" Alice ", " Bob "]
    })

    result = clean_strings(df)

    assert result["name"].tolist() == ["Alice", "Bob"]


def test_normalize_categorical_values():

    df = pd.DataFrame({
        "gender": ["Male", "FEMALE", "Male"]
    })

    result = normalize_categorical_values(df)

    assert result["gender"].tolist() == [
        "male",
        "female",
        "male"
    ]


def test_numeric_conversion():

    df = pd.DataFrame({
        "time_in_hospital": ["3", "5", "7"]
    })

    result, columns = normalize_numeric_columns(df)

    assert pd.api.types.is_numeric_dtype(
        result["time_in_hospital"]
    )

    assert "time_in_hospital" in columns


def test_duplicate_removal():

    df = pd.DataFrame({
        "id": [1, 1, 2],
        "value": ["A", "A", "B"]
    })

    result, removed = remove_duplicates(df)

    assert len(result) == 2
    assert removed == 1