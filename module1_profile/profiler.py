from pathlib import Path
import json
import pandas as pd


DATA_PATH = Path("data/raw/diabetic_data.csv")
OUTPUT_PATH = Path("results/profiling_report.json")


def profile_dataset(data_path=DATA_PATH, output_path=OUTPUT_PATH):

    # Create results folder if it does not exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load dataset
    df = pd.read_csv(data_path)

    # Dataset information
    report = {
        "dataset_name": "Diabetes 130-US Hospitals",
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_information": {},
        "duplicate_rows": int(df.duplicated().sum()),
    }

    # Analyze every column
    for column in df.columns:

        missing_count = int(df[column].isna().sum())

        missing_percentage = round(
            (missing_count / len(df)) * 100, 2
        )

        unique_count = int(
            df[column].nunique(dropna=True)
        )

        report["column_information"][column] = {
            "data_type": str(df[column].dtype),
            "missing_count": missing_count,
            "missing_percentage": missing_percentage,
            "unique_values": unique_count
        }

    # Numerical statistics
    numerical_df = df.select_dtypes(include="number")

    statistics = numerical_df.describe().round(2)

    # Add statistics to JSON report
    report["numerical_statistics"] = statistics.to_dict()

    # Save statistics as CSV
    statistics.to_csv("results/basic_statistics.csv")

    # Save JSON report
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("Profiling completed successfully.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(f"Report saved to: {output_path}")
    print("Statistics saved to: results/basic_statistics.csv")


if __name__ == "__main__":
    profile_dataset()