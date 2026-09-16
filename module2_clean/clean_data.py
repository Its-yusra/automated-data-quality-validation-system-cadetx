from pathlib import Path
import json
import pandas as pd


# -----------------------------
# Paths
# -----------------------------

DATA_PATH = Path("data/raw/diabetic_data.csv")
RESULTS_PATH = Path("results")

CLEANED_DATA_PATH = RESULTS_PATH / "cleaned_data.csv"
CLEANING_LOG_PATH = RESULTS_PATH / "cleaning_log.json"


# -----------------------------
# Load dataset
# -----------------------------

def load_data():
    df = pd.read_csv(
        DATA_PATH,
        na_values=["?", "", " "]
    )
    return df


# -----------------------------
# Schema inference
# -----------------------------

def infer_schema(df):
    schema = {}

    for column in df.columns:
        schema[column] = {
            "dtype": str(df[column].dtype),
            "missing_values": int(df[column].isna().sum()),
            "unique_values": int(df[column].nunique(dropna=True))
        }

    return schema


# -----------------------------
# Clean strings
# -----------------------------

def clean_strings(df):
    string_columns = df.select_dtypes(include=["object"]).columns

    for column in string_columns:
        df[column] = df[column].apply(
            lambda x: x.strip() if isinstance(x, str) else x
        )

    return df


# -----------------------------
# Normalize categorical values
# -----------------------------

def normalize_categorical_values(df):
    string_columns = df.select_dtypes(include=["object"]).columns

    for column in string_columns:
        df[column] = df[column].apply(
            lambda x: x.lower() if isinstance(x, str) else x
        )

    return df


# -----------------------------
# Remove duplicate rows
# -----------------------------

def remove_duplicates(df):
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    removed = before - after

    return df, removed


# -----------------------------
# Basic numeric conversion
# -----------------------------

def normalize_numeric_columns(df):
    numeric_candidates = [
        "time_in_hospital",
        "num_lab_procedures",
        "num_procedures",
        "num_medications",
        "number_outpatient",
        "number_emergency",
        "number_inpatient",
        "number_diagnoses"
    ]

    converted_columns = []

    for column in numeric_candidates:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            converted_columns.append(column)

    return df, converted_columns


# -----------------------------
# Main cleaning process
# -----------------------------

def clean_dataset():

    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    df = load_data()

    original_rows = len(df)
    original_columns = len(df.columns)

    schema = infer_schema(df)

    # Missing values before cleaning
    missing_before = int(df.isna().sum().sum())

    # Clean strings
    df = clean_strings(df)

    # Normalize categorical values
    df = normalize_categorical_values(df)

    # Convert numeric columns
    df, converted_columns = normalize_numeric_columns(df)

    # Remove duplicates
    df, duplicates_removed = remove_duplicates(df)

    # Missing values after cleaning
    missing_after = int(df.isna().sum().sum())

    # Save cleaned dataset
    df.to_csv(CLEANED_DATA_PATH, index=False)

    # Cleaning log
    cleaning_log = {
        "dataset": str(DATA_PATH),
        "original_rows": original_rows,
        "original_columns": original_columns,
        "final_rows": len(df),
        "final_columns": len(df.columns),
        "missing_values_before": missing_before,
        "missing_values_after": missing_after,
        "duplicates_removed": duplicates_removed,
        "numeric_columns_converted": converted_columns,
        "string_values_stripped": True,
        "categorical_values_normalized_to_lowercase": True,
        "schema": schema
    }

    with open(CLEANING_LOG_PATH, "w", encoding="utf-8") as file:
        json.dump(
            cleaning_log,
            file,
            indent=4
        )

    print("Cleaning completed successfully.")
    print(f"Original rows: {original_rows}")
    print(f"Final rows: {len(df)}")
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Missing values before: {missing_before}")
    print(f"Missing values after: {missing_after}")
    print(f"Cleaned dataset saved to: {CLEANED_DATA_PATH}")
    print(f"Cleaning log saved to: {CLEANING_LOG_PATH}")


if __name__ == "__main__":
    clean_dataset()