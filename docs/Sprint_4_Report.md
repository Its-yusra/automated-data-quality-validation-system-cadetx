# Sprint 4 Report

## Project

Automated Data Quality & Validation System

## Sprint

Sprint 4

## Module

Module 1 — Profile

## Sprint Goal

The goal of Sprint 4 was to finalize Module 1 of the Automated Data Quality & Validation System by completing the profiling documentation, final profiling report, automated tests, and project documentation.

---

## Completed Work

### 1. Advanced Profiling Finalization

The advanced profiling module was finalized to analyze the healthcare dataset.

The module performs:

* Missing-value analysis
* Numerical feature analysis
* Distribution analysis
* Correlation analysis
* Outlier detection
* Suspicious-column detection

---

### 2. Missing-Value Analysis

Missing-value counts and percentages are calculated for dataset columns.

A missing-value summary is generated as:

```text
results/missing_values_summary.csv
```

A missing-value heatmap is also generated:

```text
results/missing_values_heatmap.png
```

---

### 3. Statistical Analysis

Numerical columns are analyzed using descriptive statistics.

The existing statistical output is:

```text
results/basic_statistics.csv
```

---

### 4. Distribution Analysis

Distribution plots were generated for numerical features.

Output:

```text
results/distributions.png
```

These visualizations help identify the spread and distribution of numerical data.

---

### 5. Correlation Analysis

A correlation heatmap was generated for numerical features.

Output:

```text
results/correlation_heatmap.png
```

This helps identify relationships between numerical variables.

---

### 6. Outlier Detection

Potential numerical outliers were detected using the Interquartile Range (IQR) method.

Output:

```text
results/outlier_summary.csv
```

The Profile module reports potential outliers but does not remove them.

---

### 7. Suspicious Column Detection

A heuristic rule was implemented to identify column names that may represent identifiers or potentially sensitive information.

Output:

```text
results/suspicious_columns.csv
```

---

### 8. Advanced Profiling Report

A final JSON report was generated containing the main profiling results.

Output:

```text
results/advanced_profiling_report.json
```

---

### 9. Documentation

Module 1 documentation was created:

```text
docs/Module_1_Profile_Documentation.md
```

The documentation explains:

* Module purpose
* Input dataset
* Profiling workflow
* Analysis methods
* Functions
* Generated outputs
* Execution instructions

---

### 10. Automated Testing

Automated tests were added using pytest.

Test file:

```text
tests/test_profile.py
```

The tests cover:

* Missing-value analysis
* Outlier detection
* Suspicious-column detection
* Advanced profiling report generation

Tests are executed using:

```bash
pytest
```

---

## Final Module 1 Outputs

The Profile module now generates:

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

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Pytest
* JSON
* CSV

---

## Sprint Outcome

Sprint 4 successfully completed Module 1 — Profile.

The system can now inspect the healthcare dataset and produce structured profiling reports, statistical summaries, visualizations, potential outlier information, and suspicious-column information.

Automated tests were also added to verify the main profiling functions.

Module 1 is now ready to provide input for:

**Module 2 — Clean**

---

## Next Sprint

Sprint 5 will begin Module 2 — Clean.

Planned activities include:

* Schema inference
* Missing-value handling
* Duplicate detection
* Data-type normalization
* String normalization
* Date normalization
* Basic data cleaning
* Cleaning output generation
