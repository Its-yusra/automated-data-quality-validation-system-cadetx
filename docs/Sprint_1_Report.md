# Sprint 1 Report

## Sprint Goal

To establish the foundation of the Automated Data Quality &
Validation System by selecting the healthcare domain and dataset,
setting up the project repository and structure, and preparing
the initial project documentation.

## Planned Tasks

1. Select the project domain.
2. Select a suitable healthcare dataset.
3. Review the dataset characteristics.
4. Create the GitHub repository.
5. Create the project folder structure.
6. Prepare initial project documentation.
7. Prepare the initial dataset inspection script.

## Completed Work

### 1. Domain Selection

The Healthcare domain was selected for the project.

### 2. Dataset Selection

The Diabetes 130-US Hospitals for Years 1999-2008 dataset was
selected from the UCI Machine Learning Repository.

### 3. Dataset Review

The dataset contains 101,766 records and 47 features. It includes
categorical and integer data and contains missing values.

### 4. GitHub Repository

A GitHub repository was created for version control and project
development.

### 5. Project Structure

The following folders were created:

- data
- module1_profile
- module2_clean
- module3_validate
- module4_pipeline
- tests
- results
- docs

### 6. Initial Files

The following project files were prepared:

- README.md
- requirements.txt
- .gitignore
- Project_Description.md
- Dataset_Information.md
- dataset_inspection.py

### 7. Initial Dataset Inspection

An initial Python script was prepared to inspect:

- dataset shape
- column names
- data types
- missing values
- duplicate rows
- sample records

## Challenges

The healthcare dataset is relatively large, so the project will
use summarized profiling information rather than displaying the
complete dataset during analysis.

## Outcome

The foundation of the Automated Data Quality & Validation System
has been established. The repository and documentation are ready
for development of Module 1.

## Next Sprint

The next sprint will begin Module 1 — Profile.

Planned work:

- load the dataset
- extract metadata
- analyze data types
- calculate missing-value statistics
- analyze unique values
- identify suspicious columns
- start generating the profiling report