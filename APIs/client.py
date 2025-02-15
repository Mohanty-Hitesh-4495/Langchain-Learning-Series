import requests
import streamlit as st

def get_essay(topic):
    response = requests.post(
        "http://localhost:8000/essay/invoke", 
        json={'input':{'topic':topic}}
    )
    return response.json()['output']['content']

def get_poem(topic):
    response = requests.post(
        "http://localhost:8000/poem/invoke", 
        json={'input':{'topic':topic}}
    )
    return response.json()['output']['content']

st.title("Lanngchain Demo with OpenAI")
input_text1 = st.text_input("Enter a topic for an essay:")
input_text2 = st.text_input("Enter a topic for an poem:")

if input_text1:
    st.subheader("Generated Essay")
    st.write(get_essay(input_text1))
    
if input_text2:
    st.subheader("Generated Poem")
    st.write(get_poem(input_text2))