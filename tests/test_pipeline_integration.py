
import json
from pathlib import Path

import pandas as pd
import yaml

from pipeline import run_pipeline


def test_end_to_end_pipeline(tmp_path):
    input_file = tmp_path / "input.csv"
    output_dir = tmp_path / "results"
    config_file = tmp_path / "config.yaml"

    df = pd.DataFrame({
        "encounter_id": [1, 2, 3],
        "patient_nbr": [101, 102, 103],
        "race": ["Caucasian", "Asian", "AfricanAmerican"],
        "gender": ["Female", "Male", "Female"],
        "age": ["[50-60)", "[40-50)", "[60-70)"],
        "time_in_hospital": [3, 5, 7],
        "readmitted": ["NO", "YES", "NO"]
    })
    df.to_csv(input_file, index=False)

    config = {
        "pipeline": {
            "name": "test-pipeline",
            "log_level": "INFO"
        },
        "cleaning": {
            "missing_values": ["?", "", " "],
            "normalize_strings": True,
            "remove_duplicates": True,
            "fill_numeric_missing": "median",
            "fill_categorical_missing": "mode"
        },
        "validation": {
            "required_columns": [
                "encounter_id",
                "patient_nbr",
                "race",
                "gender",
                "age",
                "time_in_hospital",
                "readmitted"
            ],
            "numeric_ranges": {
                "time_in_hospital": [1, 14]
            }
        }
    }

    config_file.write_text(
        yaml.safe_dump(config),
        encoding="utf-8"
    )

    report = run_pipeline(
        input_file, output_dir, config_file
    )

    assert report["profile"]["rows"] == 3
    assert report["cleaning"]["rows_after"] == 3
    assert report["validation"]["passed"] is True

    assert (output_dir / "profiling_report.json").exists()
    assert (output_dir / "cleaned_data.csv").exists()
    assert (output_dir / "validation_report.json").exists()
    assert (output_dir / "pipeline.log").exists()

    saved_report = json.loads(
        (output_dir / "validation_report.json").read_text(
            encoding="utf-8"
        )
    )
    assert saved_report["validation"]["passed"] is True


def test_pipeline_missing_input_fails(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text(
        yaml.safe_dump({
            "pipeline": {"log_level": "INFO"},
            "cleaning": {},
            "validation": {}
        }),
        encoding="utf-8"
    )

    missing_input = tmp_path / "missing.csv"

    try:
        run_pipeline(
            missing_input,
            tmp_path / "results",
            config_file
        )
    except FileNotFoundError:
        pass
    else:
        raise AssertionError(
            "Expected FileNotFoundError for missing input."
        )
