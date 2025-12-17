# import streamlit as st
# import pandas as pd
# from multi_app import MultiApp   # import your class

# import dataset_overview
# import eda
# import aqi_predcition   # fixed spelling

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

# ---------- Styling ----------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #f8f9fa;
}
.sidebar-title {
    background-color: #2e7d32;
    color: white;
    padding: 16px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 15px;
}
.sidebar-footer {
    font-size: 13px;
    color: gray;
    text-align: center;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load data ----------
df = pd.read_csv("cleaned_air_quality.csv")

# ---------- Sidebar ----------
st.sidebar.markdown(
    "<div class='sidebar-title'>🇮🇳 India Air Quality Analysis</div>",
    unsafe_allow_html=True
)

st.sidebar.markdown("### 📌 Navigation")

# ---------- MultiApp ----------
app = MultiApp()
app.add_app("📊 Dataset Overview", lambda: dataset_overview.app(df))
app.add_app("📈 EDA", lambda: eda.app(df))
app.add_app("🌍 AQI Prediction", lambda: aqi_predcition.app())

st.sidebar.markdown(
    "<div class='sidebar-footer'>👨‍🎓 Student ID<br><b>20341085</b></div>",
    unsafe_allow_html=True
)

# ---------- Run ----------
app.run()
