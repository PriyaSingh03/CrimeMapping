import streamlit as st
import pandas as pd

@st.cache_data  # Cache the data to improve performance
def load_data():
    # Replace with the path to your CSV file
    data = pd.read_csv('all_india_fir_data - sample.csv')
    return data

def app():
    st.title("Location Data on Map")
    
    # Load the data
    data = load_data()

    # Rename the 'Latitude' and 'Longitude' columns to 'lat' and 'lon' (standard for Streamlit)
    data.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)

    # Create a Streamlit map
    st.map(data, use_container_width=True)

if __name__ == "__main__":
    app()
