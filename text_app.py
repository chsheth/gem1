import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Text data

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini LLM Application")
st.header("Gemini LLM Application - Q&A Demo")

input = st.text_input("Please ask a question: ", key="input")
submit = st.button("Submit")

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)

