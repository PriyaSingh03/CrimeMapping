import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

@st.cache_data  # Cache the data to improve performance
def load_data():
    # Replace with the path to your CSV file
    data = pd.read_csv('CONCAT_CRIME_IPC_DATA_HEAD_500_geocoded.csv')
    return data


def create_folium_map(data):

    min_latitude = data['lat'].min()
    max_latitude = data['lat'].max()
    min_longitude = data['lon'].min()
    max_longitude = data['lon'].max()


    UP_AREA = [(min_latitude + max_latitude) / 2, (min_longitude + max_longitude) / 2]
    map  = folium.Map(location=UP_AREA, zoom_start=6)

    for _,row in data.iterrows():
        location = (row['lat'], row['lon'])
        folium.Marker( location=location, 
                      popup=True,
                    icon=folium.Icon(color='red')).add_to(map)

    return map


def show_plot(data):
    # Group data by 'state_ut' and calculate the sum of each crime column
    crime_data = data.groupby('state_ut')[['rape', 'arson', 'robbery', 'custodial_rape',
                                      'theft', 'riots', 'auto_theft',
                                      'kidnapping_abduction', 'dacoity', 'cheating', 'murder', 'other_ipc_crimes', 'dowry_deaths',]].sum()

    # Create a Streamlit sidebar to select the state
    selected_state = st.sidebar.selectbox("Select State", data['state_ut'].unique())

    # Filter the data for the selected state
    state_data = crime_data[crime_data.index == selected_state].squeeze()
    return selected_state,state_data

def app():
    # st.title("Crime Rate Visualization all over India")
    
    # Load the data
    data = load_data()

    # Rename the 'Latitude' and 'Longitude' columns to 'lat' and 'lon' (standard for Streamlit)
    data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)

    # Create a Streamlit sidebar to select the map type
    map_type = st.sidebar.radio("Select Map Type", ["Normal Map", 'Show Plot'])

    if map_type == "Normal Map":
        # Create and display the Folium map
        folium_map = create_folium_map(data)
        st_folium(folium_map, width=1000)
    if map_type == 'Show Plot':
        selected_state, state_data = show_plot(data=data)

        st.title(f"Crime Rate for {selected_state}")
        fig, ax = plt.subplots(figsize=(10, 6))
        state_data.plot(kind='bar', ax=ax)
        plt.xlabel("Crimes")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        st.pyplot(fig)
   

if __name__ == "__main__":
    app()
