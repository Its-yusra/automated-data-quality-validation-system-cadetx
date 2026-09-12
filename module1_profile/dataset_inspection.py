from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw/diabetic_data.csv")


def inspect_dataset(path=DATA_PATH):
    df = pd.read_csv(path)

    print("\n--- DATASET SHAPE ---")
    print(df.shape)

    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- MISSING VALUES ---")
    print(df.isna().sum().sort_values(ascending=False).head(15))

    print("\n--- DUPLICATE ROWS ---")
    print(df.duplicated().sum())

    print("\n--- SAMPLE ROWS ---")
    print(df.head())

    return df


if __name__ == "__main__":
    inspect_dataset()