import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Basic Information
print(df.head())
print(df.info())
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Top 10 States by Sales
state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
state_sales.head(10).plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("state_sales.png")
plt.show()

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Category-wise Sales")
plt.savefig("category_sales.png")
plt.show()

print("\nRetail Sales Analysis Completed Successfully!")

# Top 5 Profitable States
profit = df.groupby("State")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
profit.head(5).plot(kind="bar", color="green")
plt.title("Top 5 Profitable States")
plt.xlabel("State")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("top_profit_states.png")
plt.show()

print("\nTop 5 Profitable States:")
print(profit.head(5))