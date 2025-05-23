import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("Amazon Sale Report.csv")
pd.set_option("display.max_columns", None)  
pd.set_option("display.width", None)      
pd.set_option("display.max_colwidth", None)
# print(df.head())
print(df.info())

# checking Null Values:-
print(df.isnull().sum())
print(df.shape)

#Data Cleaning
# dropping null values:-
df.dropna(inplace=True)
print(df.isnull().sum())
print(df.shape)
df.info()

print(df.head())

#change data type :-
df["ship-postal-code"]=df["ship-postal-code"].astype("int")
print(df["ship-postal-code"].dtype)
# Convert 'Date' to datetime objects
df['Date'] = pd.to_datetime(df['Date'])
print(df.describe())

#describing our data with object data type :-
print(df.describe(include="object"))
print(df[["Qty","Amount"]].describe())
# print(df.head())

#Plot 1:- this plot will show quantity of the various sizes of clothes purchased by the customers.

custom_colors = ['#FFC107', '#2196F3', '#4CAF50', '#9C27B0', '#FF5722', '#607D8B', '#795548', '#00BCD4', '#E91E63', '#8BC34A','#216653']
ax=sns.countplot(x="Size",data=df,hue="Size",palette=custom_colors)
plt.xlabel("Product Sizes")
plt.ylabel('Number of Orders')
plt.title('Distribution of Product Sizes')
plt.tight_layout()
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

#Insights :- Plot 1 shows that majority of orders are of "M" size clothes followed by L and XL.

#Plot 2:- this plot will show different category of product and their quantities purchased.

cat=df["Category"].astype(str)
plt.figure()
plt.hist(cat,bins=15,edgecolor="Green",color='green')
plt.title('Top Categories by Quantity Sold')
plt.xticks(rotation=90)
plt.show()

#Insights:- Plot 2 shows that Tshirt is the most purchased product.

#Plot 3:- This plot will show the courier status :-

ax=sns.countplot(data=df,x="Courier Status",hue="Status")
plt.title('Total Sales by Courier Status') 
plt.show() 

#Plot 3 shows that majority of the products have been shipped through courier

#Plot 4 :- This plot will show available sizes of different products

x=df["Category"]
y=df["Size"]
plt.scatter(x,y,marker="D")
plt.xlabel("category")
plt.ylabel("Sizes")
plt.title("Available Size")
plt.grid()
plt.show()

# Plot 5:- This plot will show the B2B vs B2C sales 

b2b_sales = df.groupby('B2B')['Amount'].sum()
plt.figure(figsize=(7, 5))
ax_b2b = sns.barplot(x=b2b_sales.index.map({True: 'B2B', False: 'B2C'}), y=b2b_sales.values, palette='viridis')
ax_b2b.bar_label(ax_b2b.containers[0], fmt='%.0f', fontsize=10)
plt.title('Total Sales: B2B vs. B2C')
plt.xlabel('Customer Type')
plt.ylabel('Total Sales Amount (INR)')
plt.tight_layout()
plt.show()

#Plot 6 :- This plot will show top 10 cities along with the order count 

top10_cities=df['ship-city'].value_counts().head(10)
plt.figure(figsize=(10,6))
ax=sns.countplot(data=df[df['ship-city'].isin(top10_cities.index)],x="ship-city",hue="ship-city",palette='tab10')
plt.title("Cities with most orders")
plt.xticks(rotation=90)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

#Plot 7 :- This plot will show top 10 states along with the order count 

top10_state=df['ship-state'].value_counts().head(10)
plt.figure(figsize=(10,6))
ax=sns.countplot(data=df[df['ship-state'].isin(top10_state.index)],x="ship-state",hue="ship-state", palette='tab10')
plt.title("States with most orders")
plt.xticks(rotation=90)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

