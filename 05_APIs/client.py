import requests
import streamlit as st

def get_essay(topic):
    response = requests.post(
        "http://localhost:8000/essay", 
        json={'topic':topic}
    )   
    return response.json()['content']

def get_poem(topic):
    response = requests.post(
        "http://localhost:8000/poem", 
        json={'topic':topic}
    )
    return response.json()['content']

st.title("Langchain Demo with GROQ's LLM")
input_text1 = st.text_input("Enter a topic for an essay:")
input_text2 = st.text_input("Enter a topic for an poem:")

if input_text1:
    st.subheader("Generated Essay")
    # get_essay(input_text1)
    st.write(get_essay(input_text1))
    
if input_text2:
    st.subheader("Generated Poem")
    # get_essay(input_text2)
    st.write(get_poem(input_text2))