from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
# Langsmith tracking
os.environ['LANGACHAIN_TRACING_V2'] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework
st.title('🤖 Langchian Demo with Open-AI')
input_text = st.text_input("Ask me anything 💬")

# OpenAI LLM
llm = ChatOpenAI(model = "gpt-4o-mini")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.markdown(chain.invoke({'question':input_text}))

# About Section
with st.expander("ℹ️ About this Chatbot 🤖"):
    st.markdown("""
        This chatbot is built using **LangChain** and **OpenAI API**.
        
        - **LangChain:** A framework for building LLM-powered applications.
        - **OpenAI API:** Used to generate intelligent responses.
        - **Streamlit:** Provides a simple and interactive UI.
        
        🛠 **Implementation:**
        1. Uses **ChatPromptTemplate** to format user queries.
        2. Uses **OpenAI's GPT-4o-mini** model for responses.
        3. Displays responses in a clean and interactive UI.
        
        💡 **Use cases:** General Q&A, research assistance, and interactive AI conversations.
    """)