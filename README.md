# 🌍 API-Powered Travel Intelligence Tool

> A lightweight, robust Python CLI tool that fetches real-time country intelligence, demographic information, and geographic snapshots using the public REST Countries API.

---

## 📌 Features

- **Comprehensive Travel Snapshots**: Pulls capital city, official currency, formatted population metrics, regional details, official languages, and bordering neighbors.
- **Robust Error Handling**: Handles network timeouts, 404s (unknown countries), missing API payload fields, and invalid user inputs gracefully without crashing.
- **Externalized Configuration**: Loads API endpoints and connection timeouts from `config.py` with support for environment variables.
- **Flexible CLI Execution**: Accepts country queries either via command-line arguments or through an interactive CLI prompt.

---

## 📁 Repository Structure

```text
travel-intel-tool/
├── config.py              # Configuration & environment variable settings
├── env.example            # Sample environment configuration template
├── .gitignore             # Git ignore list for virtual environments & cache
├── requirements.txt       # Project dependencies
├── travel_intel.py        # Primary CLI application logic
├── obstacle_log.md        # Technical obstacle and resolution log
├── README.md              # Project documentation
└── sample_outputs/        # Stored execution outputs
    ├── india.txt
    ├── japan.txt
    └── invalid_country.txt
