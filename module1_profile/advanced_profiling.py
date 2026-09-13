from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json


DATA_PATH = Path("data/raw/diabetic_data.csv")
RESULTS_PATH = Path("results")


def load_dataset():
    """Load the healthcare dataset."""
    return pd.read_csv(DATA_PATH)


def analyze_missing_values(df):
    """Analyze missing values in every column."""

    missing = df.isna().sum()
    missing_percentage = (missing / len(df)) * 100

    missing_table = pd.DataFrame({
        "missing_count": missing,
        "missing_percentage": missing_percentage.round(2)
    })

    missing_table = missing_table.sort_values(
        by="missing_percentage",
        ascending=False
    )

    return missing_table


def create_missing_heatmap(df):
    """Create missing-value heatmap."""

    plt.figure(figsize=(14, 8))

    sns.heatmap(
        df.isnull(),
        cbar=False,
        yticklabels=False
    )

    plt.title("Missing Values Heatmap")
    plt.xlabel("Columns")
    plt.ylabel("Records")

    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "missing_values_heatmap.png",
        dpi=150
    )

    plt.close()


def create_correlation_heatmap(df):
    """Create correlation heatmap for numerical columns."""

    numerical_df = df.select_dtypes(include="number")

    if numerical_df.shape[1] < 2:
        print("Not enough numerical columns for correlation heatmap.")
        return

    correlation = numerical_df.corr()

    plt.figure(figsize=(12, 8))

    sns.heatmap(
        correlation,
        annot=False,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Numerical Feature Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "correlation_heatmap.png",
        dpi=150
    )

    plt.close()


def create_distribution_plot(df):
    """Create distribution plots for numerical columns."""

    numerical_df = df.select_dtypes(include="number")

    if numerical_df.empty:
        print("No numerical columns available.")
        return

    numerical_df.hist(
        figsize=(14, 10),
        bins=20
    )

    plt.suptitle("Numerical Feature Distributions")

    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "distributions.png",
        dpi=150
    )

    plt.close()


def detect_outliers(df):
    """Detect potential outliers using the IQR method."""

    numerical_df = df.select_dtypes(include="number")

    outlier_summary = {}

    for column in numerical_df.columns:

        Q1 = numerical_df[column].quantile(0.25)
        Q3 = numerical_df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = (
            (numerical_df[column] < lower_bound) |
            (numerical_df[column] > upper_bound)
        ).sum()

        outlier_summary[column] = int(outliers)

    return outlier_summary


def identify_suspicious_columns(df):
    """Identify columns that may require additional quality checks."""

    suspicious_columns = []

    for column in df.columns:

        column_lower = column.lower()

        if any(keyword in column_lower for keyword in [
            "id",
            "number",
            "name",
            "email",
            "phone",
            "address"
        ]):
            suspicious_columns.append({
                "column": column,
                "reason": "Potential identifier or PII-like column"
            })

    return suspicious_columns


def main():

    RESULTS_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    print("Loading dataset...")

    df = load_dataset()

    print(f"Dataset shape: {df.shape}")

    # Missing-value analysis
    missing_table = analyze_missing_values(df)

    missing_table.to_csv(
        RESULTS_PATH / "missing_values_summary.csv"
    )

    # Visualizations
    print("Creating missing-value heatmap...")
    create_missing_heatmap(df)

    print("Creating correlation heatmap...")
    create_correlation_heatmap(df)

    print("Creating distribution plots...")
    create_distribution_plot(df)

    # Outlier detection
    print("Detecting potential outliers...")

    outliers = detect_outliers(df)

    outlier_table = pd.DataFrame(
        list(outliers.items()),
        columns=["column", "outlier_count"]
    )

    outlier_table.to_csv(
        RESULTS_PATH / "outlier_summary.csv",
        index=False
    )

    # Suspicious columns
    print("Checking suspicious columns...")

    suspicious_columns = identify_suspicious_columns(df)

    suspicious_table = pd.DataFrame(
        suspicious_columns
    )

    suspicious_table.to_csv(
        RESULTS_PATH / "suspicious_columns.csv",
        index=False
    )

    print("\nAdvanced profiling completed successfully.")

    print("\nGenerated files:")

    print("results/missing_values_summary.csv")
    print("results/missing_values_heatmap.png")
    print("results/correlation_heatmap.png")
    print("results/distributions.png")
    print("results/outlier_summary.csv")
    print("results/suspicious_columns.csv")


if __name__ == "__main__":
    main()
def create_advanced_report(df):
    """Create a summary of advanced profiling results."""

    missing = df.isna().sum()
    missing_percentage = (missing / len(df)) * 100

    numerical_df = df.select_dtypes(include="number")

    report = {
        "dataset_shape": {
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1])
        },

        "missing_values": {
            column: {
                "count": int(missing[column]),
                "percentage": round(
                    float(missing_percentage[column]),
                    2
                )
            }
            for column in df.columns
        },

        "numerical_columns": numerical_df.columns.tolist(),

        "categorical_columns": df.select_dtypes(
            include="object"
        ).columns.tolist(),

        "duplicate_rows": int(
            df.duplicated().sum()
        )
    }
    with open(
    RESULTS_PATH / "advanced_profiling_report.json",
    "w",
    encoding="utf-8"
    ) as file:
     json.dump(report, file, indent=4)
    

    return report
