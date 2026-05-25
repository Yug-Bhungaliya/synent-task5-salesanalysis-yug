import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("Sales Data Analysis Dashboard")

# Load Dataset
df = pd.read_csv("C:/Users/YUG/OneDrive - charusat.edu.in/Desktop/synent-task5-salesanalysis-yug/dataset/Sample - Superstore.csv")

# Show Dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Monthly Sales
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Month_Year'] = df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('Month_Year')['Sales'].sum()

st.subheader("Monthly Revenue Trend")

fig, ax = plt.subplots(figsize=(10,5))

monthly_sales.plot(kind='line', marker='o', ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)

# Top Products
top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)

st.subheader("Top 10 Selling Products")

fig2, ax2 = plt.subplots(figsize=(10,5))

top_products.head(10).plot(kind='bar', ax=ax2)

plt.xticks(rotation=45)

st.pyplot(fig2)

# Profit Analysis
profit_category = df.groupby('Category')['Profit'].sum()

st.subheader("Profit Analysis")

fig3, ax3 = plt.subplots(figsize=(8,5))

profit_category.plot(kind='bar', ax=ax3)

st.pyplot(fig3)