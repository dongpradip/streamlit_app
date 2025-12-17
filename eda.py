# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px

# def app(df):
#     st.header("Exploratory Data Analysis")

#     option = st.selectbox(
#         "Choose Analysis",
#         [
#             "AQI Trend Over Time",
#             "AQI Bucket Distribution",
#             "Top 5 Polluted Cities"
#         ]
#     )

#     if option == "AQI Trend Over Time":
#         df['Date'] = pd.to_datetime(df['Date'])
#         trend = df.groupby('Date')['AQI'].mean().reset_index()

#         fig, ax = plt.subplots(figsize=(10, 5))
#         sns.lineplot(data=trend, x='Date', y='AQI', ax=ax)
#         st.pyplot(fig)

#     elif option == "AQI Bucket Distribution":
#         fig, ax = plt.subplots()
#         sns.countplot(
#             data=df,
#             x='AQI_Bucket',
#             order=['Good','Satisfactory','Moderate','Poor','Very Poor','Severe'],
#             ax=ax
#         )
#         st.pyplot(fig)

#     else:
#         top5 = df.groupby('City')['AQI'].mean().sort_values(ascending=False).head(5).index
#         df_top5 = df[df['City'].isin(top5)]

#         fig = px.sunburst(
#             df_top5,
#             path=['City', 'AQI_Bucket'],
#             values='AQI',
#             title="AQI Distribution in Top 5 Polluted Cities"
#         )
#         st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def app(df):
    st.header("📊 Exploratory Data Analysis with Multi-Pollutant Filter")

    # Ensure Date is datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    # Sidebar filters
    st.sidebar.header("Filters")
    cities = df['City'].unique().tolist()
    selected_cities = st.sidebar.multiselect("Select City/Cities", options=cities, default=cities[:3])

    # Pollutants excluding AQI
    pollutants = [col for col in df.columns if col not in ['Date','City','AQI','AQI_Bucket']]
    selected_pollutants = st.sidebar.multiselect("Select Pollutant(s)", options=pollutants, default=pollutants[:2])

    df_filtered = df[df['City'].isin(selected_cities)]

    # Tabs for charts
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📈 Trend Over Time",
        "🟢 AQI Bucket Distribution",
        "📊 Boxplots",
        "🌡️ Heatmap",
        "📉 Correlation Matrix",
        "🥧 Pie Chart of AQI Buckets",
        "🏢 Average Pollutant by City",
        "🎻 Violin Plots"
    ])

    # --------- Trend Over Time ---------
    with tab1:
        st.subheader("Trend of Selected Pollutants Over Time")
        for pollutant in selected_pollutants:
            trend = df_filtered.groupby('Date')[pollutant].mean().reset_index()
            fig, ax = plt.subplots(figsize=(12,4))
            sns.lineplot(data=trend, x='Date', y=pollutant, marker='o', ax=ax)
            ax.set_title(f"{pollutant} Trend Over Time")
            ax.set_ylabel(pollutant)
            st.pyplot(fig)

    # --------- AQI Bucket Distribution ---------
    with tab2:
        st.subheader("🟢 AQI Bucket Distribution")
        if 'AQI_Bucket' in df_filtered.columns:
            fig = px.histogram(
                df_filtered,
                x='AQI_Bucket',
                color='AQI_Bucket',
                category_orders={'AQI_Bucket':['Good','Satisfactory','Moderate','Poor','Very Poor','Severe']},
                title="AQI Bucket Distribution",
                color_discrete_sequence=px.colors.sequential.Viridis
            )
            st.plotly_chart(fig)
        else:
            st.warning("AQI_Bucket column not found.")

    # --------- Boxplots ---------
    with tab3:
        st.subheader("Boxplots of Selected Pollutants by City")
        for pollutant in selected_pollutants:
            fig, ax = plt.subplots(figsize=(12,5))
            sns.boxplot(data=df_filtered, x='City', y=pollutant, palette='Set2', ax=ax)
            ax.set_title(f"{pollutant} Distribution per City")
            plt.xticks(rotation=45)
            st.pyplot(fig)

    # --------- Heatmap ---------
    with tab4:
        st.subheader("Heatmaps of Selected Pollutants")
        for pollutant in selected_pollutants:
            pivot = df_filtered.pivot_table(index='City', columns='Date', values=pollutant, aggfunc='mean')
            fig, ax = plt.subplots(figsize=(12,5))
            sns.heatmap(pivot, cmap='YlOrRd', linecolor='white', linewidths=0.1)
            ax.set_title(f"{pollutant} Heatmap: City vs Date")
            st.pyplot(fig)

    # --------- Correlation Matrix ---------
    with tab5:
        st.subheader("Correlation Matrix of Selected Pollutants")
        if len(selected_pollutants) > 1:
            corr = df_filtered[selected_pollutants].corr()
            fig, ax = plt.subplots(figsize=(10,6))
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
            ax.set_title("Correlation Matrix")
            st.pyplot(fig)
        else:
            st.write("Select at least 2 pollutants for correlation matrix.")

    # --------- Pie Chart of AQI Buckets ---------
    with tab6:
        st.subheader("Pie Chart of AQI Buckets")
        if 'AQI_Bucket' in df_filtered.columns:
            bucket_counts = df_filtered['AQI_Bucket'].value_counts().reset_index()
            bucket_counts.columns = ['AQI_Bucket', 'Count']
            fig = px.pie(bucket_counts, values='Count', names='AQI_Bucket',
                         color='AQI_Bucket',
                         color_discrete_map={
                             'Good':'green','Satisfactory':'lime','Moderate':'yellow',
                             'Poor':'orange','Very Poor':'red','Severe':'darkred'
                         },
                         title="Proportion of AQI Buckets")
            st.plotly_chart(fig)
        else:
            st.warning("AQI_Bucket column not found.")

    # --------- Average Pollutant by City ---------
    with tab7:
        st.subheader("Average Levels by City")
        for pollutant in selected_pollutants:
            avg_city = df_filtered.groupby('City')[pollutant].mean().reset_index()
            fig = px.bar(avg_city, x='City', y=pollutant, text=pollutant,
                         color=pollutant, color_continuous_scale='Viridis',
                         title=f"Average {pollutant} by City")
            fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
            st.plotly_chart(fig)

    # --------- Violin Plots ---------
    with tab8:
        st.subheader("Violin Plots of Selected Pollutants")
        for pollutant in selected_pollutants:
            fig, ax = plt.subplots(figsize=(12,5))
            sns.violinplot(data=df_filtered, x='City', y=pollutant, palette='Set3', ax=ax)
            ax.set_title(f"{pollutant} Distribution per City")
            plt.xticks(rotation=45)
            st.pyplot(fig)

    # Footer
    st.markdown("---")
    st.markdown("💡 **Tip:** Use sidebar filters to explore multiple cities and pollutants interactively.")
