import streamlit as st
import os

st.set_page_config(
    page_title="GlobalFin — Markets Dashboard",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit chrome
st.markdown("""
<style>
#MainMenu, header, footer { display: none !important; }
.block-container { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# Get the directory where app.py lives and load index.html from same folder
base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=920, scrolling=False)
