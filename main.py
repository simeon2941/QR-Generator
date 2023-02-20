import streamlit as st
import qrcode
from io import BytesIO

st.title("Website QR Code Generator")
url_input = st.text_input("Enter a website URL:")
generate_button = st.button("Generate QR Code")

# Generate the QR code when the "Generate QR Code" button is clicked
if generate_button and url_input:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url_input)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    st.image(img_bytes)
