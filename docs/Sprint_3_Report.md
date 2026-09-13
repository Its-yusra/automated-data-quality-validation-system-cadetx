# Sprint 3 Report

## Sprint 3 — Advanced Data Profiling

### 1. Sprint Goal

The goal of Sprint 3 was to extend Module 1 with advanced data profiling, visualization, outlier analysis, and identification of potentially suspicious columns.

### 2. Planned Tasks

* Analyze missing-value patterns.
* Generate a missing-value heatmap.
* Analyze numerical feature correlations.
* Generate a correlation heatmap.
* Generate numerical distribution plots.
* Detect potential numerical outliers.
* Identify potentially suspicious or identifier-like columns.
* Generate an advanced profiling summary.

### 3. Work Completed

Advanced profiling functionality was implemented using Python, Pandas, Matplotlib, and Seaborn.

The system now performs:

* Missing-value analysis
* Missing-value visualization
* Numerical correlation analysis
* Numerical distribution analysis
* IQR-based potential outlier detection
* Suspicious column identification
* Advanced profiling summary generation

### 4. Generated Outputs

The following outputs were generated:

* `missing_values_summary.csv`
* `missing_values_heatmap.png`
* `correlation_heatmap.png`
* `distributions.png`
* `outlier_summary.csv`
* `suspicious_columns.csv`
* `advanced_profiling_report.json`

### 5. Visualization Analysis

The missing-value heatmap provides a visual overview of missing data across the dataset.

The correlation heatmap provides information about relationships between numerical variables.

The distribution plots provide an overview of the distributions of numerical features.

### 6. Outlier Analysis

Potential numerical outliers were identified using the Interquartile Range (IQR) method.

These records are treated as potential anomalies rather than automatically incorrect records. Further validation will be performed in the validation module.

### 7. Suspicious Column Analysis

Column names were checked for terms that may indicate identifiers or PII-like information, such as ID, number, name, email, phone, or address.

### 8. Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

### 9. Sprint Outcome

Module 1 has been extended from basic profiling to advanced profiling and visualization. The system can now provide deeper information about missing data, numerical relationships, distributions, potential outliers, and suspicious columns.

### 10. Next Sprint

Sprint 4 will focus on completing Module 1, improving the profiling report, adding profiling rules and tests, and preparing Module 1 documentation before moving to Module 2 — Clean.
