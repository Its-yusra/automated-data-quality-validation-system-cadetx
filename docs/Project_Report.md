# Automated Data Quality Validation System
## Final Project Report — Module 4: Integration, Orchestration & Production Engineering

**Project Name:** Automated Data Quality Validation System  
**Module:** Module 4 — Integration, Orchestration & Production Engineering  
**Dataset:** Diabetes 130-US Hospitals Dataset  
**Programming Language:** Python  
**Libraries and Tools:** Pandas, NumPy, PyYAML, Pytest, Docker, DVC, Git LFS, Git  
**Project Repository:** Automated Data Quality Validation System  
**Status:** Core pipeline, Docker execution, and automated tests verified

---

## 1. Abstract

The Automated Data Quality Validation System is designed to improve the quality and reliability of structured datasets through automated profiling, data cleaning, and validation.

The project uses the Diabetes 130-US Hospitals dataset, containing 101,766 records and 50 columns. The system examines dataset characteristics, handles missing values, removes duplicate records when present, and checks whether the cleaned dataset meets configured quality rules.

Module 4 focuses on integrating the workflow into a command-line pipeline, supporting YAML-based configuration, maintaining logs, executing the pipeline through Docker, and testing the end-to-end process. DVC is used for dataset versioning, while Git LFS is configured for selected large-file formats.

The implemented pipeline completed successfully on the project dataset, and the validation report indicated that the configured validation checks passed.

## 2. Introduction

Data quality is an important requirement in data science, machine learning, healthcare analytics, and reporting. Datasets may contain missing values, duplicate records, inconsistent values, incorrect data types, and values outside expected ranges.

Manual data preparation can be repetitive and difficult to reproduce. An automated system can make the process more consistent by applying defined rules and generating reports.

This project provides a reusable workflow for profiling, cleaning, and validating a dataset through a single command.

## 3. Problem Statement

Raw datasets often contain quality issues that can affect analysis and machine learning results. Manually identifying and correcting these issues can require significant effort and may lead to inconsistent outcomes.

The objective of this project is to build an automated data quality system that processes a dataset, produces cleaning and validation outputs, records pipeline activity, and supports repeatable execution.

## 4. Project Objectives

The main objectives are:

- Profile the input dataset and summarize its structure and quality.
- Identify and handle missing values.
- Normalize string values and remove duplicate records when required.
- Validate required columns and configured numeric ranges.
- Generate machine-readable reports and cleaned data.
- Orchestrate profiling, cleaning, and validation through a CLI.
- Support YAML configuration.
- Record INFO, WARNING, and ERROR log messages.
- Execute the pipeline in a Docker container.
- Maintain dataset versioning through DVC and configure Git LFS for supported large files.
- Verify the workflow using automated unit and integration tests.
- Document the architecture, execution steps, and results.

## 5. Dataset Information

The project uses the Diabetes 130-US Hospitals dataset, commonly associated with encounters at US hospitals involving patients with diabetes.

**Dataset file:** `data/raw/diabetic_data.csv`

| Property | Value |
|---|---|
| Number of records | 101,766 |
| Number of columns | 50 |
| Duplicate rows reported | 0 |
| Data format | CSV |
| Domain | Healthcare |
| Main data types | Numeric and categorical |

The dataset includes fields such as `encounter_id`, `patient_nbr`, `race`, `gender`, `age`, `time_in_hospital`, and `readmitted`.

The original dataset contains missing-value indicators, including `?`, and missing data in multiple columns. Some fields, such as `weight`, `payer_code`, and `medical_specialty`, contain substantial missingness.

The dataset is used for data quality processing rather than for making clinical decisions.

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading, profiling, cleaning, and validation |
| NumPy | Numerical data operations |
| PyYAML | Reading pipeline configuration |
| Pytest | Automated testing |
| Docker | Containerized pipeline execution |
| DVC | Dataset versioning |
| Git | Source-code version control |
| Git LFS | Configuration for selected large files |
| JSON | Profiling, cleaning, and validation reports |
| CSV | Input dataset, cleaned data, and tabular outputs |
| Markdown | Project documentation |

## 7. System Architecture

The system follows a sequential data-processing architecture.

```text
             Input CSV Dataset
                     |
                     v
            Configuration Loader
                (config.yaml)
                     |
                     v
              Stage 1: Profiling
                     |
                     v
           Profiling Report (JSON)
                     |
                     v
               Stage 2: Cleaning
                     |
                     v
             Cleaned Dataset (CSV)
                     |
                     v
              Stage 3: Validation
                     |
                     v
           Validation Report (JSON)
                     |
                     v
             Pipeline Result and Logs
```

The command-line interface receives the input and output paths. Configuration values control the pipeline settings and validation rules. The pipeline records execution messages and produces reports that can be reviewed after processing.

Docker provides a containerized environment for running the pipeline. Pytest checks the behavior of the individual components and the end-to-end workflow.

## 8. Project Structure

The main project files and directories are organized as follows:

```text
automated-data-quality-validation-system-cadetx/
│
├── data/
│   └── raw/
│       ├── diabetic_data.csv
│       └── diabetic_data.csv.dvc
│
├── module1_profile/
│   └── Profiling components
│
├── module2_clean/
│   └── Cleaning components
│
├── module3_validate/
│   └── Validation components
│
├── module4_pipeline/
│   └── logging_config.py
│
├── results/
│   ├── profiling_report.json
│   ├── cleaned_data.csv
│   ├── validation_report.json
│   └── pipeline.log
│
├── tests/
│   └── test_pipeline_integration.py
│
├── docs/
│   ├── Dataset_Information.md
│   ├── Module_1_Profile_Documentation.md
│   ├── Project_Description.md
│   └── Project_Report.md
│
├── config.yaml
├── pipeline.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .gitattributes
└── README.md
```

This tree shows the principal project components. Additional files and test modules may also be present in the repository.

## 9. Implementation Methodology

### 9.1 Dataset Loading

The pipeline loads the CSV dataset from the path supplied through the command line. Missing-value indicators can be specified through the YAML configuration.

### 9.2 Data Profiling

The profiling stage examines the input dataset and produces a JSON report. Profiling helps identify:

- Dataset dimensions.
- Column names and data types.
- Missing values.
- Duplicate records.
- Basic statistical information.

The project also contains profiling components for additional summaries and visual analysis.

### 9.3 Data Cleaning

The cleaning stage prepares the dataset for validation. Configured operations include:

- Handling configured missing-value indicators.
- Normalizing string values.
- Filling numeric missing values using the configured median strategy.
- Filling categorical missing values using the configured mode strategy.
- Removing duplicate records when present.

The cleaned dataset is saved as a CSV file for downstream checks.

### 9.4 Data Validation

The validation stage checks whether the processed dataset meets the configured quality rules.

The YAML configuration defines required columns, including:

- `encounter_id`
- `patient_nbr`
- `race`
- `gender`
- `age`
- `time_in_hospital`
- `readmitted`

It also defines numeric ranges for selected columns, including length of hospital stay, laboratory procedures, medications, outpatient visits, emergency visits, inpatient visits, and number of diagnoses.

The validation report records the results of the configured checks and indicates whether validation passed.

### 9.5 YAML Configuration

The `config.yaml` file contains the pipeline name, log level, cleaning settings, required columns, and numeric validation ranges.

This separates configuration values from the pipeline's command-line execution and makes supported rules easier to maintain.

### 9.6 Logging

The logging configuration supports INFO, WARNING, and ERROR levels. Execution messages can be written to the console and a pipeline log file.

Logging helps identify the current processing stage, errors, and the final validation status.

### 9.7 Command-Line Interface

The pipeline supports command-line arguments for the input dataset, output directory, and optional configuration file.

The standard execution command is:

```powershell
python pipeline.py --input data/raw/diabetic_data.csv --output results/
```

To supply a configuration file explicitly:

```powershell
python pipeline.py --input data/raw/diabetic_data.csv --output results/ --config config.yaml
```

The pipeline runs the profiling, cleaning, and validation stages and saves its outputs in the selected output directory.

## 10. Docker Integration

Docker packages the pipeline and its Python dependencies into a containerized environment. This makes execution more reproducible across compatible systems.

### Build the Docker image

```powershell
docker build --load -t data-quality-pipeline .
```

### Run the pipeline in Docker

Run the following command from the project root:

```powershell
docker run --rm -v "${PWD}/data:/data" -v "${PWD}/results:/results" data-quality-pipeline --input /data/raw/diabetic_data.csv --output /results
```

The command mounts the local dataset directory and results directory into the container. The container reads the input dataset and writes generated outputs to the mounted results directory.

The Docker image built successfully, and the containerized pipeline completed with validation passing.

## 11. Testing and Quality Assurance

Automated testing was performed using Pytest.

Command:

```powershell
pytest -v
```

**Recorded test result:** 28 tests passed.

The test suite includes checks for data cleaning, cleaning quality, summaries, missing-value handling, profiling, validation, validation details, and end-to-end pipeline behavior.

Integration tests also check that the pipeline can process an input dataset and that a missing input file is handled as an error.

Six pandas warnings were reported during the recorded test run. They did not prevent the tests from passing.

### 11.1 End-to-End Verification

The pipeline was executed using the original dataset. It completed the profiling, cleaning, and validation stages and reported:

```text
Pipeline started.
Stage 1/3: Profiling
Stage 2/3: Cleaning
Stage 3/3: Validation
Validation passed: True
Pipeline completed.
```

The run also produced a pandas `DtypeWarning` concerning mixed types in the `payer_code` column. This warning did not prevent successful execution.

## 12. Results and Evaluation

The following results were obtained from the recorded pipeline run and validation report.

| Metric | Observed result |
|---|---:|
| Original records | 101,766 |
| Original columns | 50 |
| Duplicate rows in the input | 0 |
| Records in the cleaned dataset | 101,766 |
| Duplicate rows removed | 0 |
| Missing values in the validated cleaned output | 0 |
| Missing required columns | 0 |
| Configured numeric range checks with invalid values | 0 |
| Automated tests passed | 28 |
| Overall validation status | Passed |

### 12.1 Interpretation

The cleaned output retained all 101,766 records because the input contained no duplicate rows requiring removal. The validation report indicated that all required columns were present, the configured numeric range checks had no invalid values, and the cleaned output contained no missing values.

These results demonstrate that the implemented workflow completed successfully for the selected dataset and the configured quality rules. They do not imply that every possible data quality issue or clinical inconsistency has been detected.

## 13. Data Versioning

### 13.1 DVC

DVC is configured to track the raw dataset through:

`data/raw/diabetic_data.csv.dvc`

This allows the dataset reference and versioning metadata to be managed through Git while DVC manages the underlying data content.

The command below was used to check the DVC state:

```powershell
dvc status
```

The recorded result was:

```text
Data and pipelines are up to date.
```

This verifies that DVC reported no outstanding changes for the configured tracked data and pipelines at that time. A remote backup is not claimed unless a DVC remote is configured and the data has been pushed to it.

### 13.2 Git LFS

Git LFS is configured for selected large-file formats:

- `.keras`
- `.pth`
- `.mp4`

These patterns are recorded in `.gitattributes`. The raw CSV dataset is tracked using DVC rather than Git LFS to avoid managing the same file through both systems.

At the time of verification, `git lfs ls-files` returned no tracked LFS files. Therefore, the patterns were configured, but actual LFS file tracking still depends on adding matching files to Git after applying the relevant attributes.

## 14. Limitations

The current implementation has the following limitations:

1. The pipeline applies the rules defined in its configuration; it cannot automatically detect every domain-specific data issue.
2. Filling missing values with the median or mode may not always be suitable for every dataset or analytical objective.
3. The mixed-type `payer_code` column produces a pandas data-type warning during CSV loading.
4. Passing configured validation checks does not guarantee that all values are factually correct or clinically meaningful.
5. Git LFS patterns are configured, but no files were listed as LFS-tracked at the time of verification.
6. Cloud backup for DVC data is not claimed without a configured remote and successful data push.
7. The reported results apply to the tested dataset, configuration, and pipeline version.

## 15. Future Improvements

Potential improvements, if included in a later version, are:

- Improve handling and reporting of mixed data types.
- Add dataset-specific validation rules where required.
- Configure a DVC remote for off-machine data backup.
- Track suitable large model or demonstration files through Git LFS.
- Expand test coverage for additional edge cases.
- Improve documentation and reproducibility instructions as the project evolves.

These are possible future improvements and are not claimed as completed features.

## 16. Conclusion

The Automated Data Quality Validation System provides a command-line workflow for profiling, cleaning, and validating structured data. It uses YAML configuration, logging, Docker, DVC, Git, Git LFS configuration, and automated tests to support repeatable data preparation.

The pipeline was successfully executed on the Diabetes 130-US Hospitals dataset containing 101,766 records and 50 columns. The recorded validation report indicated that the cleaned output passed the configured checks, and the recorded automated test run completed with 28 passing tests.

The project demonstrates how data quality operations can be organized into a reproducible processing workflow with documented results and containerized execution.

## 17. References

1. UCI Machine Learning Repository — Diabetes 130-US Hospitals for Years 1999–2008.
2. Pandas documentation — https://pandas.pydata.org/docs/
3. Pytest documentation — https://docs.pytest.org/
4. Docker documentation — https://docs.docker.com/
5. DVC documentation — https://dvc.org/doc
6. Git LFS documentation — https://git-lfs.com/

---

**End of Report**
