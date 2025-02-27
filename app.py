import streamlit as st
import requests

st.title("AI Autocomplete")

# User input box with session state
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

user_input = st.text_input("Start typing...", st.session_state["user_input"], key="input")

# Send request on every keystroke
if user_input:
    response = requests.post("http://localhost:5678/webhook-test/77ddaac1-4233-41c2-80b7-df9de4ffa3a8", json={"query": user_input})
    if response.status_code == 200:
        suggestions = response.json().get("suggestions", "").split("\n")  # Convert to list
    else:
        suggestions = []

    # Display suggestions in a dropdown
    selected_suggestion = st.selectbox("Suggestions:", suggestions) if suggestions else st.write("No suggestions yet.")
