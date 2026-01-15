import streamlit as st
import pandas as pd
from multi_app import MultiApp # custom class for multi-page app

import dataset_overview # page 1: dataset summary
import eda # page 2: exploratory data analysis
import aqi_predcition  # page 3: AQI prediction model

# Loading the cleaned air quality dataset
df = pd.read_csv("cleaned_air_quality.csv")

# sidebar title
st.sidebar.markdown(
    "<h2 style='text-align:center; color:green;'>India Air Quality Analysis</h2>",
    unsafe_allow_html=True
)
st.sidebar.markdown("---")

st.sidebar.markdown("👨‍🎓 Student ID: 20341085")

# Creating MultiApp instance to manage multiple pages
app = MultiApp()

# Adding apps (passing df using lambda)
app.add_app("Dataset Overview", lambda: dataset_overview.app(df))
app.add_app("EDA", lambda: eda.app(df))
app.add_app("AQI Prediction", lambda: aqi_predcition.app())

# Running the Streamlit application
app.run()
