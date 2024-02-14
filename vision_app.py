import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Text & Vision data

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini LLM Application")

st.header("Gemini LLM Application - Vision Demo")

input = st.text_input("Please ask a question: ", key="input")
uploaded_file = st.file_uploader("Choose an image to upload",type=["jpg", "jpeg", "png"])

image=""
if uploaded_file:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Submit")

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is ")
    st.write(response)
