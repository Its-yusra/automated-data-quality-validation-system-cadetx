from pathlib import Path
import json
import pandas as pd


ORIGINAL_DATA_PATH = Path(
    "data/raw/diabetic_data.csv"
)

FINAL_DATA_PATH = Path(
    "results/final_cleaned_data.csv"
)

RESULTS_PATH = Path("results")

SUMMARY_PATH = (
    RESULTS_PATH / "final_cleaning_summary.json"
)


def calculate_dataset_summary(df):
    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "missing_values": int(
            df.isna().sum().sum()
        ),
        "duplicate_rows": int(
            df.duplicated().sum()
        ),
        "numeric_columns": int(
            len(
                df.select_dtypes(
                    include=["number"]
                ).columns
            )
        ),
        "categorical_columns": int(
            len(
                df.select_dtypes(
                    include=["object"]
                ).columns
            )
        )
    }


def create_summary():

    if not ORIGINAL_DATA_PATH.exists():

        raise FileNotFoundError(
            f"Original dataset not found: "
            f"{ORIGINAL_DATA_PATH}"
        )

    if not FINAL_DATA_PATH.exists():

        raise FileNotFoundError(
            f"Final cleaned dataset not found: "
            f"{FINAL_DATA_PATH}"
        )

    original_df = pd.read_csv(
        ORIGINAL_DATA_PATH
    )

    final_df = pd.read_csv(
        FINAL_DATA_PATH
    )

    original_summary = calculate_dataset_summary(
        original_df
    )

    final_summary = calculate_dataset_summary(
        final_df
    )

    summary = {
        "original_dataset": original_summary,
        "final_cleaned_dataset": final_summary,
        "changes": {
            "rows_removed": (
                original_summary["rows"]
                - final_summary["rows"]
            ),
            "columns_changed": (
                original_summary["columns"]
                - final_summary["columns"]
            ),
            "missing_values_remaining": (
                final_summary["missing_values"]
            ),
            "duplicate_rows_remaining": (
                final_summary["duplicate_rows"]
            )
        }
    }

    RESULTS_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        SUMMARY_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )

    return summary


def main():

    summary = create_summary()

    print(
        "Final cleaning summary generated successfully."
    )

    print(
        "Original rows:",
        summary["original_dataset"]["rows"]
    )

    print(
        "Final rows:",
        summary["final_cleaned_dataset"]["rows"]
    )

    print(
        "Rows removed:",
        summary["changes"]["rows_removed"]
    )

    print(
        "Missing values remaining:",
        summary["changes"][
            "missing_values_remaining"
        ]
    )

    print(
        "Duplicate rows remaining:",
        summary["changes"][
            "duplicate_rows_remaining"
        ]
    )

    print(
        f"Summary saved to: {SUMMARY_PATH}"
    )


if __name__ == "__main__":
    main()