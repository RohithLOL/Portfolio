import requests
import streamlit as st
import time
from streamlit_js_eval import streamlit_js_eval

image_path = "https://cdn.esawebb.org/archives/images/screen/potm2410a.jpg"

st.markdown(
    f"""
    <body>
    <img src={image_path}>
    </body>
    """,
    unsafe_allow_html=True
)


coolPic = st.container()

if st.button("Home"):
    st.switch_page("streamlit_app.py")
if st.button("Page 1"):
    st.switch_page("pages/one.py")

with coolPic: 
    with st.spinner("Loading files"):
        url = "https://drive.google.com/uc?export=view&id=1UX1ORnpUj87_3CmLZu9C4KSs1WdFJi_C"
        response = requests.get(url)
        coolPic = st.image(response.content)
        time.sleep(0.5)