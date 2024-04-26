import streamlit as st
from PIL import Image
import base64
import io
import subprocess

from streamlit_image_select import image_select

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

img = Image.open("img/Alliant_Avatars.png")
img = img.convert("RGB")
image_bytes = io.BytesIO()
img.save(image_bytes, format="JPEG")
image_base64 = base64.b64encode(image_bytes.getvalue()).decode()
# Create a container for the main content and logo
main_content_container = st.empty()
main_content_container.markdown(f'<img class="intrologo" src="data:image/jpg;base64,{image_base64}">', unsafe_allow_html=True)

# Define image data (assuming each underwriter has one image)
image_sources = [
  "[Name: Tyrone, Location: Arizona](https://askmyunderwriter-chatbot.streamlit.app/)",
  "[Name: Jessica, Location: North Carolina](https://askmyunderwriter-chatbot.streamlit.app/)",
  "[Name: Sheila, Location: Missouri](https://askmyunderwriter-chatbot.streamlit.app/)",
  "[Name: Jeffry, Location: Florida](https://askmyunderwriter-chatbot.streamlit.app/)",
  "[Name: Rayni, Location: Texas](https://askmyunderwriter-chatbot.streamlit.app/)",
  "[Name: Patrick, Location: Georgia](https://askmyunderwriter-chatbot.streamlit.app/)"
]

# Load images and convert to base64 encoded strings
image_urls = [
  Image.open("img/Tyrone- Arizona.jpg"),
  Image.open("img/Jessica- NC.jpg"),
  Image.open("img/Sheila- Missouri.jpg"),
  Image.open("img/Jeffry- Florida.jpg"),
  Image.open("img/Rayni- Texas.jpg"),
  Image.open("img/Patrick- Georgia.jpg")
]

st.markdown("<h3 style='font-size:24px; font-weight:bold;'>Connect With Your Underwriter Ally: Choose the Key to Your Insurance Success!</h3>", unsafe_allow_html=True)

selected_underwriter = image_select(
   label="",
   images=image_urls,
   captions=image_sources,
   use_container_width=False,
   unsafe_allow_html=True 
 )


# On selecting an underwriter execute alliant_chatbot_pdf_V2.py
#if selected_underwriter:
#    st.markdown("[Click here to open the chatbot](https://askmyunderwriter-chatbot.streamlit.app/)")

