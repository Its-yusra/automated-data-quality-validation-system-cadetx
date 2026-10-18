
import pandas as pd
import pytest

from module3_validate.validation_details import (
    identify_invalid_records,
    create_validation_summary
)


def sample_data():
    return pd.DataFrame({
        "encounter_id": [1, 2, 3],
        "patient_nbr": [101, 102, 103],
        "race": ["caucasian", "asian", "africanamerican"],
        "gender": ["female", "male", "female"],
        "age": ["[50-60)", "[40-50)", "[60-70)"],
        "time_in_hospital": [3, 4, 5],
        "readmitted": ["NO", "YES", "NO"]
    })


def test_invalid_numeric_record_detected():
    df = sample_data()
    df.loc[1, "time_in_hospital"] = 20

    invalid = identify_invalid_records(df)

    assert len(invalid) == 1
    assert invalid.iloc[0]["encounter_id"] == 2
    assert "time_in_hospital" in invalid.iloc[0]["validation_errors"]


def test_missing_value_record_detected():
    df = sample_data()
    df.loc[0, "race"] = None

    invalid = identify_invalid_records(df)

    assert 1 in invalid["encounter_id"].tolist()
    assert "Missing values" in invalid.loc[
        invalid["encounter_id"] == 1,
        "validation_errors"
    ].iloc[0]


def test_duplicate_records_detected():
    df = sample_data()
    df.loc[2] = df.loc[0]

    invalid = identify_invalid_records(df)

    assert len(invalid) == 2
    assert invalid["validation_errors"].str.contains(
        "Duplicate row"
    ).all()


def test_summary_counts():
    df = sample_data()
    df.loc[1, "time_in_hospital"] = 20

    invalid = identify_invalid_records(df)
    summary = create_validation_summary(df, invalid)

    assert summary["total_rows"] == 3
    assert summary["invalid_rows"] == 1
    assert summary["valid_rows"] == 2
    assert summary["validation_passed"] is False


def test_missing_required_column():
    df = sample_data().drop(columns=["gender"])

    with pytest.raises(ValueError):
        identify_invalid_records(df)
