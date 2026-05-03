import requests
import streamlit as st
import time
from Banner import add_banner

st.set_page_config(layout="centered")

add_banner()

st.title("hi i am Rohith")
coolPic = st.container()

if st.button("Home"):
    st.switch_page("streamlit_app.py")
if st.button("Page 1"):
    st.switch_page("pages/one.py")

with coolPic: 
    with st.spinner("Loading files"):
        url = ""
        #response = requests.get(url)
        #coolPic = st.image(response.content)
        time.sleep(0.5)