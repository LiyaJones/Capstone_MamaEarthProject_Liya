import pandas as pd
import matplotlib.pyplot as plt
import os

print("--- Generating Visualizations ---")

os.makedirs('visualizations', exist_ok=True)

# Load datasets for visualization
orders_df = pd.read_csv('data/orders.csv')
products_df = pd.read_csv('data/products.csv')
orders_clean = orders_df.drop_duplicates(subset=['order_id']).copy()
orders_clean['payment_method'] = orders_clean['payment_method'].str.upper().str.strip()
orders_clean['discount_pct'] = orders_clean['discount_pct'].fillna(0)
merged_df = orders_clean.merge(products_df, on='product_id', how='left')
merged_df['order_value'] = merged_df['quantity'] * merged_df['price'] * (1 - merged_df['discount_pct'] / 100.0)

# Chart 1: Return rate by payment method
payment_return_stats = merged_df.groupby('payment_method')['returned'].agg(['count', 'mean'])
payment_return_stats['return_rate_pct'] = (payment_return_stats['mean'] * 100).round(1)
payment_return_sorted = payment_return_stats.sort_values(by='return_rate_pct', ascending=False)

plt.figure(figsize=(7, 5))
bars = plt.bar(payment_return_sorted.index, payment_return_sorted['return_rate_pct'], color=['#C44E52', '#4C72B0', '#55A868'])
plt.title('COD Returns at 44.4% — Over 3x Higher Than Card', fontsize=12, fontweight='bold', pad=15)
plt.ylabel('Return Rate (%)', fontsize=10)
plt.xlabel('Payment Method', fontsize=10)
plt.ylim(0, 55)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height + 1.0, f"{height:.1f}%", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/return_rate_by_payment.png', dpi=300)
plt.close()

# Chart 2: Monthly revenue trend (outlier-corrected)
merged_df['order_date'] = pd.to_datetime(merged_df['order_date'])
q1 = merged_df['quantity'].quantile(0.25)
q3 = merged_df['quantity'].quantile(0.75)
iqr = q3 - q1
merged_df['is_outlier'] = (merged_df['quantity'] < (q1 - 1.5 * iqr)) | (merged_df['quantity'] > (q3 + 1.5 * iqr))

clean_time_df = merged_df[~merged_df['is_outlier']].copy()
clean_time_df['year_month'] = clean_time_df['order_date'].dt.to_period('M')
monthly_corrected = clean_time_df.groupby('year_month')['order_value'].sum()

peak_period = monthly_corrected.idxmax()
peak_rev = monthly_corrected.max()

plt.figure(figsize=(9, 4.5))
plt.plot(monthly_corrected.index.astype(str), monthly_corrected.values, marker='o', color='#2ca02c', linewidth=2.5, markersize=6)
plt.title(f'Outlier-Corrected Monthly Revenue Trend (Peak: {peak_period} at ₹{peak_rev:,.2f})', fontsize=12, fontweight='bold', pad=15)
plt.ylabel('Revenue (₹)', fontsize=10)
plt.xlabel('Month', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('visualizations/monthly_revenue_trend.png', dpi=300)
plt.close()

print("Visualizations saved successfully to visualizations/.")
