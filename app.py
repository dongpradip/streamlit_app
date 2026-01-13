# import streamlit as st
# import pandas as pd
# from multi_app import MultiApp

# import dataset_overview
# import eda
# import aqi_predcition 

# # Load the dataframe
# df = pd.read_csv("cleaned_air_quality.csv")

# st.sidebar.markdown(
#     "<h2 style='text-align:center; color:green;'>India Air Quality Analysis</h2>",
#     unsafe_allow_html=True
# )
# st.sidebar.markdown("---")

# st.sidebar.markdown("👨‍🎓 Student ID: 20341085")

# # Create app instance
# app = MultiApp()

# # Add apps (pass df using lambda)
# app.add_app("Dataset Overview", lambda: dataset_overview.app(df))
# app.add_app("EDA", lambda: eda.app(df))
# app.add_app("AQI Prediction", lambda: aqi_predcition.app())

# # Run the app
# app.run()

import streamlit as st
import pandas as pd
from multi_app import MultiApp
import dataset_overview
import eda
import aqi_predcition

# 1. Page Configuration
st.set_page_config(
    page_title="Air Quality India",
    page_icon="🍏",
    layout="wide",
)

# 2. Apple-Style Minimalist CSS
st.markdown("""
    <style>
        /* Main Background */
        .stApp {
            background-color: #ffffff;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #f5f5f7 !important; /* Apple's signature light gray */
            border-right: 1px solid #d2d2d7;
        }

        /* Force Sidebar Text to Dark Gray (Apple's #1d1d1f) */
        [data-testid="stSidebar"] .stMarkdown p, 
        [data-testid="stSidebar"] h1, h2, h3, label {
            color: #1d1d1f !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Sidebar Title Design */
        .apple-title {
            font-size: 24px;
            font-weight: 600;
            letter-spacing: -0.5px;
            text-align: center;
            padding: 20px 0;
            color: #1d1d1f;
        }

        /* Bottom Student ID Styling */
        .sidebar-footer {
            position: fixed;
            bottom: 20px;
            width: 260px; /* Adjust based on sidebar width */
            text-align: center;
            font-size: 12px;
            color: #86868b !important;
            background-color: #f5f5f7;
            padding-top: 10px;
            border-top: 0.5px solid #d2d2d7;
        }

        /* Metric Styling to look like Apple Dashboards */
        [data-testid="stMetricValue"] {
            font-weight: 700 !important;
            color: #1d1d1f !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---

# A. Clean Header
st.sidebar.markdown('<div class="apple-title">Air Quality India</div>', unsafe_allow_html=True)

# B. Quick Snapshot with minimal metrics
df = pd.read_csv("cleaned_air_quality.csv")
st.sidebar.markdown("### Statistics")
c1, c2 = st.sidebar.columns(2)
c1.metric("Cities", df['City'].nunique())
c2.metric("Records", f"{len(df)/1000:.1f}K")

st.sidebar.markdown("---")

# C. Navigation
st.sidebar.markdown("### Navigation")
app = MultiApp()
app.add_app("Overview", lambda: dataset_overview.app(df))
app.add_app("Analytics", lambda: eda.app(df))
app.add_app("Predictions", lambda: aqi_predcition.app())

app.run()

# D. Fixed Student ID at the very bottom
st.sidebar.markdown(
    """<div class="sidebar-footer">
        Student ID: 20341085
    </div>""", 
    unsafe_allow_html=True
)
