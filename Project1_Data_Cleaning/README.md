# Project 1: Data Cleaning & Preparation

## Objective
Clean a raw dataset by handling missing values, duplicates, and incorrect data formats to produce a production-ready "Gold Standard" dataset.

## Dataset Used
- **File:** `raw_dataset.csv`
- **Description:** [Describe your dataset here — e.g., "E-commerce orders data with 1000 rows and 8 columns"]
- **Source:** [Kaggle / Provided / Self-created]

## Steps Performed

### Phase 1: Strategic Imputation (Missing Values)
| Column | Missing Count | Strategy Used | Reason |
|--------|--------------|---------------|--------|
| e.g. Age | 45 | Median | Skewed distribution |
| e.g. Category | 12 | Mode | Categorical column |

### Phase 2: Integrity Audit (Duplicates)
- Total duplicate rows found: `X`
- Rows removed: `X`
- Method: `df.drop_duplicates()` / GROUP BY Order_ID HAVING COUNT(*) > 1

### Phase 3: Format Standardization
- Dates converted to: `YYYY-MM-DD` (ISO 8601)
- Text columns: Proper Case + whitespace trimmed
- Numeric columns: Rounded to 2 decimal places

## Results
| Metric | Before | After |
|--------|--------|-------|
| Total Rows | | |
| Missing Values | | 0 |
| Duplicate Rows | | 0 |
| Format Errors | | 0 |

## Files
- `raw_dataset.csv` — Original dataset
- `cleaned_dataset.csv` — Final cleaned output
- `data_cleaning.py` — Cleaning script
- `change_log.pdf` — Documented change log

## How to Run
```bash
pip install pandas
python data_cleaning.py
```
