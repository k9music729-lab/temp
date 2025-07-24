import requests
import json
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = st.secrets["api_key"]

url = "https://openrouter.ai/api/v1/chat/completions"

st.write("API Key Loaded:", bool(api_key))

headers = {
    "Authorization": api_key,  # ✅ Add 'Bearer ' prefix
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-site.com",  # Optional
    "X-Title": "TestApp"                     # Optional
}

story=st.text_input('Enter some text')

payload = {
    "model": "mistralai/mistral-small-3.2-24b-instruct",
    "messages": [
        {"role": "user", "content":f"{story}"}
    ]
}

if st.button('Generate Response'):
    if story:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        with st.spinner("Loading Response"):
            if response.status_code==200:
                print("Status:", response.status_code)
                print("Response:")
                print(response.json()["choices"][0]["message"]["content"])
                st.write(response.json()["choices"][0]["message"]["content"])

