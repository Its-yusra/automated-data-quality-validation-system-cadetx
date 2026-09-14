# Module 1 — Data Profiling Documentation

## 1. Module Overview

The Profile module is the first stage of the Automated Data Quality & Validation System.

Its purpose is to inspect the healthcare dataset and identify important data-quality characteristics before the data moves to the cleaning and validation stages.

The module performs basic and advanced data profiling, including dataset structure analysis, missing-value analysis, numerical statistics, distributions, correlations, outlier detection, and suspicious-column detection.

---

## 2. Input Dataset

The project uses the UCI Diabetes 130-US Hospitals dataset.

The dataset contains healthcare records collected from 130 US hospitals over a period of ten years.

Input file:

```text
data/raw/diabetic_data.csv
```

The dataset contains numerical and categorical columns and includes missing values.

---

## 3. Profile Module Workflow

The Profile module follows this workflow:

```text
Healthcare Dataset
       ↓
Load Dataset
       ↓
Basic Profiling
       ↓
Missing Value Analysis
       ↓
Statistical Analysis
       ↓
Distribution Analysis
       ↓
Correlation Analysis
       ↓
Outlier Detection
       ↓
Suspicious Column Detection
       ↓
Profiling Reports
```

---

## 4. Basic Profiling

The basic profiler collects:

* Number of rows
* Number of columns
* Column names
* Data types
* Missing-value counts
* Missing-value percentages
* Number of unique values
* Duplicate rows
* Numerical descriptive statistics

The basic profiling report is stored as:

```text
results/profiling_report.json
```

Basic numerical statistics are stored as:

```text
results/basic_statistics.csv
```

---

## 5. Missing-Value Analysis

The advanced profiler calculates:

* Missing-value count
* Missing-value percentage
* Missing values for every column

The summary is stored as:

```text
results/missing_values_summary.csv
```

A visualization is also generated:

```text
results/missing_values_heatmap.png
```

The dataset may contain missing-value placeholders such as `?`. These values are treated as missing values during profiling.

---

## 6. Distribution Analysis

Numerical columns are analyzed using distribution plots.

The distribution visualization helps identify:

* Data spread
* Skewed distributions
* Concentration of values
* Potential unusual values

Output:

```text
results/distributions.png
```

---

## 7. Correlation Analysis

The module calculates correlations between numerical features.

A correlation heatmap is generated to help identify relationships between numerical variables.

Output:

```text
results/correlation_heatmap.png
```

---

## 8. Outlier Detection

Potential numerical outliers are detected using the Interquartile Range (IQR) method.

The calculation uses:

```text
IQR = Q3 - Q1
```

Potential outliers are identified outside:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

The results are stored in:

```text
results/outlier_summary.csv
```

These values are treated as potential outliers and are not automatically removed during the Profile stage.

---

## 9. Suspicious Column Detection

The module checks column names for keywords that may indicate identifiers or potentially sensitive information.

The current keywords include:

* id
* number
* name
* email
* phone
* address

The results are stored in:

```text
results/suspicious_columns.csv
```

This is a heuristic check. A flagged column does not automatically mean that it contains personal information.

---

## 10. Advanced Profiling Report

The advanced profiling results are summarized in:

```text
results/advanced_profiling_report.json
```

The report contains:

* Dataset information
* Dataset dimensions
* Missing-value information
* Numerical columns
* Categorical columns
* Duplicate-row count
* Outlier detection method
* Suspicious-column detection rule

---

## 11. Main Functions

### `load_dataset()`

Loads the healthcare CSV dataset.

```python
def load_dataset():
    ...
```

### `analyze_missing_values(df)`

Calculates missing-value counts and percentages.

```python
def analyze_missing_values(df):
    ...
```

### `create_missing_heatmap(df)`

Creates a missing-value visualization.

```python
def create_missing_heatmap(df):
    ...
```

### `create_correlation_heatmap(df)`

Creates a numerical correlation heatmap.

```python
def create_correlation_heatmap(df):
    ...
```

### `create_distribution_plot(df)`

Creates numerical feature distribution plots.

```python
def create_distribution_plot(df):
    ...
```

### `detect_outliers(df)`

Detects potential numerical outliers using the IQR method.

```python
def detect_outliers(df):
    ...
```

### `identify_suspicious_columns(df)`

Identifies columns that may require additional quality or privacy checks.

```python
def identify_suspicious_columns(df):
    ...
```

### `create_advanced_report(df)`

Creates the final advanced profiling report.

```python
def create_advanced_report(df):
    ...
```

---

## 12. How to Run Module 1

Activate the project virtual environment:

```bash
venv\Scripts\activate
```

Run basic profiling:

```bash
python module1_profile/profiler.py
```

Run advanced profiling:

```bash
python module1_profile/advanced_profiling.py
```

The generated reports and visualizations are saved in:

```text
results/
```

---

## 13. Module 1 Outputs

The completed Profile module produces:

```text
results/
├── profiling_report.json
├── basic_statistics.csv
├── missing_values_summary.csv
├── missing_values_heatmap.png
├── correlation_heatmap.png
├── distributions.png
├── outlier_summary.csv
├── suspicious_columns.csv
└── advanced_profiling_report.json
```

---

## 14. Module 1 Completion

Module 1 provides the initial data-quality assessment required before cleaning and validation.

The output of this module will be used as a foundation for the next project stage:

**Module 2 — Clean**

The Profile module does not modify the original dataset. It only analyzes and reports its data-quality characteristics.
