import streamlit as st


def app():
    # Header
    st.title("Welcome to the Crime Mapping Model 🗺️")

    # Introduction
    st.write("Explore crime data in your area and make data-driven decisions with our interactive crime mapping model. 🚓🔍")

    # Key Features
    st.header("Key Features 🌟")
    st.markdown("""
    - **Real-time Crime Data Visualization**: Visualize crime data on an interactive map. 🗺️📊
    - **Crime Trends Analysis**: Analyze crime patterns and trends. 📈🔍
    - **User-Friendly Interface**: Easy-to-use tools for customizing and filtering data. 🖥️🎛️
    """)

    # User Instructions
    st.header("How to Use 🤔")
    st.write("1. Select your location and date range. 📅📍")
    st.write("2. Use filters to customize the data displayed. 🔍📂")
    st.write("3. Interact with the map to explore crime incidents. 🗺️🚔")
    st.write("4. Analyze trends and make informed decisions. 📊🧐")

    # Data Sources
    st.header("Data Sources 📊📂")
    st.write("Our crime mapping model uses data from local law enforcement agencies and is updated regularly.")

    # Use Cases
    st.header("Use Cases 🌐🤝")
    st.markdown("""
    - **Citizens**: Stay informed about crime trends in your neighborhood. 🏘️👥
    - **Law Enforcement**: Make data-driven decisions to allocate resources effectively. 🚓💼
    - **Researchers**: Analyze crime patterns for academic or policy purposes. 📚🔬
    """)

    # Contact Information
    st.header("Contact Us 📧📞")
    st.write("Have questions or feedback? Contact us at contact@byteSquat.com 📩📞")

