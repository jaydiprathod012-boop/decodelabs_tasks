"""
DecodeLabs - Data Analytics Internship 2026
Project 2: Exploratory Data Analysis (EDA)
Dataset: E-commerce Orders (1200 rows, 14 columns)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ─────────────────────────────────────────
# STEP 1: LOAD DATA
# ─────────────────────────────────────────
df = pd.read_excel('dataset.xlsx')
df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')

print("=" * 60)
print("  DATASET OVERVIEW")
print("=" * 60)
print(f"Shape  : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\nColumns: {list(df.columns)}")

# ─────────────────────────────────────────
# STEP 2: DESCRIPTIVE STATISTICS
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("  DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df[['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']].describe().round(2))

# ─────────────────────────────────────────
# STEP 3: CATEGORY ANALYSIS
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("  CATEGORY ANALYSIS")
print("=" * 60)
print("\nOrder Status Distribution:")
print(df['OrderStatus'].value_counts())
print("\nTop Products by Sales Count:")
print(df['Product'].value_counts())
print("\nPayment Methods:")
print(df['PaymentMethod'].value_counts())
print("\nReferral Sources:")
print(df['ReferralSource'].value_counts())

# ─────────────────────────────────────────
# STEP 4: OUTLIER DETECTION (IQR Method)
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("  OUTLIER DETECTION — IQR Method")
print("=" * 60)

for col in ['UnitPrice', 'TotalPrice', 'Quantity', 'ItemsInCart']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"  {col:15s}: {len(outliers)} outliers | Range: [{lower:.2f} – {upper:.2f}]")

# ─────────────────────────────────────────
# STEP 5: CORRELATION ANALYSIS
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("  CORRELATION MATRIX")
print("=" * 60)
corr = df[['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']].corr().round(2)
print(corr)

# ─────────────────────────────────────────
# STEP 6: VISUALIZATIONS
# ─────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('DecodeLabs EDA — E-commerce Orders Dataset', fontsize=14, fontweight='bold')

# Chart 1: Order Status
df['OrderStatus'].value_counts().plot(kind='bar', ax=axes[0,0], color='steelblue', edgecolor='white')
axes[0,0].set_title('Order Status Distribution')
axes[0,0].set_xlabel('')
axes[0,0].tick_params(axis='x', rotation=30)

# Chart 2: Product Sales
df['Product'].value_counts().plot(kind='barh', ax=axes[0,1], color='teal', edgecolor='white')
axes[0,1].set_title('Products by Order Count')

# Chart 3: TotalPrice Distribution
df['TotalPrice'].hist(bins=30, ax=axes[0,2], color='coral', edgecolor='white')
axes[0,2].set_title('TotalPrice Distribution (Right-Skewed?)')
axes[0,2].set_xlabel('Total Price')

# Chart 4: Payment Method
df['PaymentMethod'].value_counts().plot(kind='bar', ax=axes[1,0], color='mediumpurple', edgecolor='white')
axes[1,0].set_title('Payment Methods')
axes[1,0].tick_params(axis='x', rotation=30)

# Chart 5: Referral Source
df['ReferralSource'].value_counts().plot(kind='bar', ax=axes[1,1], color='gold', edgecolor='white')
axes[1,1].set_title('Referral Sources')
axes[1,1].tick_params(axis='x', rotation=30)

# Chart 6: Correlation Heatmap
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=axes[1,2], center=0)
axes[1,2].set_title('Correlation Heatmap')

plt.tight_layout()
plt.savefig('eda_charts.png', dpi=120)
plt.close()
print("\n✅ Charts saved → 'eda_charts.png'")

# ─────────────────────────────────────────
# STEP 7: KEY FINDINGS (The "So What?" Test)
# ─────────────────────────────────────────
total_revenue = df['TotalPrice'].sum()
avg_order     = df['TotalPrice'].mean()
top_product   = df['Product'].value_counts().idxmax()
top_payment   = df['PaymentMethod'].value_counts().idxmax()
cancelled_pct = round(df[df['OrderStatus']=='Cancelled'].shape[0] / len(df) * 100, 1)

print("\n" + "=" * 60)
print("  KEY FINDINGS SUMMARY")
print("=" * 60)
print(f"  Total Revenue        : ₹{total_revenue:,.2f}")
print(f"  Average Order Value  : ₹{avg_order:,.2f}")
print(f"  Top Product          : {top_product}")
print(f"  Top Payment Method   : {top_payment}")
print(f"  Cancellation Rate    : {cancelled_pct}%")
print(f"\n  Business Diagnosis:")
print(f"  → {cancelled_pct}% cancellation rate = revenue loss risk")
print(f"  → {top_product} is the best-selling product — prioritize stock")
print(f"  → {top_payment} is most used — ensure smooth payment gateway")
