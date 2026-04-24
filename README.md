# Demo Analytics App

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/demo-analytics-repo/security.yml?branch=main)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive Python CLI application demonstrating modern dependency management, Docker containerization, and DevSecOps GitHub Actions pipelines.

## Features
* **CLI Interface:** Built with `click`.
* **Data Validation:** Uses `pydantic` to validate external API calls (`requests`).
* **Analytics:** Uses `pandas` and `numpy`, visualized with `matplotlib`.
* **Security:** Simulates payload encryption with `cryptography` and manages secrets via `python-dotenv`.
* **DevSecOps Pipeline:** Automated SAST and SCA scanning via CodeQL, Semgrep, Picklescan, and Trivy.

## Local Setup

### 1. Prerequisites
* Python 3.10+
* Docker (Optional, for containerized execution)

### 2. Installation
Clone the repository and install the dependencies securely using PEP 621 standards:

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the application and its dependencies
pip install .