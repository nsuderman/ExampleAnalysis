import pandas as pd
import os
import streamlit as st


@st.cache(persist=False,
          allow_output_mutation=True,
          suppress_st_warning=True,
          show_spinner=True)
def get_country_data():
    path = f'{os.getcwd()}\\data\\countries_of_the_world.csv'
    return pd.read_csv(path)
