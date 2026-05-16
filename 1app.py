import streamlit as st
import requests
from PIL import Image

# =========================
# 📱 SEITE EINSTELLEN
# =========================
st.set_page_config(
    page_title="Schadensaufnahme",
    layout="centered"
)

# =========================
# 🎨 DESIGN
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #f5f5f5;
}

/* Karten */
.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.1);
}

/* Buttons */
div.stButton > button {
    width: 100%;
    height: 55px;
