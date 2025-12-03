import os
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()

def load_api():
    api_key = None

    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    elif os.getenv("GOOGLE_API_KEY"):
        api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        st.error("GOOGLE_API_KEY not found in st.secrets or .env/env variables.")
        st.stop()

    os.environ["GOOGLE_API_KEY"] = api_key