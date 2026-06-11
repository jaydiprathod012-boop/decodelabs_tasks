# Project 2: Exploratory Data Analysis (EDA)

## Objective
Analyze a dataset to uncover hidden patterns, trends, distributions, and outliers — turning raw numbers into actionable business insights.

## Dataset Used
- **File:** `dataset.csv`
- **Description:** [Describe your dataset — e.g., "Retail sales data with 5000 rows across 10 columns"]
- **Source:** [Kaggle / Provided / Self-created]
- **Why this dataset?** [Explain why it's business-relevant — avoid "Hello World" datasets like Titanic/Iris]

## Analysis Performed

### 1. Descriptive Statistics
- Mean, Median, Std, Min, Max for all numeric columns
- Value counts for categorical columns

### 2. Distribution Analysis
- Identified symmetrical vs skewed distributions
- Used histograms to visualize data shape

### 3. Outlier Detection
- **Method Used:** IQR Method / Z-Score Method
- **Outliers Found:** [List columns and outlier counts]
- **Decision:** Noise (removed) or Signal (investigated)

### 4. Correlation Analysis
- Pearson Correlation Coefficient used
- Key correlations found: [e.g., "Strong positive correlation (r=0.82) between X and Y"]
- Note: Correlation ≠ Causation — checked for confounding variables

## Key Findings (The "So What?" Test)

| What the Data Says | Business Diagnosis |
|--------------------|--------------------|
| [Stat finding 1] | [Business impact 1] |
| [Stat finding 2] | [Business impact 2] |
| [Stat finding 3] | [Business impact 3] |

## Files
- `dataset.csv` — Dataset used for analysis
- `eda_analysis.py` — EDA script
- `eda_report.pdf` — Executive summary report

## How to Run
```bash
pip install pandas matplotlib seaborn
python eda_analysis.py
```
