import streamlit as st

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

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=920, scrolling=False)
