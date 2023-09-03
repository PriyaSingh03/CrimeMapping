import streamlit as st
import os
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

current_directory = os.getcwd()
st.write(f"Current working directory: {current_directory}")

@st.cache_data  # Cache the data to improve performance
def load_data():
    # Replace with the path to your CSV file
    st.write(f"Loading data from: {current_directory}")
    data = pd.read_csv('PERFECT_FIR_DATASET.csv')
    return data

def get_color_based_on_parameter(row, parameter):
    # Define a colormap based on the selected parameter
    colormap = {
        'DateTime': 'green',
        'Crime Type': 'blue'
    }

    # Get the value of the selected parameter for the current row
    parameter_value = row[parameter]

    # Map the parameter value to a color from the colormap
    color = colormap.get(parameter, 'red')  # Default to 'blue' if parameter is not found in the colormap
    return color

def get_color_based_on_time(row):
    # Extract the hour component from the 'DateTime' column
    datetime_value = pd.to_datetime(row['DateTime'], format='%Y-%m-%d %H:%M:%S')
    hour = datetime_value.hour

    # Check if the hour is before 15:00 (3 pm)
    if (hour <15):
        return 'lightgreen'
    else:
        return 'cadetblue'


def app():
    st.title("Location Data on Map")

    # Load the data
    data = load_data()

    # Rename the 'Latitude' and 'Longitude' columns to 'lat' and 'lon' (standard for Streamlit)
    data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)

    
    selected_parameter = st.sidebar.radio("Select parameter for visualization", ['Markers', 'Heatmap'])

    # # Create a Streamlit map
    # st.map(data, use_container_width=True)
    min_latitude = data['lat'].min()
    max_latitude = data['lat'].max()
    min_longitude = data['lon'].min()
    max_longitude = data['lon'].max()


    UP_AREA = [(min_latitude + max_latitude) / 2, (min_longitude + max_longitude) / 2]
    map  = folium.Map(location=UP_AREA, zoom_start=6) #tiles='Stamen Toner'

    
    if selected_parameter == 'Markers':
        selected_mapping_parameter = st.sidebar.radio("Select parameter for color mapping", [None, 'DateTime'])
        for index, row in data.iterrows():
            fir_no = row['FIR Number']
            registered_district = row['REGISTERED DISTRICT']
            registered_ps = row['Registered PS']
            location = (row['lat'], row['lon'])
            date = row['DateTime']
            crime_type = row['Crime Type']
            if selected_mapping_parameter is not None:
                color = get_color_based_on_time(row)
            else:
                color = 'red'

            folium.Marker(location=location, 
                          popup=f"FIR Number: {fir_no}<br> Date: {date} <br>Registered District: {registered_district} <br> Crime Type : {crime_type}<br>Registered PS: {registered_ps}",
                        icon=folium.Icon(color=color)).add_to(map)
            
        # Create a custom HTML legend
        legend_html = """
        <div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background-color: white; padding: 5px; border-radius: 5px; box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);">
        <p><span style="background-color: lightgreen; padding: 5px; border-radius: 5px;"></span> Morning</p>
        <p><span style="background-color: cadetblue; padding: 5px; border-radius: 5px;"></span> Night</p>
        </div>
        """
        map.get_root().html.add_child(folium.Element(legend_html))

    elif selected_parameter == 'Heatmap':
            heat_data = data[['lat', 'lon']]
            HeatMap(heat_data, radius=15).add_to(map)

            
            st_folium(map, width=1000, key='11')

        

    st_folium(map, width=1000, key='12')


if __name__ == "__main__":
    app()

