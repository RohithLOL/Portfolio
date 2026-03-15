import streamlit as st
banner= "https://cdn.esawebb.org/archives/images/screen/potm2410a.jpg"

def add_banner():
    st.markdown(f"""

    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bitcount+Single:CRSV@0&display=swap');
    
    header {{visibility: hidden;}}
    .banner {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 200px;
        z-index: 999;
    }}

    .banner img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}

    .banner-text {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }}
    .block-container {{
        padding-top: 200px;
    }}
    </style>

    <div class="banner">
        <img src="{banner}">
        <div class="banner-text">
            <h1 style="font-family:Bitcount Single;font-size: 55px">Rohith's Portfolio</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)
