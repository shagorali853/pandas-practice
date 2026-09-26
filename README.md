<div align="center">

# 🐼 Pandas Practice

### A Structured, Hands-On Journey from Pandas Fundamentals to Machine Learning Data Preparation

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Learning%20%26%20Practice-orange)]()
[![Focus](https://img.shields.io/badge/Focus-Data%20Science%20%7C%20ML-success)]()

**Learn Pandas by practicing, analyzing datasets, and building a strong foundation for Data Science and Machine Learning.**

</div>

---

## 📌 About This Repository

Welcome to **`pandas-practice`** — my structured learning and coding repository for **Pandas**, the Python library widely used for data manipulation and analysis.

This repository organizes Pandas into **16 essential topics**, progressing from core concepts and data cleaning to exploratory data analysis (EDA), feature engineering, performance, and machine learning data preparation.

### 🎯 Repository Goals

- Build a strong foundation in Pandas and tabular data manipulation.
- Practice essential Pandas methods with clear, reproducible examples.
- Learn to inspect, clean, transform, and analyze real-world datasets.
- Perform EDA and extract useful insights from data.
- Prepare clean, reliable datasets for Machine Learning workflows.
- Document my learning progress and practical exercises.

> **Learning approach:** Understand the concept → write code → practice with data → apply it to a mini-project.

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing and array operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Interactive learning and experimentation |
| Scikit-learn | ML data preparation and modeling workflows |

---

## 🗺️ Pandas Learning Roadmap

The repository is organized into the following 16 main topics.

| # | Topic | Priority |
|---:|---|---|
| 01 | Pandas Fundamentals | 🔥 Essential |
| 02 | Data Loading & Export | 🔥 Essential |
| 03 | Data Inspection & Understanding | 🔥 Essential |
| 04 | Data Selection — `loc` & `iloc` | 🔥 Essential |
| 05 | Data Cleaning — Missing Values | 🔥 Essential |
| 06 | Duplicates, Data Types & Text Cleaning | 🔥 Essential |
| 07 | Data Manipulation | 🔥 Essential |
| 08 | GroupBy & Aggregation | 🔥 Essential |
| 09 | Merge, Join & Concat | 🔥 Essential |
| 10 | Reshaping — Pivot & Melt | ⭐ Important |
| 11 | String Operations | ⭐ Important |
| 12 | DateTime & Time Series | ⭐ Important |
| 13 | Statistical Analysis & EDA | 🔥 Essential |
| 14 | Apply, Transform & Feature Engineering | 🔥 Essential |
| 15 | Pandas + NumPy + SQL + Performance | ⭐ Important |
| 16 | Pandas for Machine Learning + Projects | 🔥 Essential |

---

## 📚 Topics & Practice Guide

### 01. Pandas Fundamentals
- What is Pandas? Features and applications
- `import pandas as pd`
- Series and DataFrame
- Series vs DataFrame
- Pandas vs NumPy
- Index, columns, shape, and data types

```python
import pandas as pd

series = pd.Series([10, 20, 30])

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, 25, 30]
})

print(df)
```

### 02. Data Loading & Export
- Read CSV, Excel, JSON, SQL, and Parquet files
- Export data using `to_csv()`, `to_excel()`, `to_json()`, `to_sql()`, and `to_parquet()`
- Understand encoding, delimiters, and missing values during loading
- Learn the basics of handling large files

```python
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)
```

### 03. Data Inspection & Understanding
- `head()`, `tail()`, `sample()`
- `info()`, `describe()`, `shape`, `columns`, `dtypes`
- `unique()`, `nunique()`, `value_counts()`
- `memory_usage()`
- Initial missing-value checks

```python
df.head()
df.info()
df.describe()
df.isna().sum()
```

### 04. Data Selection — `loc` & `iloc`
- Select one or multiple columns
- Label-based selection with `loc`
- Position-based selection with `iloc`
- Boolean filtering and multiple conditions
- `isin()`, `between()`, and `query()`

```python
df["Age"]
df[["Name", "Age"]]

df.loc[0, "Age"]
df.iloc[0, 1]

df[df["Age"] > 25]
```

### 05. Data Cleaning — Missing Values
- Identify and count missing values
- `isna()`, `isnull()`, and `notna()`
- Remove or fill missing values with `dropna()` and `fillna()`
- Forward fill and backward fill
- Mean, median, and mode imputation
- Choose a strategy based on the data and context

```python
df.isna().sum()

df["Age"] = df["Age"].fillna(df["Age"].median())
```

### 06. Duplicates, Data Types & Text Cleaning
- Detect and remove duplicates: `duplicated()`, `drop_duplicates()`
- Convert types with `astype()` and `to_numeric()`
- Convert datetime and categorical columns
- Clean strings and standardize categories
- Rename and normalize column names

```python
df = df.drop_duplicates()
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Name"] = df["Name"].str.strip().str.lower()
```

### 07. Data Manipulation
- Add new and conditional columns
- Use `assign()`
- Remove rows or columns with `drop()`
- Rename columns
- Sort with `sort_values()` and `sort_index()`
- Ascending, descending, and multi-column sorting

```python
df["Bonus"] = df["Salary"] * 0.10

df = df.drop(columns=["Bonus"])
df = df.sort_values("Salary", ascending=False)
```

### 08. GroupBy & Aggregation
- Group data using `groupby()`
- Aggregations: `sum()`, `mean()`, `median()`, `min()`, `max()`, `count()`, `size()`, `std()`
- Multiple aggregations with `agg()`
- `transform()`, `filter()`, and `apply()`

```python
df.groupby("Department")["Salary"].mean()

df.groupby("Department")["Salary"].agg(
    ["mean", "min", "max"]
)
```

### 09. Merge, Join & Concat
- Combine datasets with `concat()`, `merge()`, and `join()`
- Inner, left, right, and outer merges
- One-to-one, one-to-many, and many-to-many relationships
- Merge on one or multiple keys

```python
combined = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"
)

stacked = pd.concat([df1, df2], ignore_index=True)
```

**Remember:** `concat` stacks objects, `merge` combines using key columns, and `join` commonly combines using indexes.

### 10. Reshaping — Pivot & Melt
- `pivot()`
- `pivot_table()`
- `melt()`
- Wide-to-long and long-to-wide transformations

```python
summary = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)
```

### 11. String Operations
- The `.str` accessor
- `lower()`, `upper()`, `title()`, `strip()`
- `replace()`, `contains()`, `startswith()`, `endswith()`
- `split()`, `len()`, and `extract()`
- Basic regular expressions (Regex)

```python
df["Name"] = df["Name"].str.strip().str.lower()

df[df["Name"].str.contains("rahim", case=False, na=False)]
```

### 12. DateTime & Time Series
- `pd.to_datetime()`
- Extract year, month, day, hour, week, quarter, and day of week
- Date differences and `Timedelta`
- `date_range()`, DatetimeIndex, and date filtering
- Resampling, downsampling, and upsampling

```python
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
```

### 13. Statistical Analysis & EDA
- Mean, median, mode, variance, and standard deviation
- Min, max, percentiles, quantiles, skewness, and kurtosis
- Correlation and covariance
- Univariate, bivariate, and multivariate analysis
- Feature-target relationships, distributions, categories, and outliers

```python
df.describe()
df.corr(numeric_only=True)
df.cov(numeric_only=True)
```

### 14. Apply, Transform & Feature Engineering
- `apply()` and `transform()`
- Numerical, categorical, and datetime features
- Aggregated, group-based, interaction, and ratio features
- Binning and log transformation

```python
df["Salary_Increased"] = df["Salary"].apply(lambda x: x * 1.10)

df["Department_Avg"] = (
    df.groupby("Department")["Salary"].transform("mean")
)
```

### 15. Pandas + NumPy + SQL + Performance
- Convert between Pandas DataFrames and NumPy arrays
- Read SQL query results into Pandas
- Vectorization and avoiding unnecessary loops
- Efficient filtering and memory usage
- `category`, `usecols`, and `chunksize`
- Process large CSV files in chunks

```python
array = df.to_numpy()

# Requires a database connection and a SQL query:
# result = pd.read_sql(query, connection)

for chunk in pd.read_csv("large.csv", chunksize=10_000):
    process(chunk)  # Define process() for your use case
```

### 16. Pandas for Machine Learning + Real Projects
- Prepare feature matrix `X` and target `y`
- Handle missing values, duplicates, and outliers
- Prepare categorical encoding and numerical transformations
- Feature selection and feature creation
- Train/test preparation and data leakage prevention
- Build end-to-end data preparation workflows for Scikit-learn

```python
# Example: separate features and target
X = df.drop(columns=["target"])
y = df["target"]
```

> **ML workflow:** Raw Data → Load → Inspect → Clean → Transform → EDA → Feature Engineering → `X` / `y` → Train/Test Split → Scikit-learn

---

## 🧪 Practice Projects

I plan to apply the topics above through progressively challenging datasets and projects.

| Level | Project Ideas |
|---|---|
| Beginner | Student Performance Analysis, Titanic EDA |
| Beginner–Intermediate | Sales Analysis, Netflix EDA |
| Intermediate | E-Commerce Analysis, Customer Analysis, HR Analytics |
| Intermediate–Advanced | Customer Churn, Marketing Analysis, Financial Analysis |
| Advanced | End-to-End Exploratory Data Analysis (EDA) |

Projects will be added as I complete them. Dataset choice, scope, and results may vary.

---

## 🧭 Recommended Learning Order

```text
Fundamentals
    ↓
Data Loading → Inspection → Selection & Filtering
    ↓
Missing Values → Cleaning → Manipulation
    ↓
GroupBy → Merge / Join / Concat → Pivot / Melt
    ↓
String Operations + DateTime
    ↓
Statistics + EDA
    ↓
Apply / Transform + Feature Engineering
    ↓
NumPy / SQL / Performance
    ↓
ML Data Preparation + Real Projects
```

### ⭐ Core Skills to Master

`DataFrame` → Loading → Inspection → `loc` / `iloc` → Filtering → Cleaning → `groupby()` → Merge → EDA → Feature Engineering → ML Preparation

---

## 📁 Suggested Repository Structure

```text
pandas-practice/
│
├── README.md
├── requirements.txt
│
├── 01_pandas_fundamentals/
├── 02_data_loading_export/
├── 03_data_inspection/
├── 04_data_selection/
├── 05_missing_values/
├── 06_data_cleaning/
├── 07_data_manipulation/
├── 08_groupby_aggregation/
├── 09_merge_join_concat/
├── 10_reshaping/
├── 11_string_operations/
├── 12_datetime_time_series/
├── 13_statistics_eda/
├── 14_feature_engineering/
├── 15_numpy_sql_performance/
│
└── 16_ml_preparation_projects/
    ├── student_performance_analysis/
    ├── sales_analysis/
    └── titanic_eda/
```

*This is a suggested structure; folders can be added as the repository grows.*

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/pandas-practice.git
cd pandas-practice
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter scikit-learn openpyxl
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

Open a notebook and start practicing. Some examples involving Excel, SQL, or Parquet may require additional dependencies or a database connection.

---

## 📖 Learning Resources

- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [Pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

---

## 📈 Learning Progress

This repository is a work in progress. I will continue adding notebooks, code examples, exercises, and project-based applications as I learn.

- [ ] Complete Pandas fundamentals and core operations
- [ ] Practice data cleaning and transformation
- [ ] Complete EDA exercises
- [ ] Practice feature engineering and ML data preparation
- [ ] Add real-world datasets and projects
- [ ] Review and improve existing notebooks

---

## 🤝 Contributions

This is primarily a personal learning repository. Suggestions, corrections, and constructive feedback are welcome.

If you find an issue or have an improvement, feel free to open an issue or submit a pull request.

---

## 👨‍💻 Author

**Md. Shagor Ali**  
Aspiring AI/ML Engineer | Data Science | Computer Vision | NLP | LLMs

- GitHub: https://github.com/shagor186
- LinkedIn: www.linkedin.com/in/shagor186

---

<div align="center">

### ⭐ If you find this repository useful, consider giving it a star!

**Learn consistently. Practice intentionally. Build with data.**

</div>