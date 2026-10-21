import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Naqi Rustam Bajwa",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit ka apna header, menu, footer aur padding chhupao
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      iframe {display: block; height: 100vh !important; width: 100% !important; border: 0;}
      body {overflow: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

with open("index.html", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=1000, scrolling=True)
