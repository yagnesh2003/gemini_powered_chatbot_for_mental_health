from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# fundtion to load geminin model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text