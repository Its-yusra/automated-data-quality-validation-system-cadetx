# Sprint 2 Report

## Sprint 2 — Basic Data Profiling

### 1. Sprint Goal

The goal of Sprint 2 was to begin Module 1 — Profile and perform basic data profiling on the selected healthcare dataset.

### 2. Planned Tasks

* Load the healthcare dataset.
* Identify dataset dimensions.
* Analyze column names and data types.
* Analyze missing values.
* Calculate unique values and cardinality.
* Check duplicate records.
* Generate basic numerical statistics.
* Generate the initial profiling report.

### 3. Work Completed

The selected healthcare dataset, Diabetes 130-US Hospitals for Years 1999-2008, was loaded using Python and Pandas.

The following profiling tasks were implemented:

* Dataset row and column count
* Column name extraction
* Data type identification
* Missing-value count
* Missing-value percentage
* Unique-value count
* Duplicate-row detection
* Numerical descriptive statistics

### 4. Profiling Output

The profiling process generates the following files:

* `results/profiling_report.json`
* `results/basic_statistics.csv`

The JSON report contains dataset-level information and column-level profiling information.

The CSV file contains descriptive statistics for numerical columns.

### 5. Technologies Used

* Python
* Pandas
* NumPy
* JSON

### 6. Files Created/Updated

```text
module1_profile/
└── profiler.py

results/
├── profiling_report.json
└── basic_statistics.csv

docs/
└── Sprint_2_Report.md
```

### 7. Challenges

The healthcare dataset contains a large number of records and columns. Therefore, the profiling process generates summarized information instead of displaying the complete dataset.

### 8. Sprint Outcome

Basic data profiling for Module 1 has been successfully implemented. The system can load the healthcare dataset, analyze its basic structure and data-quality characteristics, and generate a profiling report.

### 9. Next Sprint

Sprint 3 will extend Module 1 with advanced profiling and visual analysis, including:

* Missing-value visualization
* Correlation analysis
* Data distributions
* Outlier analysis
* Suspicious-column identification
* Possible PII/semantic column analysis
* Improved profiling report
