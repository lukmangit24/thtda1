import streamlit as st

st.set_page_config(
    page_title="Analisis Kinerja Pengiriman Zomato",
    layout="wide"
)

# =============================
# HEADER
# =============================

st.title("📦 Analisis Kinerja Pengiriman Zomato")
st.caption("Proyek Analisis Data End-to-End (EDA, Uji Hipotesis, Dashboard BI)")

st.markdown("---")

# =============================
# LATAR BELAKANG
# =============================

st.header("📌 Latar Belakang")

st.markdown("""
Platform pengantaran makanan online sangat bergantung pada efisiensi operasional 
untuk menjaga kepuasan pelanggan.

Salah satu indikator kinerja paling penting adalah **waktu pengiriman**.

Keterlambatan pengiriman dapat menyebabkan:

- Penurunan kepuasan pelanggan  
- Rating aplikasi menurun  
- Berkurangnya repeat order  
- Inefisiensi operasional  

Memahami faktor-faktor yang memengaruhi waktu pengiriman sangat penting 
untuk meningkatkan performa layanan.
""")

# =============================
# RUMUSAN MASALAH
# =============================

st.header("❗ Rumusan Masalah")

st.markdown("""
Meskipun volume pesanan tinggi, waktu pengiriman menunjukkan variasi yang signifikan.

Pertanyaan bisnis utama:

1. Apakah kepadatan lalu lintas berpengaruh signifikan terhadap waktu pengiriman?
2. Seberapa kuat hubungan antara jarak pengiriman dan durasi pengiriman?
3. Apakah jenis kendaraan memengaruhi efisiensi operasional?
4. Faktor operasional apa yang paling memengaruhi keterlambatan pengiriman?
""")

# =============================
# TUJUAN PROYEK
# =============================

st.header("🎯 Tujuan Proyek")

st.markdown("""
Tujuan utama dari proyek ini adalah:

- Menganalisis faktor-faktor yang memengaruhi waktu pengiriman  
- Melakukan uji hipotesis statistik (ANOVA)  
- Mengidentifikasi bottleneck operasional  
- Memberikan rekomendasi bisnis berbasis data  
- Membangun dashboard interaktif untuk monitoring performa  
""")

# =============================
# DESKRIPSI DATASET
# =============================

st.header("📊 Gambaran Dataset")

st.markdown("""
Dataset ini berisi data operasional pengiriman yang mencakup:

- Waktu pengiriman (Variabel Target)  
- Kepadatan lalu lintas  
- Koordinat lokasi pengiriman  
- Jenis kendaraan  
- Jenis pesanan  
- Kondisi cuaca  
- Rating kurir  

Analisis difokuskan untuk memahami bagaimana variabel-variabel tersebut 
memengaruhi durasi pengiriman.
""")

st.markdown("---")

st.info("Gunakan sidebar untuk menjelajahi EDA, Uji Hipotesis, dan Dashboard Power BI.")
