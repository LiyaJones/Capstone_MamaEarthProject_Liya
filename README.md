# Mamaearth Returns & Growth Intelligence Pipeline

An end-to-end data analytics and GenAI-powered intelligence pipeline. This document details the exact execution steps required to reproduce every metric, database report, visualization, and automated executive narrative in this repository from top to bottom.

---

## 📁 Repository Structure
```text
Capstone_Project_Liya/
│
├── sql/
│   ├── schema.sql             # Database schema definition
│   ├── seed_data.sql          # Data ingestion and initial NULL/blank cleanups
│   └── reports.sql            # Core analytical report queries
│
├── data/
│   ├── raw_orders.csv         # Original raw operational dataset
│   └── cleaned_orders.csv     # Processed and deduplicated clean dataset
│
├── analysis/
│   ├── clean_and_eda.py       # Data hygiene, anomaly detection, and metrics export
│   └── visualize.py           # Operational charts and visual dashboards
│
├── narrator/
│   ├── findings.json          # Extracted JSON artifact containing verified core metrics
│   ├── generate_narrative.py  # GenAI script integrating Gemini API with robust offline fallback
│   └── insight_report.md      # Final automated executive insight report
│
└── README.md                  # Project reproduction guideStep-by-Step Reproduction Guide

Step-by-Step Reproduction Guide
1. Database Setup & SQL Execution (sql/)
To initialize the database environment and execute core queries:
   Load and execute sql/schema.sql to establish the required database tables and relational constraints.

   Load and execute sql/seed_data.sql to ingest the raw operational records and resolve initial blank strings and NULL anomalies.

   Run sql/reports.sql to execute the core analytical reports and verify base metrics.

2. Python Data Cleaning, EDA, and Metrics Export (analysis/)
To process the operational dataset programmatically and generate core analytical outputs:
   Run the data cleaning and exploratory data analysis script:
   python analysis/clean_and_eda.py

   Run the visualization script to generate operational charts:
   python analysis/visualize.py

Note: Task 5 of Part 2 within the analysis/clean_and_eda.py script automatically computes and writes narrator/findings.json, ensuring all downstream reporting utilizes code-driven, verified metrics without manual drift.

3. GenAI Insight Narrator (narrator/)
To compile the final executive report using narrator/generate_narrative.py, choose one of the following execution paths:
   Option A: Running with a Gemini API Key (Online Path)
   Set Gemini API key as an environment variable before running the script:
   export GEMINI_API_KEY="LJ_API_Key"
   python narrator/generate_narrative.py

   Option B: Running with No Key (Offline Fallback Path)
   If no API key is provided, the script gracefully catches the missing key and executes its automated offline fallback path, successfully compiling the structured template report:
   python narrator/generate_narrative.py

Upon successful execution of either path, the final generated report will be saved to narrator/insight_report.md.
