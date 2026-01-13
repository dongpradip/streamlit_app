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
    page_title="India Air Quality Analysis",
    page_icon="🍃",
    layout="wide",
)

# 2. CSS for Visibility and Positioning
st.markdown("""
    <style>
        /* Forces sidebar text to be dark for readability */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6;
            color: #1a1a1a !important;
        }
        
        /* Ensures labels and markdown are dark */
        [data-testid="stSidebar"] .stMarkdown p, 
        [data-testid="stSidebar"] label {
            color: #1a1a1a !important;
        }

        .sidebar-logo-box {
            background-color: #1E88E5;
            padding: 20px;
            border-radius: 15px;
            color: white !important; /* Keep logo text white */
            text-align: center;
            margin-bottom: 25px;
        }

        /* Styling for the bottom ID */
        .bottom-id {
            position: relative;
            text-align: center;
            padding: 10px;
            border-top: 1px solid #ddd;
            color: #555 !important;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---

# A. Branded Header
st.sidebar.markdown(
    """<div class="sidebar-logo-box">
        <h2 style='margin:0; color:white;'>🍃 AirDash</h2>
        <p style='margin:0; font-size:12px; opacity:0.8; color:white;'>India Air Quality Insights</p>
    </div>""", 
    unsafe_allow_html=True
)

# B. Quick Data Summary
df = pd.read_csv("cleaned_air_quality.csv")
st.sidebar.subheader("📊 Data Snapshot")
c1, c2 = st.sidebar.columns(2)
c1.metric("Cities", df['City'].nunique())
c2.metric("Records", f"{len(df)/1000:.1f}K")

st.sidebar.markdown("---")

# C. Navigation
st.sidebar.subheader("🧭 Main Navigation")
app = MultiApp()
app.add_app("📊 Dataset Overview", lambda: dataset_overview.app(df))
app.add_app("📈 Exploratory Analysis", lambda: eda.app(df))
app.add_app("🔮 AQI Prediction", lambda: aqi_predcition.app())

app.run()
