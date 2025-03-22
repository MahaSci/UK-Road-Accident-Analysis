import streamlit as st
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv('filtered_accident_data_set.csv')

df['Accident Date'] = pd.to_datetime(df['Accident Date'], dayfirst=True)
df['Year'] = df['Accident Date'].dt.year
df['Weekday'] = df['Accident Date'].dt.weekday

vehicle_categories = {
    'Car': 'Cars & Taxis', 'Taxi/Private hire car': 'Cars & Taxis',
    'Motorcycle 50cc and under': 'Motorcycles', 'Motorcycle 125cc and under': 'Motorcycles',
    'Motorcycle over 125cc and up to 500cc': 'Motorcycles', 'Motorcycle over 500cc': 'Motorcycles',
    'Van / Goods 3.5 tonnes mgw or under': 'Goods Vehicles', 'Goods over 3.5t. and under 7.5t': 'Goods Vehicles',
    'Goods 7.5 tonnes mgw and over': 'Goods Vehicles', 'Bus or coach (17 or more pass seats)': 'Public Transport',
    'Minibus (8 - 16 passenger seats)': 'Public Transport', 'Pedal cycle': 'Others',
    'Agricultural vehicle': 'Others', 'Other vehicle': 'Others'
}
df['Vehicle_Category'] = df['Vehicle_Type'].map(vehicle_categories)

# Streamlit App
st.set_page_config(layout="wide")
st.title("Traffic Accident Dashboard")
st.markdown("This dashboard shows key trends and patterns district-wise in traffic accidents, helping to identify areas for improvement and safety measures in Birmingham and surrounding areas.")
st.markdown("Created as part of a group project: [Project Repository](https://github.com/MahaSci/UK-Road-Accident-Analysis)")
st.sidebar.header("Filters")

districts = ["All Districts"] + sorted(df['District Area'].unique().tolist())
selected_district = st.sidebar.selectbox("Select District:", districts)
filtered_df = df if selected_district == "All Districts" else df[df['District Area'] == selected_district]

years = ["All Years"] + sorted(filtered_df['Year'].unique().tolist())
selected_year = st.sidebar.selectbox("Select Year:", years)
final_filtered_df = filtered_df if selected_year == "All Years" else filtered_df[filtered_df['Year'] == int(selected_year)]


# KPI Metrics
st.subheader(f"Key Metrics for {selected_district} ({selected_year})")
kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
kpi_col1.metric("Total Accidents", len(final_filtered_df))
kpi_col2.metric("Slight Accidents", len(final_filtered_df[final_filtered_df['Accident_Severity'] == 'Slight']))
kpi_col3.metric("Serious Accidents", len(final_filtered_df[final_filtered_df['Accident_Severity'] == 'Serious']))
kpi_col4.metric("Fatal Accidents", len(final_filtered_df[final_filtered_df['Accident_Severity'] == 'Fatal']))

# Map Visualization
st.subheader(f"Accident Locations in {selected_district} ({selected_year})")
final_filtered_df['marker_size'] = final_filtered_df['Number_of_Casualties'] * 5
map_fig = px.scatter_mapbox(
    final_filtered_df, lat='Latitude', lon='Longitude', color='Accident_Severity',
    size='marker_size', opacity=0.6, mapbox_style='carto-positron', zoom=10,
    hover_data={'Accident_Severity': True, 'Number_of_Casualties': True, 'Number_of_Vehicles': True},
    labels={'Accident_Severity': 'Severity', 'Number_of_Casualties': 'Casualties', 'Number_of_Vehicles': 'Vehicles Involved'}
)
st.plotly_chart(map_fig)

# Severity Distribution
col1, col2 = st.columns(2)
severity_counts = final_filtered_df['Accident_Severity'].value_counts().reset_index()
severity_counts.columns = ['Accident_Severity', 'Count']
severity_fig = px.bar(severity_counts, x='Accident_Severity', y='Count', color='Accident_Severity', text='Count',
                      labels={'Accident_Severity': 'Severity', 'Count': 'Number of Accidents'})
col1.subheader(f"Severity Distribution in {selected_district} ({selected_year})")
col1.plotly_chart(severity_fig)

# Monthly Trend
monthly_trend = final_filtered_df.groupby(final_filtered_df['Accident Date'].dt.month).size().reset_index(name='Count')
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_trend['Month_Label'] = monthly_trend['Accident Date'].apply(lambda x: month_labels[x - 1])
monthly_fig = px.line(
    monthly_trend, 
    x='Month_Label', 
    y='Count', 
    markers=True, 
    text='Count',
    labels={'Month_Label': 'Month', 'Count': 'Number of Accidents'}
)
monthly_fig.update_traces(textposition='top center')  # Adjust label positioning

col2.subheader(f"Monthly Accident Trend in {selected_district} ({selected_year})")
col2.plotly_chart(monthly_fig)

# Weekly Trend
st.subheader(f"Weekly Accident Trend in {selected_district} ({selected_year})")
weekday_counts = final_filtered_df['Weekday'].value_counts().sort_index()
weekday_fig = px.bar(
    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    y=weekday_counts.values,
    labels={'x': 'Day of the Week', 'y': 'Number of Accidents'}
)
st.plotly_chart(weekday_fig)

# Urban/Rural & Vehicle Breakdown
col3, col4 = st.columns(2)
urban_rural_counts = final_filtered_df['Urban_or_Rural_Area'].value_counts()
urban_rural_fig = px.bar(x=urban_rural_counts.index, y=urban_rural_counts.values, text=urban_rural_counts.values,
                          labels={'x': 'Location Type', 'y': 'Number of Accidents'})
col3.subheader(f"Urban vs. Rural Accidents in {selected_district} ({selected_year})")
col3.plotly_chart(urban_rural_fig)

vehicle_category_counts = final_filtered_df['Vehicle_Category'].value_counts()
vehicle_category_fig = px.bar(x=vehicle_category_counts.index, y=vehicle_category_counts.values, text=vehicle_category_counts.values,
                              labels={'x': 'Vehicle Type', 'y': 'Number of Accidents'})
col4.subheader(f"Vehicle Type Breakdown in {selected_district} ({selected_year})")
col4.plotly_chart(vehicle_category_fig)

# Light Conditions vs Severity & Road Surface Conditions vs Severity
col5, col6 = st.columns(2)
light_severity_fig = px.histogram(final_filtered_df, x='Light_Conditions', color='Accident_Severity', barmode='group',
                                  labels={'Light_Conditions': 'Lighting', 'Accident_Severity': 'Severity'})
col5.subheader(f"Light Conditions vs. Severity in {selected_district} ({selected_year})")
col5.plotly_chart(light_severity_fig)

road_surface_fig = px.histogram(final_filtered_df, x='Road_Surface_Conditions', color='Accident_Severity', barmode='group',
                                labels={'Road_Surface_Conditions': 'Road Surface', 'Accident_Severity': 'Severity'})
col6.subheader(f"Road Surface Conditions vs. Severity in {selected_district} ({selected_year})")
col6.plotly_chart(road_surface_fig)
