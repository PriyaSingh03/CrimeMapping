import streamlit as st
from streamlit_option_menu import option_menu

import Home
import FIR
import Crime
import HeatMap

# Call set_page_config at the very beginning of your script
st.set_page_config(
    page_title="Crime Mapping",
    page_icon="🗺️"
)
st.set_option('deprecation.showPyplotGlobalUse', False)


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Crime Mapping ',
                options=['Home', 'FIR', 'Crime Rate', 'Heat Map'],
                icons=['house-fill', 'file-text-fill',
                       'exclamation-triangle', 'bar-chart-fill'],
                menu_icon='geo-alt-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "gray"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }
            )

        if app == "Home":
            Home.app()
        if app == "FIR":
            FIR.app()
        if app == "Crime Rate":
            Crime.app()
        if app == 'Heat Map':
            HeatMap.app()

# Create an instance of MultiApp and run it
multi_app = MultiApp()
multi_app.run()
