# import streamlit as st
# import pandas as pd

# def app(df):
#   st.header("Dataset Overview")

#   st.write("Dataset Shape:", df.shape)
#   st.dataframe(df.head())

#   st.subheader("Data Types")
#   st.write(df.dtypes)

#   st.subheader("Summary Statistics")
#   st.write(df.describe())


# import streamlit as st
# import pandas as pd

# def app(df):
#     st.header("Dataset Overview")

#     st.write("Dataset Shape:", df.shape)

#     # FIX STARTS HERE
#     df_display = df.copy()

#     for col in df_display.columns:
#         if df_display[col].dtype == "object":
#             df_display[col] = df_display[col].astype(str)

#     st.dataframe(df_display.head())
#     # FIX ENDS HERE

#     st.subheader("Data Types")
#     st.write(df.dtypes)

#     st.subheader("Summary Statistics")
#     st.write(df.describe())

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app(df):
    st.title("📊 Dataset Overview")

    # ----------- TOP METRICS -----------
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))
    col4.metric("Duplicate Rows", int(df.duplicated().sum()))

    st.markdown("---")

    # ----------- TABS -----------
    tab1, tab2, tab3, tab4 = st.tabs(
        ["🔍 Data Preview", "🧠 Column Info", "📈 Summary Stats", "📊 Visualizations"]
    )

    # ----------- TAB 1 : DATA PREVIEW -----------
    with tab1:
        st.subheader("Dataset Preview")
        df_display = df.copy()
        for col in df_display.columns:
            if df_display[col].dtype == "object":
                df_display[col] = df_display[col].astype(str)
        st.dataframe(df_display, use_container_width=True, height=400)

        # Optional: select a column to see unique values
        col_select = st.selectbox("Select a column to explore unique values", df.columns)
        st.write(df[col_select].value_counts().head(10))

    # ----------- TAB 2 : COLUMN INFO -----------
    with tab2:
        st.subheader("Column Information")
        dtype_df = df.dtypes.reset_index().rename(columns={"index": "Column", 0: "Data Type"})
        st.dataframe(dtype_df, use_container_width=True)

        # Missing values per column
        st.subheader("Missing Values per Column")
        missing_df = df.isnull().sum().reset_index().rename(columns={"index": "Column", 0: "Missing Values"})
        missing_df["% Missing"] = (missing_df["Missing Values"] / df.shape[0] * 100).round(2)
        st.dataframe(missing_df, use_container_width=True)

    # ----------- TAB 3 : SUMMARY STATS -----------
    with tab3:
        st.subheader("Numeric Columns Summary")
        st.dataframe(df.describe(), use_container_width=True)

        st.subheader("Categorical Columns Summary")
        cat_cols = df.select_dtypes(include="object").columns
        if len(cat_cols) > 0:
            cat_summary = pd.DataFrame({
                "Column": cat_cols,
                "Unique Values": [df[col].nunique() for col in cat_cols],
                "Top Value": [df[col].mode()[0] if not df[col].mode().empty else None for col in cat_cols],
                "Frequency": [df[col].value_counts().max() for col in cat_cols]
            })
            st.dataframe(cat_summary, use_container_width=True)

    # ----------- TAB 4 : VISUALIZATIONS -----------
    with tab4:
        st.subheader("Missing Value Heatmap")
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap="viridis", ax=ax)
        st.pyplot(fig)

        st.subheader("Numeric Column Distributions")
        num_cols = df.select_dtypes(include="number").columns
        for col in num_cols:
            st.write(f"**{col}**")
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax, color="skyblue")
            st.pyplot(fig)

        st.subheader("Correlation Heatmap")
        if len(num_cols) > 1:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.write("Not enough numeric columns for correlation heatmap.")
