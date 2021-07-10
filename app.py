import streamlit as st
from streamlit import caching
import pandas as pd
import numpy as np
from data import data
from PIL import Image
import os


if __name__ == "__main__":
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Examples For Baker Hughes",  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
    )

    tabs = ["Application", "GDP Economic Analysis", "Customer Segmentation"]
    page = st.sidebar.selectbox("Tabs", tabs)
    df_country = data.get_country_data()


    if page=='Application':
        st.title('Data Science and Econometric Examples')
        st.markdown('____')
        st.write('This application was built to provide agile examples of data science analysis and predictions. '
                 'I have provided the two examples below based on open datasets:')

        st.write('Talk about the job and the image.')
        image = Image.open(f'{os.getcwd()}\\assets\\venn.png')
        width, height = image.size
        image = image.resize((int(width*.75), int(height*.75)))
        st.image(image, caption='Data Science / Economics / Data Analysis Venn Diagram')

        st.subheader('GDP and Economic Analysis')
        st.write('This example ...')
        st.write('')

        st.subheader('Customer Segmentation')
        st.write('This example ...')
        st.write('')
        pass

    elif page=="GDP Economic Analysis":
        pass

    elif page=="Customer Segmentation":
        pass


