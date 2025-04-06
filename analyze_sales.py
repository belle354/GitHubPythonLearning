#!/usr/bin/env python3

import pandas as pd

# Load the Excel file
df = pd.read_excel("monthly_sales_2024.xlsx")

# Print basic stats
print("Monthly Sales Data:")
print(df)

# Calculate and print the average sales
average_sales = df['Sales'].mean()
print(f"\nAverage Monthly Sales: ${average_sales:,.2f}")
