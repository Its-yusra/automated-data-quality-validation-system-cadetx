
import argparse
import json
import logging
import sys
from pathlib import Path

import pandas as pd
import yaml

from module4_pipeline.logging_config import setup_logging


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def profile_data(df):
    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "missing_values": {
            str(column): int(count)
            for column, count in df.isna().sum().items()
        },
        "duplicate_rows": int(df.duplicated().sum()),
        "dtypes": {
            str(column): str(dtype)
            for column, dtype in df.dtypes.items()
        }
    }


def clean_data(df, settings):
    df = df.copy()

    missing_values = settings.get(
        "missing_values", ["?", "", " "]
    )

    # Convert configured missing-value markers to actual nulls.
    for marker in missing_values:
        df = df.replace(marker, pd.NA)

    # Remove leading/trailing whitespace from text.
    if settings.get("normalize_strings", True):
        for column in df.select_dtypes(
            include=["object", "string"]
        ).columns:
            df[column] = df[column].apply(
                lambda value: (
                    value.strip()
                    if isinstance(value, str)
                    else value
                )
            )

    # Remove duplicate records.
    duplicates_removed = 0
    if settings.get("remove_duplicates", True):
        before = len(df)
        df = df.drop_duplicates().copy()
        duplicates_removed = before - len(df)

    numeric_strategy = settings.get(
        "fill_numeric_missing", "median"
    )
    categorical_strategy = settings.get(
        "fill_categorical_missing", "mode"
    )

    # Fill missing numeric values.
    for column in df.select_dtypes(
        include=["number"]
    ).columns:
        if df[column].isna().any():
            if numeric_strategy == "median":
                fill_value = df[column].median()
            elif numeric_strategy == "mean":
                fill_value = df[column].mean()
            else:
                raise ValueError(
                    f"Unsupported numeric strategy: "
                    f"{numeric_strategy}"
                )

            if pd.notna(fill_value):
                df[column] = df[column].fillna(fill_value)

    # Fill missing categorical values.
    for column in df.select_dtypes(
        include=["object", "string", "category"]
    ).columns:
        if df[column].isna().any():
            if categorical_strategy != "mode":
                raise ValueError(
                    "Only mode is supported for categorical values."
                )

            modes = df[column].mode(dropna=True)
            if not modes.empty:
                df[column] = df[column].fillna(modes.iloc[0])

    return df, duplicates_removed


def validate_data(df, settings):
    required_columns = settings.get("required_columns", [])
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    missing_by_column = {
        str(column): int(count)
        for column, count in df.isna().sum().items()
        if count > 0
    }

    numeric_checks = {}
    for column, limits in settings.get(
        "numeric_ranges", {}
    ).items():
        if column not in df.columns:
            continue

        minimum, maximum = limits
        values = pd.to_numeric(df[column], errors="coerce")

        invalid_mask = (
            values.notna()
            & ((values < minimum) | (values > maximum))
        )

        numeric_checks[column] = {
            "minimum_allowed": minimum,
            "maximum_allowed": maximum,
            "invalid_values": int(invalid_mask.sum())
        }

    duplicate_count = int(df.duplicated().sum())
    total_missing = int(df.isna().sum().sum())

    passed = (
        not missing_columns
        and total_missing == 0
        and duplicate_count == 0
        and all(
            check["invalid_values"] == 0
            for check in numeric_checks.values()
        )
    )

    return {
        "passed": passed,
        "missing_required_columns": missing_columns,
        "total_missing_values": total_missing,
        "missing_values_by_column": missing_by_column,
        "duplicate_rows": duplicate_count,
        "numeric_range_checks": numeric_checks
    }


def run_pipeline(input_path, output_dir, config_path):
    config = load_config(config_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logging(
        output_dir,
        config.get("pipeline", {}).get("log_level", "INFO")
    )

    try:
        input_path = Path(input_path)

        if not input_path.exists():
            raise FileNotFoundError(
                f"Input dataset not found: {input_path}"
            )

        logger.info("Pipeline started.")
        logger.info("Loading input dataset: %s", input_path)

        df = pd.read_csv(
            input_path,
            na_values=config["cleaning"].get(
                "missing_values", ["?", "", " "]
            )
        )

        # Stage 1: Profile
        logger.info("Stage 1/3: Profiling")
        profile = profile_data(df)
        with open(
            output_dir / "profiling_report.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(profile, file, indent=4)

        # Stage 2: Clean
        logger.info("Stage 2/3: Cleaning")
        cleaned_df, duplicates_removed = clean_data(
            df, config["cleaning"]
        )
        cleaned_path = output_dir / "cleaned_data.csv"
        cleaned_df.to_csv(cleaned_path, index=False)

        # Stage 3: Validate
        logger.info("Stage 3/3: Validation")
        validation = validate_data(
            cleaned_df, config["validation"]
        )

        report = {
            "pipeline_name": config.get(
                "pipeline", {}
            ).get("name", "data-quality-pipeline"),
            "input_file": str(input_path),
            "profile": profile,
            "cleaning": {
                "rows_before": int(len(df)),
                "rows_after": int(len(cleaned_df)),
                "duplicates_removed": duplicates_removed,
                "output_file": str(cleaned_path)
            },
            "validation": validation
        }

        with open(
            output_dir / "validation_report.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(report, file, indent=4)

        logger.info("Cleaned dataset saved: %s", cleaned_path)
        logger.info(
            "Validation passed: %s", validation["passed"]
        )
        logger.info("Pipeline completed.")

        return report

    except Exception:
        logger.exception("Pipeline failed.")
        raise


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Profile, clean and validate a dataset "
            "with one command."
        )
    )
    parser.add_argument(
        "--input", required=True,
        help="Path to input CSV file"
    )
    parser.add_argument(
        "--output", required=True,
        help="Directory for generated reports and cleaned data"
    )
    parser.add_argument(
        "--config", default="config.yaml",
        help="YAML configuration path"
    )

    args = parser.parse_args()

    try:
        report = run_pipeline(
            args.input, args.output, args.config
        )
        return 0 if report["validation"]["passed"] else 1
    except Exception:
        return 1


if __name__ == "__main__":
    sys.exit(main())
