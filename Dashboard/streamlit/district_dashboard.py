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
serious_accidents = len(filtered_df[filtered_df['Accident_Severity'] == 'Serious'])
fatal_accidents = len(filtered_df[filtered_df['Accident_Severity'] == 'Fatal'])

with kpi_col1:
    st.metric("Total Accidents", total_accidents)
with kpi_col2:
    st.metric("Slight Accidents", slight_accidents)
with kpi_col3:
    st.metric("Serious Accidents", serious_accidents)
with kpi_col4:
    st.metric("Fatal Accidents", fatal_accidents)

st.header(f"3. Accident Locations ({selected_district})")

# Define marker size based on number of casualties (scaling factor added for better visibility)
filtered_df['marker_size'] = filtered_df['Number_of_Casualties'] * 5

map_fig = px.scatter_mapbox(
    filtered_df,
    lat='Latitude',
    lon='Longitude',
    color='Accident_Severity',
    size='marker_size',  # Adjust size based on casualties
    opacity=0.6,  # Make circles more transparent
    mapbox_style='carto-positron',
    zoom=10,
    labels={'Accident_Severity': 'Severity'},
    hover_data={
        'Latitude': True,
        'Longitude': True,
        'Accident_Severity': True,
        'Number_of_Casualties': True,
        'Number_of_Vehicles': True
    }
)

st.plotly_chart(map_fig)
st.caption("Map showing the location and severity of accidents, with circle size representing casualties.")