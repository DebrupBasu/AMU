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

# Function to convert an image to base64
def image_to_base64(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    image_bytes = io.BytesIO()
    img.save(image_bytes, format="JPEG")
    return base64.b64encode(image_bytes.getvalue()).decode()

# List of image file names in the img/ directory
image_filenames = [
    "Tyrone- Arizona.jpg",
    "Jessica-NC.png",
    "Sheila-Missouri.png",
    "Jeffry-Florida.png",
    "Rayni- Texas.jpg",
    "Patrick- Georgia.jpg"
]

# List of image sources with names and locations
image_sources = [
    "[Name: Tyrone, Location: Arizona](https://askmyunderwriter.streamlit.app/)",
    "[Name: Jessica, Location: North Carolina](https://askmyunderwriter.streamlit.app/)",
    "[Name: Sheila, Location: Missouri](https://askmyunderwriter.streamlit.app/)",
    "[Name: Jeffry, Location: Florida](https://askmyunderwriter.streamlit.app/)",
    "[Name: Rayni, Location: Texas](https://askmyunderwriter.streamlit.app/)",
    "[Name: Patrick, Location: Georgia](https://askmyunderwriter.streamlit.app/)"
]

# Display images and corresponding markdown links in the same row and column
st.markdown("<h3 style='font-size:24px; font-weight:bold;'>Connect With Your Underwriter Ally: Choose the Key to Your Insurance Success!</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

for i, image_filename in enumerate(image_filenames):
    if i % 4 == 0:
        col = col1
    elif i % 4 == 1:
        col = col2
    elif i % 4 == 2:
        col = col3
    else:
        col = col4

    with col:
        # Convert the image to base64
        image_path = f"img/{image_filename}"
        image_base64 = image_to_base64(image_path)

        # Create a hovering effect and make the image clickable
        image_html = f'<a href="https://askmyunderwriter.streamlit.app/" target="_blank"><img src="data:image/jpg;base64,{image_base64}" style="width:100%; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); transition: transform 0.3s;"></a>'
        st.markdown(image_html, unsafe_allow_html=True)
        st.markdown(image_sources[i])


