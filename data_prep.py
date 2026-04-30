"""
E-Commerce Sales Data Preparation Script
=========================================
Author: Your Name
Date: April 2026
Tools: Python, Pandas, NumPy

This script:
1. Loads the raw e-commerce dataset (CSV from Kaggle)
2. Cleans and transforms the data
3. Exports summary CSVs for Power BI / the web dashboard

Dataset used: E-Commerce Sales Dataset (Kaggle)
https://www.kaggle.com/datasets/carrie1/ecommerce-data
"""

import pandas as pd
import numpy as np
import json
import os

# ------------------------------------------------------------------
# 1. GENERATE SAMPLE DATA (replace with: df = pd.read_csv('data.csv'))
# ------------------------------------------------------------------
np.random.seed(42)

categories   = ["Electronics", "Clothing", "Home & Garden", "Sports", "Books", "Beauty"]
regions      = ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East"]
months       = pd.date_range("2024-01-01", periods=12, freq="MS")

rows = []
for month in months:
    for region in regions:
        for cat in categories:
            revenue  = np.random.randint(15_000, 120_000)
            orders   = np.random.randint(80, 600)
            returns  = int(orders * np.random.uniform(0.03, 0.12))
            rows.append({
                "month":       month.strftime("%Y-%m"),
                "month_label": month.strftime("%b %Y"),
                "region":      region,
                "category":    cat,
                "revenue":     revenue,
                "orders":      orders,
                "returns":     returns,
                "avg_order":   round(revenue / orders, 2),
            })

df = pd.DataFrame(rows)

os.makedirs("processed", exist_ok=True)

# ------------------------------------------------------------------
# 2. CLEAN DATA
# ------------------------------------------------------------------
df.dropna(inplace=True)
df["net_revenue"] = df["revenue"] - (df["returns"] * df["avg_order"])
df["return_rate"] = (df["returns"] / df["orders"] * 100).round(2)

# ------------------------------------------------------------------
# 3. DAX-EQUIVALENT KPI CALCULATIONS (Python version)
# ------------------------------------------------------------------
total_revenue    = df["revenue"].sum()
total_orders     = df["orders"].sum()
avg_order_value  = (df["revenue"].sum() / df["orders"].sum()).round(2)
avg_return_rate  = df["return_rate"].mean().round(2)

print("=" * 45)
print("  KPI SUMMARY")
print("=" * 45)
print(f"  Total Revenue   : ${total_revenue:,.0f}")
print(f"  Total Orders    : {total_orders:,}")
print(f"  Avg Order Value : ${avg_order_value}")
print(f"  Avg Return Rate : {avg_return_rate}%")
print("=" * 45)

# ------------------------------------------------------------------
# 4. EXPORT SUMMARY TABLES
# ------------------------------------------------------------------

# Monthly trend
monthly = df.groupby("month_label").agg(
    revenue=("revenue", "sum"),
    orders=("orders", "sum"),
).reset_index()
monthly.to_csv("processed/monthly_trend.csv", index=False)

# Category performance
category = df.groupby("category").agg(
    revenue=("revenue", "sum"),
    orders=("orders", "sum"),
    return_rate=("return_rate", "mean"),
).reset_index()
category["return_rate"] = category["return_rate"].round(2)
category.to_csv("processed/category_performance.csv", index=False)

# Regional breakdown
regional = df.groupby("region").agg(
    revenue=("revenue", "sum"),
    orders=("orders", "sum"),
).reset_index()
regional.to_csv("processed/regional_breakdown.csv", index=False)

# Full dataset for dashboard
df.to_csv("processed/full_data.csv", index=False)

# Export as JSON for web dashboard
dashboard_data = {
    "kpis": {
        "total_revenue": int(total_revenue),
        "total_orders":  int(total_orders),
        "avg_order_value": float(avg_order_value),
        "avg_return_rate": float(avg_return_rate),
    },
    "monthly":   monthly.to_dict(orient="records"),
    "category":  category.to_dict(orient="records"),
    "regional":  regional.to_dict(orient="records"),
    "raw":       df.to_dict(orient="records"),
}

with open("processed/dashboard_data.json", "w") as f:
    json.dump(dashboard_data, f, indent=2)

print("\n✅ All files exported to /processed/")
print("   - monthly_trend.csv")
print("   - category_performance.csv")
print("   - regional_breakdown.csv")
print("   - full_data.csv")
print("   - dashboard_data.json  ← used by web dashboard")
