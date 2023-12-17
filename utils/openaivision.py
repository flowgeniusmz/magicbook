import requests
import streamlit as st

def call_openai_vision(varMessages):
    url = st.secrets.openai.url_vision
    model = st.secrets.openai.model_vision
    auth = f"Bearer {st.secrets.openai.api_key}"
    ctype = "application/json"

    headers = {
        "Authorization": auth,
        "Content-Type": ctype
    }

    payload = {
        "model": model,
        "max_tokens": 300,
        "messages": varMessages
    }

    response = requests.post(url=url, json=payload)

    response_json = response.json()

    return response_json