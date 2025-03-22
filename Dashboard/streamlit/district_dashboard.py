import streamlit as st
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv('filtered_accident_data_set.csv')

# Convert 'Accident Date' to datetime
df['Accident Date'] = pd.to_datetime(df['Accident Date'], dayfirst=True)

# Extract year, month, day, and weekday
df['Year'] = df['Accident Date'].dt.year
df['Month'] = df['Accident Date'].dt.month
df['Day'] = df['Accident Date'].dt.day
df['Weekday'] = df['Accident Date'].dt.weekday

# Streamlit App
st.set_page_config(layout="wide")
st.title("Traffic Accident Dashboard")
st.subheader("This dashboard shows key trends and patterns in traffic accidents across districts, helping to identify areas for improvement and safety measures.")

# District Filter (Dropdown Selectbox)
districts = sorted(df['District Area'].unique())
selected_district = st.selectbox("Select District:", districts)
filtered_df = df[df['District Area'] == selected_district]

# KPIs
st.header(f"2. Key Metrics for {selected_district}")
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

total_accidents = len(filtered_df)
slight_accidents = len(filtered_df[filtered_df['Accident_Severity'] == 'Slight'])
serious_accidents = len(filtered_df[filtered_df['Acxscident_Severity'] == 'Serious'])
fatal_accidents = len(filtered_df[filtered_df['Accident_Severity'] == 'Fatal'])

with kpi_col1:
    st.metric("Total Accidents", total_accidents)
with kpi_col2:
    st.metric("Slight Accidents", slight_accidents)
with kpi_col3:
    st.metric("Serious Accidents", serious_accidents)
with kpi_col4:
    st.metric("Fatal Accidents", fatal_accidents)
