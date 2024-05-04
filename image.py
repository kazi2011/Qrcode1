import streamlit as st 
from PIL import Image

img = Image.open("c:\Users\taham\OneDrive\Desktop\TAHSIN\Tahsin.PY\PYTHON\Myself.kz.jpg")
st.image(
    img ,
    caption = "Myself Qrcode",
    width = 400 ,
    channels = "RGB"
)
img1 = Image.open("c:\Users\taham\OneDrive\Desktop\TAHSIN\Tahsin.PY\PYTHON\Interview.kz.jpg")
st.image(
    img1 ,
    caption = "Interview Qrcode",
    width = 400 ,
    channels = "RGB"
)
