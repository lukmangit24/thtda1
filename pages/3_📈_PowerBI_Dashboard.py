import streamlit as st

st.set_page_config(page_title="Operational Dashboard", layout="wide")

st.title("📈 Operational Dashboard (Power BI)")

st.markdown("""
Halaman ini menampilkan dashboard operasional yang dibuat menggunakan Microsoft Power BI.
Dashboard ini merangkum insight utama terkait performa pengiriman.
""")

st.divider()

st.image("assets/powerbi_dashboard.png", width="stretch")

st.caption(
    "Dashboard dibuat menggunakan Microsoft Power BI dan ditampilkan sebagai screenshot untuk kebutuhan portfolio."
)
