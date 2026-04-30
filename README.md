<<<<<<< HEAD
# 📊 E-Commerce Sales Dashboard

> **Resume Line:** E-Commerce Sales Dashboard — Power BI, Excel, Python (Pandas) — Apr 2026

An interactive sales analytics dashboard analyzing 12 months of e-commerce data across 5 regions, 6 categories, and 121,000+ orders.

**[🔗 Live Demo](https://your-username.github.io/ecommerce-dashboard)**

![Dashboard Preview](preview.png)

---

## 🛠 Tools & Technologies

| Tool | Usage |
|------|-------|
| **Python (Pandas, NumPy)** | Data cleaning, transformation, KPI calculations |
| **Chart.js** | Interactive charts (line, bar, donut, scatter) |
| **HTML/CSS/JavaScript** | Dashboard UI, filters, drill-down table |
| **Power BI Desktop** | `.pbix` file with DAX measures (see `/powerbi/`) |
| **Excel** | Raw dataset exploration and pivot tables |

---

## 📈 Dashboard Features

- **4 KPI Cards** — Total Revenue, Orders, Avg Order Value, Return Rate
- **Revenue Trend** — Monthly line chart (Jan–Dec 2024)
- **Regional Breakdown** — Donut chart across 5 regions
- **Category Performance** — Horizontal bar chart (6 categories)
- **Return Rate Analysis** — Bar chart by category with color-coded thresholds
- **Orders vs Revenue Scatter** — Category-level correlation view
- **Drill-down Table** — Revenue share bars, AOV, return rate per category
- **Interactive Filters** — Filter by Region and/or Category (live updates all charts)

---

## 🔢 DAX-Equivalent KPI Measures (Python)

```python
# Total Revenue
total_revenue = df["revenue"].sum()

# Average Order Value (equivalent to DAX DIVIDE)
avg_order_value = df["revenue"].sum() / df["orders"].sum()

# Return Rate %
df["return_rate"] = (df["returns"] / df["orders"]) * 100

# Net Revenue after returns
df["net_revenue"] = df["revenue"] - (df["returns"] * df["avg_order"])
```

In Power BI, these translate to DAX measures like:
```dax
Total Revenue = SUM(Sales[revenue])
AOV = DIVIDE(SUM(Sales[revenue]), SUM(Sales[orders]))
Return Rate % = DIVIDE(SUM(Sales[returns]), SUM(Sales[orders])) * 100
```

---

## 📁 Project Structure

```
ecommerce-dashboard/
├── index.html          ← Main dashboard (self-contained, works offline)
├── data_prep.py        ← Python data pipeline (Pandas)
├── README.md
└── processed/
    ├── monthly_trend.csv
    ├── category_performance.csv
    ├── regional_breakdown.csv
    ├── full_data.csv
    └── dashboard_data.json
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ecommerce-dashboard.git
cd ecommerce-dashboard

# 2. (Optional) Regenerate data from Python
pip install pandas numpy
python data_prep.py

# 3. Open dashboard in browser
open index.html   # Mac
start index.html  # Windows
```

No server needed — `index.html` is fully self-contained.

---

## 📊 Dataset

Based on the [E-Commerce Data (Kaggle)](https://www.kaggle.com/datasets/carrie1/ecommerce-data).  
Data was cleaned and aggregated using `data_prep.py`.

**Key stats:**
- 📅 Date range: Jan 2024 – Dec 2024
- 🌍 Regions: North America, Europe, Asia Pacific, Latin America, Middle East
- 🏷️ Categories: Electronics, Clothing, Home & Garden, Sports, Books, Beauty
- 💰 Total Revenue: $24.7M
- 📦 Total Orders: 121,655

---

## 👤 Author

**Your Name**  
[LinkedIn](https://linkedin.com/in/your-profile) · [GitHub](https://github.com/your-username)

*Built as part of a portfolio project — Apr 2026*
=======
# ecommerce-dashboard
Interactive e-commerce sales dashboard - Python, Chart.js
>>>>>>> 151e1a5ad0447268e8f35e1a68612ca062703b83
