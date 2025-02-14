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
st.title('Langchian Demo with Open-AI API')
input_text = st.text_input("Search the topic that you want")

# OpenAI LLM
llm = ChatOpenAI(model = "gpt-4o-mini")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.markdown(chain.invoke({'question':input_text}))