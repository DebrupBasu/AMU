# -*- coding: utf-8 -*-
"""
Created on Sat Dec 2 01:11:40 2023

@author: Debrup Basu
"""
import streamlit as st
from PIL import Image
import base64, io
import sys
import subprocess
st.markdown("""
    <style>
        .intrologo {
            position: absolute;
            top: -5px;
            left: -350px;
            width: 1200px;
            height: 750px;
            border: none; /* This removes the border */
        }
    </style>
""", unsafe_allow_html=True)

img = Image.open("img/Alliant-Avatars.png")
img = img.convert("RGB")
image_bytes = io.BytesIO()
img.save(image_bytes, format="JPEG")
image_base64 = base64.b64encode(image_bytes.getvalue()).decode()
# Create a container for the main content and logo
main_content_container = st.empty()
main_content_container.markdown(f'<img class="intrologo" src="data:image/jpg;base64,{image_base64}">', unsafe_allow_html=True)

# Title and introduction text
st.markdown("<h1 style='text-align: left;font-size: 20px; color: black;'>Introducing Ask My Underwriter! These virtual underwriting assistants are here to get instant, informed, and tailored responses to your title insurance questions.</h1>", unsafe_allow_html=True)

st.write("""
**Skip the wait, get expert underwriting answers.**

Ask My Underwriter leverages AI trained on Alliant's underwriters to tailor responses based on your chosen underwriter's unique insights.

No more waiting for emails – get the information you need, when you need it.
""")

# Create a button that executes alliant_underwriters.py
#import subprocess
st.markdown("[Open Ask My Underwriter](https://underwriters.streamlit.app/)")
    #subprocess.Popen(["streamlit", "run", "alliant_underwriters.py"])
    #subprocess.run([f"{sys.executable}", "alliant_underwriters.py"])
