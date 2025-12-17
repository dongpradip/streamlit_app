import streamlit as st
import pandas as pd
from multi_app import MultiApp   # import your class

import dataset_overview
import eda
import aqi_predcition   # fixed spelling

# Load the dataframe
df = pd.read_csv("cleaned_air_quality.csv")

st.sidebar.markdown("<h2 style='text-align:center; color:green;'>India Air Quality</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("Choose Page", ["Dataset Overview", "EDA", "AQI Prediction"])
st.sidebar.markdown("---")
st.sidebar.markdown("👨‍🎓 Student ID: 20341085")

# Create app instance
app = MultiApp()

# # Add apps (pass df using lambda)
# app.add_app("Dataset Overview", lambda: dataset_overview.app(df))
# app.add_app("EDA", lambda: eda.app(df))
# app.add_app("AQI Prediction", lambda: aqi_predcition.app())

if page == "Dataset Overview":
    dataset_overview.app(df)
elif page == "EDA":
    eda.app(df)
elif page == "AQI Prediction":
    aqi_predcition.app()

# Run the app
app.run()