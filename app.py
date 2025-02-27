import requests
import streamlit as st
import json  

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #f8f9fa, #e3e7eb);
            color: black;
        }
        .stTextInput > div > div > input {
            background-color: #f1f3f4;
            color: black;
            border-radius: 24px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #dfe1e5;
        }
        .suggestions {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 10px;
        }
        .suggestion-button {
            background-color: #f1f3f4;
            color: black;
            border-radius: 20px;
            padding: 8px 14px;
            font-size: 14px;
            border: none;
            cursor: pointer;
            transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
        }
        .suggestion-button:hover {
            background-color: #e0e0e0;
            transform: scale(1.05);
        }
        .header {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            background: linear-gradient(to right, #ff8a00, #da1b60);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown("<h1 class='header'>TU LIKH BHAI</h1>", unsafe_allow_html=True)

# Use session state to store user input
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

user_input = st.text_input("Search...", st.session_state.user_input)

if user_input:
    response = requests.post(
        "http://localhost:5678/webhook/b548cdf2-d85c-4993-b90f-d0943e3344b2",
        json={"query": user_input}
    )

    response_list = json.loads(response.text)

    st.write("<div class='suggestions'>", unsafe_allow_html=True)
    
    cols = st.columns(len(response_list))
    for i, suggestion in enumerate(response_list):
        with cols[i]:
            if st.button(suggestion, key=f"{suggestion}_{i}"):  
                if suggestion.startswith(st.session_state.user_input):
                    st.session_state.user_input = suggestion
                else:
                    st.session_state.user_input += " " + suggestion  
                st.rerun()

    st.write("</div>", unsafe_allow_html=True)
