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

# 2. Advanced Styling for Sidebar (No-Logo Design)
st.markdown("""
    <style>
        /* This styles the sidebar top area */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6;
        }
        
        /* Create a "Logo" box using CSS */
        .sidebar-logo-box {
            background-color: #1E88E5; /* Professional Blue */
            padding: 20px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        
        .student-id-text {
            font-size: 0.85rem;
            color: #555;
            text-align: center;
            border-bottom: 1px solid #ddd;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---

# A. Styled Header (Acts as your "Logo")
st.sidebar.markdown(
    """<div class="sidebar-logo-box">
        <h2 style='margin:0; color:white;'>🍃 AirDash</h2>
        <p style='margin:0; font-size:12px; opacity:0.8;'>India Air Quality Insights</p>
    </div>""", 
    unsafe_allow_html=True
)

# B. Student Info (Subtle and clean)
st.sidebar.markdown(f'<p class="student-id-text">🎓 Student ID: <b>20341085</b></p>', unsafe_allow_html=True)

# C. Quick Data Summary
df = pd.read_csv("cleaned_air_quality.csv")
with st.sidebar.container():
    st.markdown("🔍 **Data Snapshot**")
    c1, c2 = st.columns(2)
    c1.metric("Cities", df['City'].nunique())
    # Display record count in thousands (K) for a cleaner look
    c2.metric("Records", f"{len(df)/1000:.1f}K")
    st.sidebar.markdown("---")

# --- APP LOGIC ---
st.sidebar.markdown("### 🧭 Main Navigation")
app = MultiApp()

# Added emojis to labels to make them look like buttons
app.add_app("📊 Dataset Overview", lambda: dataset_overview.app(df))
app.add_app("📈 Exploratory Analysis", lambda: eda.app(df))
app.add_app("🔮 AQI Prediction", lambda: aqi_predcition.app())

# Run the app
app.run()
