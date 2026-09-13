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