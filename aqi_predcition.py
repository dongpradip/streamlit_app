import streamlit as st
import pandas as pd
import joblib

# -------- Load models only once --------
@st.cache_resource
def load_models():
    return (
        joblib.load("aqi_rfmodel.pkl"),
        joblib.load("aqi_rfcmodel.pkl")
    )

aqi_model, bucket_model = load_models()

# AQI bucket mapping
aqi_bucket_map = {
    0: "Good",
    1: "Satisfactory",
    2: "Moderate",
    3: "Poor",
    4: "Very Poor",
    5: "Severe"
}

def app():
    st.markdown("""
    <style>
    .title {font-size:42px; font-weight:700; text-align:center;}
    .subtitle {text-align:center; color:gray; margin-bottom:30px;}
    .card {background:#f6f6f6; padding:20px; border-radius:14px;}
    .result {background:#eaeaea; padding:30px; border-radius:18px; text-align:center;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🌍 Air Quality Prediction</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Predict AQI value and AQI category</div>", unsafe_allow_html=True)

    with st.form("aqi_form"):
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        PM25 = c1.number_input("PM2.5 (µg/m³)", min_value=0.0)
        PM10 = c2.number_input("PM10 (µg/m³)", min_value=0.0)
        NO   = c3.number_input("NO (µg/m³)", min_value=0.0)

        c4, c5, c6 = st.columns(3)
        NO2 = c4.number_input("NO₂ (µg/m³)", min_value=0.0)
        NOx = c5.number_input("NOx (µg/m³)", min_value=0.0)
        NH3 = c6.number_input("NH₃ (µg/m³)", min_value=0.0)

        c7, c8, c9 = st.columns(3)
        CO  = c7.number_input("CO (mg/m³)", min_value=0.0)
        SO2 = c8.number_input("SO₂ (µg/m³)", min_value=0.0)
        O3  = c9.number_input("O₃ (µg/m³)", min_value=0.0)

        c10, c11, c12 = st.columns(3)
        Benzene = c10.number_input("Benzene (µg/m³)", min_value=0.0)
        Toluene = c11.number_input("Toluene (µg/m³)", min_value=0.0)
        Xylene  = c12.number_input("Xylene (µg/m³)", min_value=0.0)

        submitted = st.form_submit_button("🔍 Predict Air Quality")
        st.markdown("</div>", unsafe_allow_html=True)

    if submitted:
        input_df = pd.DataFrame([{
            "PM2.5": PM25,
            "PM10": PM10,
            "NO": NO,
            "NO2": NO2,
            "NOx": NOx,
            "NH3": NH3,
            "CO": CO,
            "SO2": SO2,
            "O3": O3,
            "Benzene": Benzene,
            "Toluene": Toluene,
            "Xylene": Xylene
        }])

        input_df = input_df[aqi_model.feature_names_in_]

        predicted_aqi = aqi_model.predict(input_df)[0]
        bucket_num = bucket_model.predict(input_df)[0]
        predicted_bucket = aqi_bucket_map[bucket_num]

        st.markdown("### 📊 Prediction Results")

        col1, col2 = st.columns(2)
        col1.markdown(
            f"<div class='result'>📈 AQI<br><h1>{predicted_aqi:.2f}</h1></div>",
            unsafe_allow_html=True
        )
        col2.markdown(
            f"<div class='result'>🏷 Category<br><h1>{predicted_bucket}</h1></div>",
            unsafe_allow_html=True
        )
