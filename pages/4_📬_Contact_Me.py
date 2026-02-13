import streamlit as st
import requests


st.title("📬 Contact Me")

st.write("""
Feel free to reach out for collaboration, opportunities, or discussion.
""")

st.write("""
📧 Email: lukmnaja24@gmail.com  
🔗 GitHub: https://github.com/lukmangi24  
💼 LinkedIn: https://linkedin.com/in/muhammad-lukmanul-hakim
""")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

# =============================
# Google Form Config
# =============================
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdS7HaI3dVSLlO0wi-k0inPKiNRiwlkhNkVThCsSf38ia3OwA/formResponse"

ENTRY_NAME = "entry.554957823"
ENTRY_EMAIL = "entry.99138585"
ENTRY_MESSAGE = "entry.107615171"

# =============================
# Submit
# =============================
if st.button("Kirim"):
    if name and email and message:
        payload = {
            ENTRY_NAME: name,
            ENTRY_EMAIL: email,
            ENTRY_MESSAGE: message
        }

        response = requests.post(FORM_URL, data=payload)

        if response.status_code == 200:
            st.success("✅ Message sent successfully. Thank you. 🙌")
        else:
            st.error("❌ Failed to send message. Please try again.")
    else:
        st.warning("⚠️ Please complete all fields")
st.info("Thank you for visiting this project 🙌")