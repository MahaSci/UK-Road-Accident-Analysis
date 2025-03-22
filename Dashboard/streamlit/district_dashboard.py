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

# District Filter (Dropdown Selectbox) - Include "All Districts" option
districts = ["All Districts"] + sorted(df['District Area'].unique().tolist())
selected_district = st.selectbox("Select District:", districts)

# Filter data based on selected district (or show all if "All Districts" is selected)
if selected_district == "All Districts":
    filtered_df = df
else:
    filtered_df = df[df['District Area'] == selected_district]

# Year Filter (Dropdown Selectbox) - Include "All Years" option
years = ["All Years"] + sorted(filtered_df['Year'].unique().tolist())
selected_year = st.selectbox("Select Year:", years)

# Filter data based on selected year (or show all if "All Years" is selected)
if selected_year == "All Years":
    final_filtered_df = filtered_df
else:
    final_filtered_df = filtered_df[filtered_df['Year'] == int(selected_year)]

# KPIs
st.header(f"2. Key Metrics for {selected_district} ({selected_year})")
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

total_accidents = len(final_filtered_df)
slight_accidents = len(final_filtered_df[final_filtered_df['Accident_Severity'] == 'Slight'])
serious_accidents = len(final_filtered_df[final_filtered_df['Accident_Severity'] == 'Serious'])
fatal_accidents = len(final_filtered_df[final_filtered_df['Accident_Severity'] == 'Fatal'])

with kpi_col1:
    st.metric("Total Accidents", total_accidents)
with kpi_col2:
    st.metric("Slight Accidents", slight_accidents)
with kpi_col3:
    st.metric("Serious Accidents", serious_accidents)
with kpi_col4:
    st.metric("Fatal Accidents", fatal_accidents)

st.header(f"3. Accident Locations in {selected_district} ({selected_year})")
st.markdown("**How to Use:** Zoom with scroll/trackpad or settings (top right), click legend circles to filter by severity, use dropdowns for district & year, and hover for casualties & vehicles.")


# Define marker size based on number of casualties (scaling factor added for better visibility)
final_filtered_df['marker_size'] = final_filtered_df['Number_of_Casualties'] * 5

# vis 1: Create map figure
map_fig = px.scatter_mapbox(
    final_filtered_df,
    lat='Latitude',
    lon='Longitude',
    color='Accident_Severity',
    size='marker_size',  # Adjust size based on casualties
    opacity=0.6,  # Make circles more transparent
    mapbox_style='carto-positron',
    zoom=10,
    labels={'Accident_Severity': 'Severity'},
    hover_data={
        'Accident_Severity': True,
        'Number_of_Casualties': True,
        'Number_of_Vehicles': True,
        'Latitude': True,
        'Longitude': True,
        'marker_size': False
    }
)

st.plotly_chart(map_fig)
st.caption("Map showing the location and severity of accidents, with circle size representing casualties.")

# vis 2: Create bar chart of severity distribution
st.header(f"Accident Severity Distribution in {selected_district} ({selected_year})")

# Count occurrences of each severity level
severity_counts = final_filtered_df['Accident_Severity'].value_counts().reset_index()
severity_counts.columns = ['Accident_Severity', 'Count']

# Create bar chart
severity_fig = px.bar(
    severity_counts, 
    x='Accident_Severity', 
    y='Count', 
    color='Accident_Severity',
    color_discrete_sequence=['lightgrey', 'lightblue', 'lightsalmon'],
    text='Count'  # Display count above bars
)

st.plotly_chart(severity_fig)