import streamlit as st
from streamlit_option_menu import option_menu

import Home
import FIR
import Crime
import HeatMap
st.set_page_config(
    page_title="Crime Mapping",
)


class MultiApp:

    def _init_(self):
        self.apps = []

    def add_app(self, title, func,):

        self.apps.append({
            "title": title,
            "function": func

        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Crime Mapping ',
                options=['Home', 'FIR', 'Crime Rate', 'Heat Map'],
                icons=['house-fill', 'file-text-fill',
                       'exclamation-triangle', 'bar-chart-fill'],
                menu_icon='geo-alt-fill',
                default_index=1,
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

    run()