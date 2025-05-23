# 🛍️ Amazon Sales Data Analysis
This project explores an Amazon sales dataset to uncover trends in product sizes, categories, customer types, and regional order patterns using Python-based data analysis and visualizations.

## 📊 Project Objectives
- Clean and preprocess raw sales data.
- Analyze product and customer behavior.
- Visualize sales patterns by size, category, location, and type.
- Extract insights to support business decisions.

## 🧰 Technologies Used
- **Python**
- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Matplotlib** and **Seaborn** for visualization

## 📁 Dataset
-Source: Internal Amazon sales report provided as Amazon Sale Report.csv
-Key Columns:
Date, Qty, Amount, Size, Category
Courier Status, Status, B2B
ship-city, ship-state, ship-postal-code

## 📈 Key Visualizations
- **Bar Plot**: Distribution of product sizes sold
- **Histogram**: Popular product categories by quantity
- **Count Plot**: Courier shipping status breakdown
- **Scatter Plot**: Available product sizes by category
- **Bar Plot**: Comparison of B2B vs B2C total sales
- **Bar Plots**: Top 10 cities and states by order volume

## 🔍 Sample Insights
- "M" size clothing is the most commonly purchased.
- T-shirts are the leading product category.
- Most shipments are successfully couriered.
- B2C sales volume exceeds B2B in total revenue.
- Metro cities like Mumbai and Delhi top the order charts.

## ▶️ How to Run
-Ensure the dataset file Amazon Sale Report.csv is in the project directory.

-Run the analysis script:-
**python amazon_data_analysis.py**


## 🔧 Notes
Modify the file path in the script if needed:-
**df = pd.read_csv("Amazon Sale Report.csv")**

