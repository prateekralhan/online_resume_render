import os
import base64
import streamlit as st

st.set_page_config(
    page_title="Prateek Ralhan | Resume",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:ralhanprateek@gmail.com',
        'About': "### This webpage is just an online rendered view of my resume."
    }
)

@st.cache_data()
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data()
def render_pdf(file):
    # Opening file from file path
    with open(os.path.abspath(os.path.join("resume/", file)), "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = f'<div style="display: flex; justify-content: center; align-items: center; height: 100vh;"><embed src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="80%" height="100%" type="application/pdf"></div>' 

    return pdf_display


bg_img = "assets/background.jpg"
file_name = "Prateek_Ralhan.pdf"

img = get_img_as_base64("assets/background.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 120%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

with st.container():
    pdf_display = render_pdf(file_name)
    st.markdown(pdf_display, unsafe_allow_html=True)

st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)