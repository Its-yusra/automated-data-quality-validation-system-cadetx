# Sprint 12 Report — Final Documentation, Verification & Submission

## 1. Sprint Overview

**Project Name:** Automated Data Quality Validation System — Healthcare Domain
**Sprint:** 12
**Project Track:** Data Engineering / Data Quality
**Dataset:** Diabetes 130-US Hospitals Dataset
**Primary Objective:** Finalize project documentation, verify the complete pipeline, prepare the presentation, and organize deliverables for submission.

## 2. Sprint Objectives

The objectives of Sprint 12 were to:

- Review and finalize project documentation.
- Verify the end-to-end profiling, cleaning, and validation pipeline.
- Confirm Docker execution and configuration files.
- Review data versioning using DVC and Git LFS.
- Verify automated tests and pipeline outputs.
- Prepare the final project presentation and demo materials.
- Organize deliverables for final submission.

## 3. Work Completed

### 3.1 Documentation

The project documentation was prepared and reviewed to describe the system architecture, modules, execution commands, configuration, testing, and results.

Key documentation files:

- `README.md` — Project overview and execution instructions.
- `docs/Project_Report.md` — Complete project report.
- `docs/SPRINT_11.md` — Previous sprint documentation.
- `docs/SPRINT_12.md` — Current sprint report.
- `docs/Presentation1.pptx` — Final project presentation.

### 3.2 End-to-End Pipeline Verification

The pipeline integrates three major stages:

1. **Profiling:** Examines dataset structure and data-quality indicators.
2. **Cleaning:** Handles configured missing values, normalizes strings, and removes duplicates according to the configuration.
3. **Validation:** Checks required columns and configured numeric ranges.

The pipeline can be executed using:

```bash
python pipeline.py --input data/raw/diabetic_data.csv --output results/
```

The verified run completed all three stages successfully, and the validation result was `True`.

### 3.3 Configuration and Logging

The `config.yaml` file defines the pipeline settings, missing-value markers, cleaning behavior, required columns, and numeric validation ranges.

The logging component records pipeline activity and relevant warnings to support troubleshooting and execution tracking.

### 3.4 Docker Verification

The Docker image was built successfully, and the containerized pipeline was executed successfully.

Build command:

```bash
docker build --load -t data-quality-pipeline .
```

Run command in PowerShell:

```powershell
docker run --rm -v "${PWD}/data:/data" -v "${PWD}/results:/results" data-quality-pipeline --input /data/raw/diabetic_data.csv --output /results
```

The containerized run completed with validation passing.

### 3.5 Data Versioning

**DVC:** The raw dataset is tracked through its `.dvc` metadata file. The previous DVC status check reported that data and pipelines were up to date.

**Git LFS:** The demo video at `demo/project_demo.mp4` is tracked using Git LFS. The tracking was verified through `git lfs ls-files`.

These tools support dataset and large-file management within the project.

### 3.6 Automated Testing

The project test suite was executed using:

```bash
pytest -v
```

**Verified result: 28 tests passed.**

Six pandas warnings were reported during the test run. These included a mixed-type warning associated with the `payer_code` column; the warning did not prevent the verified pipeline execution from completing.

### 3.7 Final Presentation and Demo

A revised 10-slide presentation was prepared covering:

- Problem statement and objectives.
- Dataset overview.
- System architecture.
- Profiling, cleaning, and validation.
- CLI, YAML configuration, and logging.
- Docker, DVC, and Git LFS.
- Automated testing and verified results.
- Conclusion and live-demo steps.

The demo video is maintained separately at `demo/project_demo.mp4`.

## 4. Dataset and Final Results

| Metric                                        |           Verified Result |
| --------------------------------------------- | ------------------------: |
| Dataset                                       | Diabetes 130-US Hospitals |
| Original rows                                 |                   101,766 |
| Dataset columns                               |                        50 |
| Duplicate rows reported                       |                         0 |
| Rows retained in the verified cleaned output  |                   101,766 |
| Missing values in the verified cleaned output |                         0 |
| Configured numeric range checks               |          0 invalid values |
| Pipeline validation                           |                    Passed |
| Automated tests                               |                 28 passed |

*Note: These results describe the verified project run and configured checks. They should not be interpreted as proof that every possible data-quality issue in the original dataset has been eliminated.*

## 5. Main Deliverables

The final project deliverables include:

- Python profiling, cleaning, and validation modules.
- End-to-end orchestration through `pipeline.py`.
- YAML configuration through `config.yaml`.
- Logging configuration.
- `requirements.txt` and `Dockerfile`.
- Automated integration tests.
- Profiling, cleaning, and validation reports in `results/`.
- DVC metadata for the raw dataset.
- Git LFS tracking for the demo video.
- Project README and detailed project report.
- Final PowerPoint presentation and demo video.

## 6. Challenges and Resolutions

### Mixed Data Types

The `payer_code` column can contain mixed data types, resulting in a pandas warning. The verified pipeline still completed successfully.

### Reproducible Execution

The project was tested both through the local CLI and in Docker, confirming that the configured workflow can execute in both environments.

### Large-File Management

DVC was used for the raw dataset, while Git LFS was configured and verified for the demo video.

## 7. Sprint Outcome

Sprint 12 consolidated the project documentation, verification results, presentation, and submission materials. The end-to-end pipeline and Docker execution were verified, and the automated test suite reported 28 passing tests.

The project now has documented instructions and a presentation suitable for demonstrating its principal workflow.

## 8. Final Submission Checklist

- [x] End-to-end pipeline verified.
- [x] YAML configuration checked.
- [x] Docker image built and container run verified.
- [x] Automated tests executed: 28 passed.
- [x] DVC dataset tracking checked.
- [x] Git LFS demo-video tracking verified.
- [x] Project report prepared.
- [x] Updated presentation prepared.
- [x] Confirm all final files are saved in the project directory.
- [x] Review `git status`, commit the intended final files, and push them to GitHub.
- [x] Perform a final review of the GitHub repository and submission materials.

## 9. Conclusion

Sprint 12 focused on final documentation, verification, and presentation readiness for the Automated Data Quality Validation System. The project demonstrates an integrated workflow for profiling, cleaning, and validating healthcare data, with configurable rules, logging, automated tests, Docker execution, and data-versioning tools.

The remaining submission tasks are to confirm the final files in the repository and complete the intended Git commit and push.

**Sprint Status:** Core pipeline and verification completed; final repository submission checks remain.
