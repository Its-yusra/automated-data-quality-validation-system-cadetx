from pathlib import Path
import json
import pandas as pd


DATA_PATH = Path("results/cleaned_data.csv")
RESULTS_PATH = Path("results")

REPORT_PATH = RESULTS_PATH / "missing_value_report.json"
FINAL_DATA_PATH = RESULTS_PATH / "cleaned_data_v2.csv"


def generate_missing_value_report(df):
    report = {}

    for column in df.columns:
        missing_count = int(df[column].isna().sum())

        report[column] = {
            "missing_values": missing_count,
            "missing_percentage": round(
                (missing_count / len(df)) * 100, 2
            )
        }

    return report


def fill_missing_values(df):

    numerical_columns = df.select_dtypes(
        include=["number"]
    ).columns

    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    numerical_filled = []
    categorical_filled = []

    for column in numerical_columns:

        if df[column].isna().sum() > 0:

            median_value = df[column].median()

            df[column] = df[column].fillna(median_value)

            numerical_filled.append(column)

    for column in categorical_columns:

        if df[column].isna().sum() > 0:

            mode_values = df[column].mode()

            if not mode_values.empty:

                mode_value = mode_values.iloc[0]

                df[column] = df[column].fillna(mode_value)

                categorical_filled.append(column)

    return df, numerical_filled, categorical_filled


def save_missing_value_report(report):

    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    with open(REPORT_PATH, "w", encoding="utf-8") as file:

        json.dump(
            report,
            file,
            indent=4
        )


def main():

    if not DATA_PATH.exists():

        print("Cleaned dataset not found.")

        return

    df = pd.read_csv(DATA_PATH)

    missing_before = int(
        df.isna().sum().sum()
    )

    report_before = generate_missing_value_report(df)

    df, numerical_filled, categorical_filled = (
        fill_missing_values(df)
    )

    missing_after = int(
        df.isna().sum().sum()
    )

    report_after = generate_missing_value_report(df)

    df.to_csv(
        FINAL_DATA_PATH,
        index=False
    )

    report = {
        "missing_values_before": missing_before,
        "missing_values_after": missing_after,
        "numerical_columns_filled": numerical_filled,
        "categorical_columns_filled": categorical_filled,
        "before": report_before,
        "after": report_after
    }

    save_missing_value_report(report)

    print("Missing-value handling completed.")
    print(f"Missing before: {missing_before}")
    print(f"Missing after: {missing_after}")

    print(
        f"Numerical columns filled: "
        f"{len(numerical_filled)}"
    )

    print(
        f"Categorical columns filled: "
        f"{len(categorical_filled)}"
    )

    print(
        f"Final dataset saved to: "
        f"{FINAL_DATA_PATH}"
    )


if __name__ == "__main__":
    main()