import pandas as pd
import numpy as np   # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import matplotlib.pyplot as plt
import streamlit as st  # pip install streamlit
import plotly

st.set_page_config(page_title="SUPER MARKET DASHBOARD", page_icon=":bar_chart:", layout="wide")
st.title("SUPER MARKET DASHBOARD")
st.header("Description")
st.subheader("A supermarket is a self-service shop offering a wide variety of food, beverages and household products, organized into sections. This kind of store is larger and has a wider selection than earlier grocery stores, but is smaller and more limited in the range of merchandise than a hypermarket or big-box market")
st.image("89.PNG")
st.image("56.PNG")

# Load the data
df = pd.read_csv("supermarket_sales - Sheet1.csv")

# Set the page title and icon

# Create a sidebar to select the visualization type
st.sidebar.title("Visualization Type")
vis_type = st.sidebar.selectbox("Choose a visualization type", ["Pie Chart", "Bar Chart", "Scatter Plot", "Line Chart"])

# Create a sidebar to select the product line
st.sidebar.title("Product Line")
product_line = st.sidebar.selectbox("Choose a product line", df["Product line"].unique())

filtered_df = df[df["Product line"] == product_line]

# Create the visualization based on the selected visualization type
if vis_type == "Pie Chart":
    fig = px.pie(filtered_df, values="gross income", names="City", title=f"Gros income by City for {product_line}")
    st.plotly_chart(fig)
elif vis_type == "Bar Chart":
    fig = px.bar(filtered_df, x="City", y="Unit price", title=f"unit price by city for {product_line}")
    st.plotly_chart(fig)
elif vis_type == "Scatter Plot":
    fig = px.scatter(filtered_df, x="City", y="Total", color="Payment", title=f"Total  vs city for {product_line}")
    st.plotly_chart(fig)
elif vis_type == "Line Chart":
    fig = px.line(filtered_df, x="Payment", y="Rating", color="City", title=f"Gross income over city for {product_line}")
    st.plotly_chart(fig)


fig = px.box(df, x="Product line", y="Unit price", title="Unit Price by Product Line")
st.plotly_chart(fig)

fig = px.histogram(df, x="Total", nbins=20, title="Histogram of Total Sales")
st.plotly_chart(fig)

fig = px.scatter(df, x="Quantity", y="Total", title="Total Sales by Quantity")
st.plotly_chart(fig)