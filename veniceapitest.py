import streamlit as st
import requests
import json

# Get API key from Streamlit secrets
api_key = st.secrets["api_key"]

st.write("API Key Present:", bool(api_key))
st.write("API Key Preview:", api_key[:6] + "...")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-app.streamlit.app",
    "X-Title": "StreamlitApp"
}

story = st.text_input("Enter prompt")
if st.button("Generate Response") and story:
    payload = {
        "model": "mistralai/mistral-small-3.2-24b-instruct",
        "messages": [{"role": "user", "content": story}]
    }

    with st.spinner("Contacting OpenRouter..."):
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.success("Done!")
        st.write(reply)
    else:
        st.error(f"Status Code: {response.status_code}")
        st.code(response.text, language="json")
