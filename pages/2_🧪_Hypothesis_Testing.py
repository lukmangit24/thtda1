import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

st.set_page_config(page_title="Uji Hipotesis", layout="wide")

st.title("🧪 Uji Hipotesis - One Way ANOVA")

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("data/Zomato Dataset.csv")

df = df.dropna(subset=["Time_taken (min)", "Road_traffic_density"])

# ======================
# PENJELASAN
# ======================
st.markdown("""
### 📌 Tujuan Pengujian
Analisis ini menggunakan **One-Way ANOVA** untuk mengetahui apakah terdapat 
perbedaan rata-rata waktu pengiriman yang signifikan berdasarkan tingkat kepadatan lalu lintas.

### 🎯 Hipotesis Statistik
- **H0 (Hipotesis Nol):** Tidak terdapat perbedaan rata-rata waktu pengiriman pada setiap tingkat kepadatan lalu lintas.
- **H1 (Hipotesis Alternatif):** Minimal terdapat satu tingkat kepadatan lalu lintas dengan rata-rata waktu pengiriman yang berbeda secara signifikan.
""")

st.divider()

# ======================
# KELOMPOK DATA
# ======================
low = df[df['Road_traffic_density'] == 'Low']['Time_taken (min)']
medium = df[df['Road_traffic_density'] == 'Medium']['Time_taken (min)']
high = df[df['Road_traffic_density'] == 'High']['Time_taken (min)']
jam = df[df['Road_traffic_density'] == 'Jam']['Time_taken (min)']

# ======================
# UJI ANOVA
# ======================
f_stat, p_value = f_oneway(low, medium, high, jam)

st.subheader("📊 Hasil Uji ANOVA")

col1, col2 = st.columns(2)

col1.metric("F-statistic", round(f_stat, 3))
col2.metric("p-value", f"{p_value:.6f}")

st.divider()

# ======================
# INTERPRETASI
# ======================
st.subheader("📌 Interpretasi Hasil")

if p_value < 0.05:
    st.success("""
    Nilai p-value lebih kecil dari 0.05.
    Maka kita menolak hipotesis nol (H0).
    
    ✅ Terdapat perbedaan yang signifikan secara statistik pada waktu pengiriman 
    berdasarkan tingkat kepadatan lalu lintas.
    """)
else:
    st.warning("""
    Nilai p-value lebih besar atau sama dengan 0.05.
    Maka kita gagal menolak hipotesis nol (H0).
    
    ❌ Tidak ditemukan perbedaan yang signifikan.
    """)

st.divider()

# ======================
# VISUALISASI
# ======================
st.subheader("📦 Distribusi Waktu Pengiriman Berdasarkan Kepadatan Lalu Lintas")

fig, ax = plt.subplots()
sns.boxplot(data=df, x="Road_traffic_density", y="Time_taken (min)", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.divider()

# ======================
# INSIGHT BISNIS
# ======================
st.subheader("💡 Insight Bisnis")

st.markdown("""
Jika kepadatan lalu lintas terbukti berpengaruh signifikan terhadap waktu pengiriman, maka perusahaan dapat:

- Menyesuaikan estimasi waktu pengiriman secara dinamis  
- Menambah jumlah kurir saat jam dengan traffic tinggi  
- Mengoptimalkan strategi routing  
- Meningkatkan komunikasi kepada pelanggan saat kondisi lalu lintas padat  

Analisis ini mendukung pengambilan keputusan operasional berbasis data.
""")
