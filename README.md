# Automated Data Quality & Validation System

## Project Domain
Healthcare

## Project Goal

The goal of this project is to develop an automated data-quality
gatekeeper that profiles, cleans, validates, and automates data
quality checks on healthcare datasets.

## Project Pipeline

Raw Dataset
→ Profile
→ Clean
→ Validate
→ Automate

## Selected Dataset

Diabetes 130-US Hospitals for Years 1999-2008

Source:
https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals+for+years+1999-2008

## Dataset Characteristics

- 101,766 records
- 47 features
- Healthcare domain
- Categorical and integer features
- Missing values
- Multiple data-quality issues suitable for profiling and cleaning

## Planned Outputs

- profiling_report.json
- cleaned_data.csv
- cleaning_log.json
- validation_report.json

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- PyYAML
- Pytest
- Git/GitHub
- Docker

## Current Progress

### Sprint 1
- Healthcare domain selected
- Healthcare dataset selected
- Project structure created
- Initial documentation prepared
- Initial dataset inspection script prepared

## Future Modules

### Module 1 — Profile
Dataset profiling and quality analysis.

### Module 2 — Clean
Missing values, duplicates, data-type and format cleaning.

### Module 3 — Validate
Rule-based validation and anomaly detection.

### Module 4 — Automate
End-to-end automated pipeline with configuration and Docker.

### Sprint 2
- Module 1 basic profiling implemented
- Dataset metadata analyzed
- Data types analyzed
- Missing values analyzed
- Unique values analyzed
- Duplicate records checked
- Numerical statistics generated
- `profiling_report.json` generated
- `basic_statistics.csv` generated

### Sprint 3
- Advanced data profiling implemented
- Missing-value analysis extended
- Missing-value heatmap generated
- Correlation heatmap generated
- Numerical distribution plots generated
- Potential outliers detected using IQR
- Suspicious columns identified
- Advanced profiling report generated

### Sprint 4 — Module 1 Completion

Sprint 4 completed the Profile module of the Automated Data Quality & Validation System.

Completed tasks:

* Finalized basic data profiling
* Finalized advanced data profiling
* Added missing-value analysis
* Added missing-value heatmap
* Added numerical distribution analysis
* Added correlation heatmap
* Added IQR-based outlier detection
* Added suspicious-column detection
* Added advanced profiling JSON report
* Added Module 1 documentation
* Added automated tests using pytest
* Verified Profile module functionality

### Module 1 Outputs

The Profile module generates:

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

### Testing

Tests can be executed from the project root using:

```bash
pytest
```

The tests verify:

* Missing-value analysis
* Outlier detection
* Suspicious-column detection
* Advanced profiling report generation

### Module 1 Status

**Completed**

The Profile module is now ready to provide data-quality information to the next stage of the system:


## Module 2 — Clean

The Clean module prepares the dataset for further validation.

### Current Cleaning Operations

* Schema inference
* Missing-value representation handling
* String whitespace cleaning
* Categorical normalization
* Numeric type conversion
* Duplicate detection and removal
* Cleaning activity logging

### Input

`data/raw/diabetic_data.csv`

### Outputs

`results/cleaned_data.csv`

`results/cleaning_log.json`

### Tests

Run the cleaning tests with:

```bash
pytest tests/test_clean.py -v
```

Run all project tests with:

```bash
pytest -v
```
### Sprint 6 — Missing Value Handling

Sprint 6 extends the Clean module with missing-value analysis and handling.

The system:

* Generates a missing-value report
* Calculates missing-value percentages
* Fills numerical missing values using the median
* Fills categorical missing values using the mode
* Saves the cleaned dataset
* Records the cleaning process

### Outputs

`results/missing_value_report.json`

`results/cleaned_data_v2.csv`

### Tests

Run Sprint 6 tests:

```bash
pytest tests/test_missing.py -v
```

Run all project tests:

```bash
pytest -v
```

