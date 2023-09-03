import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

@st.cache_data  # Cache the data to improve performance
def load_data():
    data = pd.read_csv('CONCAT_CRIME_IPC_DATA_HEAD_500_geocoded.csv')
    return data

@st.cache_data  
def load_hotspot_data():
    data = pd.read_csv('PERFECT_FIR_DATASET.csv')
    return data


def create_folium_map(data):

    min_latitude = data['lat'].min()
    max_latitude = data['lat'].max()
    min_longitude = data['lon'].min()
    max_longitude = data['lon'].max()


    UP_AREA = [(min_latitude + max_latitude) / 2, (min_longitude + max_longitude) / 2]
    map  = folium.Map(location=UP_AREA, zoom_start=6)

    heat_data = data[['lat', 'lon']]
    HeatMap(heat_data, radius=15).add_to(map)

    return map




def app():
    st.title("Heat Map of Crimes all over India")
    
    # Load the data
    data = load_data()

    # Rename the 'Latitude' and 'Longitude' columns to 'lat' and 'lon' (standard for Streamlit)
    data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)

    # Create a Streamlit sidebar to select the map type
    map_type = st.sidebar.radio("Select Map Type", ["Normal Map", 'Hotspot for Crimes'])

    if map_type == "Normal Map":
        # Create and display the Folium map
        folium_map = create_folium_map(data)
        st_folium(folium_map, width=900, zoom=4)

    if map_type == 'Hotspot for Particular Crimes':
         st.title("Crime Hotspot Analysis")

        # Load the data
         data = load_hotspot_data()

        # Rename the 'Latitude' and 'Longitude' columns to 'lat' and 'lon' (standard for Streamlit)
         data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)

        # Create a Streamlit sidebar to select the crime type (IPC section)
         selected_crime_type = st.sidebar.selectbox("Select Crime Type (IPC Section)", data['Crime Type'].unique())

        # Filter the data based on the selected crime type
         filtered_data = data[data['Crime Type'] == selected_crime_type]

        # Create a Streamlit map
         min_latitude = filtered_data['lat'].min()
         max_latitude = filtered_data['lat'].max()
         min_longitude = filtered_data['lon'].min()
         max_longitude = filtered_data['lon'].max()

         UP_AREA = [(min_latitude + max_latitude) / 2, (min_longitude + max_longitude) / 2]
         map = folium.Map(location=UP_AREA, zoom_start=6)

        # Plot hotspot zones based on the selected crime type
         heat_data = filtered_data[['lat', 'lon']]
         HeatMap(heat_data, radius=15).add_to(map)

         st_folium(map, width=1000)
        
   

if __name__ == "__main__":
    app()
