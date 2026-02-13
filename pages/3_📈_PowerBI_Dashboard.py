import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Operational Dashboard", layout="wide")

st.title("📈 Operational Dashboard (Power BI)")

st.markdown("""
Halaman ini menampilkan dashboard operasional yang dibuat menggunakan Microsoft Power BI.
Dashboard ini merangkum insight utama terkait performa pengiriman.
""")

st.divider()

# ======================
# LOAD SCREENSHOT (SAFE VERSION)
# ======================
image_path = os.path.join("assets", "powerbi_dashboard.png")

if os.path.exists(image_path):
    st.image(image_path, width="stretch")  # replace deprecated parameter
else:
    st.error("Image file not found. Please check assets folder.")

st.caption("Dashboard dibuat menggunakan Microsoft Power BI dan ditampilkan sebagai screenshot untuk kebutuhan portfolio.")
