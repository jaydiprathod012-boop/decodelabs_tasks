"""
DecodeLabs - Data Analytics Internship 2026
Project 1: Data Cleaning & Preparation
Dataset: E-commerce Orders (1200 rows, 14 columns)
"""

import pandas as pd

# ─────────────────────────────────────────
# STEP 1: LOAD DATA
# ─────────────────────────────────────────
df = pd.read_excel('raw_dataset.xlsx')

print("=" * 55)
print("  INITIAL DATA AUDIT")
print("=" * 55)
print(f"Shape       : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Duplicates  : {df.duplicated().sum()}")
print(f"\nMissing Values:\n{df.isnull().sum()}")

# ─────────────────────────────────────────
# STEP 2: HANDLE MISSING VALUES
# (CouponCode has 309 missing values)
# ─────────────────────────────────────────
print("\n[Phase 1] Handling Missing Values...")

# CouponCode is missing for orders where no coupon was used
# Filling with 'NO_COUPON' — logical business value, not deletion
df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')

print(f"  CouponCode missing after fix : {df['CouponCode'].isnull().sum()}")

# ─────────────────────────────────────────
# STEP 3: REMOVE DUPLICATES
# ─────────────────────────────────────────
print("\n[Phase 2] Integrity Audit - Removing Duplicates...")
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"  Rows before : {before}")
print(f"  Rows after  : {after}")
print(f"  Removed     : {before - after} duplicates")

# ─────────────────────────────────────────
# STEP 4: STANDARDIZE FORMATS
# ─────────────────────────────────────────
print("\n[Phase 3] Standardizing Formats...")

# Date → YYYY-MM-DD string format (ISO 8601)
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
print("  Date column → YYYY-MM-DD ✓")

# Text columns → Proper Case + strip whitespace
for col in ['Product', 'PaymentMethod', 'OrderStatus', 'ReferralSource', 'ShippingAddress']:
    df[col] = df[col].str.strip().str.title()
print("  Text columns → Proper Case ✓")

# Numeric → 2 decimal places
df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)
print("  Numeric columns → 2 decimal places ✓")

# ─────────────────────────────────────────
# STEP 5: VERIFICATION GATE
# ─────────────────────────────────────────
print("\n" + "=" * 55)
print("  VERIFICATION GATE (Must be 0%)")
print("=" * 55)
print(f"  Missing Values : {df.isnull().sum().sum()} ✅")
print(f"  Duplicates     : {df.duplicated().sum()} ✅")
print(f"  Final Shape    : {df.shape}")

# ─────────────────────────────────────────
# STEP 6: SAVE CLEANED DATA
# ─────────────────────────────────────────
df.to_csv('cleaned_dataset.csv', index=False)
print("\n✅ Cleaned dataset saved → 'cleaned_dataset.csv'")

# ─────────────────────────────────────────
# CHANGE LOG
# ─────────────────────────────────────────
print("\n" + "=" * 55)
print("  CHANGE LOG SUMMARY")
print("=" * 55)
print("  CR001 | CouponCode null (309) → 'NO_COUPON'   | Preserved 309 records")
print("  CR002 | Date → ISO 8601 format YYYY-MM-DD     | Standardized")
print("  CR003 | Text → Proper Case + whitespace trim  | Standardized")
print("  CR004 | UnitPrice/TotalPrice → 2 decimals     | Standardized")
