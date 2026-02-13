import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="EDA Analysis", layout="wide")

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("data/Zomato Dataset.csv")

# ======================
# DATA CLEANING
# ======================
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d-%m-%Y')

df['order_hour'] = pd.to_datetime(
    df['Time_Orderd'],
    format='%H:%M',
    errors='coerce'
).dt.hour

df['order_hour'] = df['order_hour'].fillna(df['order_hour'].median())

df = df.drop(columns=['Time_Orderd', 'Time_Order_picked'], errors='ignore')

num_cols = ['Delivery_person_Age','Delivery_person_Ratings','multiple_deliveries']
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

cat_cols = ['Weather_conditions','Road_traffic_density','Festival','City']
for col in cat_cols:
    df[col] = df[col].fillna('Unknown')

# ======================
# SIDEBAR FILTER
# ======================
st.sidebar.header("🔎 Filter")

traffic_filter = st.sidebar.multiselect(
    "Select Traffic Density",
    df["Road_traffic_density"].unique(),
    default=df["Road_traffic_density"].unique()
)

df = df[df["Road_traffic_density"].isin(traffic_filter)]

# ======================
# TITLE
# ======================
st.title("📊 Exploratory Data Analysis")
st.markdown("Comprehensive operational analysis of delivery performance.")

# ======================
# KPI SECTION
# ======================
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", len(df))
col2.metric("Avg Delivery Time", f"{df['Time_taken (min)'].mean():.2f} min")
col3.metric("Max Delivery Time", f"{df['Time_taken (min)'].max()} min")
col4.metric("Avg Courier Rating", f"{df['Delivery_person_Ratings'].mean():.2f}")

st.divider()

# ======================
# DISTRIBUTION
# ======================
colA, colB = st.columns(2)

with colA:
    st.subheader("⏱ Delivery Time Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(df['Time_taken (min)'], bins=25, kde=True, ax=ax1)
    st.pyplot(fig1)

    st.markdown("""
    **Insight:**
    - Mayoritas pengiriman berada pada rentang 20–40 menit.
    - Distribusi cenderung right-skewed, menunjukkan adanya pengiriman dengan delay ekstrem.
    - Variabilitas tinggi mengindikasikan ketidakstabilan operasional.
    """)

with colB:
    st.subheader("🚦 Traffic Impact")
    traffic_order = ['Low','Medium','High','Jam']
    avg_traffic = (
        df.groupby('Road_traffic_density')['Time_taken (min)']
        .mean()
        .reindex(traffic_order)
    )

    fig2, ax2 = plt.subplots()
    avg_traffic.plot(kind='bar', ax=ax2)
    ax2.set_ylabel("Average Delivery Time (min)")
    st.pyplot(fig2)

    st.markdown("""
    **Insight:**
    - Waktu pengiriman meningkat konsisten dari Low → Jam.
    - Traffic merupakan faktor operasional paling dominan.
    - Perlu strategi alokasi kurir tambahan saat peak traffic.
    """)

st.divider()

# ======================
# HOUR & WEATHER
# ======================
colC, colD = st.columns(2)

with colC:
    st.subheader("🕒 Order Hour Impact")
    avg_hour = df.groupby('order_hour')['Time_taken (min)'].mean()

    fig3, ax3 = plt.subplots()
    ax3.plot(avg_hour.index, avg_hour.values)
    ax3.set_xlabel("Order Hour")
    ax3.set_ylabel("Average Delivery Time")
    st.pyplot(fig3)

    st.markdown("""
    **Insight:**
    - Peak hour menunjukkan peningkatan delivery time.
    - Lonjakan volume order menyebabkan bottleneck operasional.
    - Dynamic rider allocation dapat membantu mengurangi delay.
    """)

with colD:
    st.subheader("🌦 Weather Impact")
    avg_weather = (
        df.groupby('Weather_conditions')['Time_taken (min)']
        .mean()
        .sort_values()
    )

    fig4, ax4 = plt.subplots()
    ax4.barh(avg_weather.index, avg_weather.values)
    ax4.set_xlabel("Average Delivery Time")
    st.pyplot(fig4)

    st.markdown("""
    **Insight:**
    - Cuaca buruk seperti Stormy atau Fog meningkatkan waktu pengiriman.
    - Sistem estimasi waktu perlu mempertimbangkan variabel cuaca secara real-time.
    """)

st.divider()

# ======================
# MULTIPLE & CORRELATION
# ======================
colE, colF = st.columns(2)

with colE:
    st.subheader("📦 Multiple Deliveries Impact")
    avg_multi = df.groupby('multiple_deliveries')['Time_taken (min)'].mean()

    fig5, ax5 = plt.subplots()
    ax5.bar(avg_multi.index.astype(str), avg_multi.values)
    ax5.set_xlabel("Number of Deliveries")
    ax5.set_ylabel("Average Time")
    st.pyplot(fig5)

    st.markdown("""
    **Insight:**
    - Semakin banyak delivery sekaligus, durasi pengiriman meningkat.
    - Terdapat trade-off antara efisiensi biaya dan kecepatan layanan.
    """)

with colF:
    st.subheader("🔥 Correlation Heatmap")
    corr_cols = [
        'Delivery_person_Age',
        'Delivery_person_Ratings',
        'multiple_deliveries',
        'order_hour',
        'Time_taken (min)'
    ]

    corr_matrix = df[corr_cols].corr()

    fig6, ax6 = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax6)
    st.pyplot(fig6)

    st.markdown("""
    **Insight:**
    - multiple_deliveries memiliki korelasi positif terhadap delivery time.
    - Rating kurir berkorelasi negatif (rating tinggi → pengiriman lebih cepat).
    - Faktor operasional lebih dominan dibanding faktor personal.
    """)

st.divider()

st.success("EDA menunjukkan bahwa traffic density, multiple deliveries, dan peak hour merupakan faktor utama yang memengaruhi waktu pengiriman.")
