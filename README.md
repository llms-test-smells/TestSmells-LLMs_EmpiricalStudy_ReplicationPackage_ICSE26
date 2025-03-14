# TestSmells-LLMs_EmpiricalStudy_ReplicationPackage

# Overview

This repository contains the resources and results from a study investigating the impact of refactoring performed by Large Language Models (LLMs) on test smells. The study involved evaluating various prompt templates for detecting and refactoring test smells, analyzing the outcomes, assessing the impact on code coverage metrics, and documenting the entire process.

## Repository Structure

### Prompt Templates

The `prompt templates` folder includes templates used in projects Python and Java:
- **10 templates** for **test smell detection**
- **10 templates** for **test smell refactoring**

These templates were used to guide the analysis and refactoring processes.

### Dataset

The `dataset` folder contains the URLs of the repositories used in this study. These repositories served as the basis for evaluating the effectiveness of the refactoring techniques.

### Results

The `results` folder stores the outcomes of the refactoring process, including:

- Changes in **code coverage metrics**.
- **Test smells** that were mitigated or introduced during refactoring.

### Source Code

The `src` folder includes the scripts used to:

- Send prompts to the models.
- Save and process the results.

Each script is accompanied by a dedicated `README` file with detailed instructions on how to execute the code.

## Usage

To replicate or extend this study, follow the instructions provided in the `README` files within each folder. Ensure all dependencies are installed and the dataset is properly configured before running the scripts.