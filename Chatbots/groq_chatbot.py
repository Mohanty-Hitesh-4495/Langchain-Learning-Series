from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_v2'] = 'true'

prompts = ChatPromptTemplate.from_messages([
    ("system", "you are an intelligent chatbot, help the user with answering there query in crisp and concise."),
    ("user", "{question}")
])

output_parser = StrOutputParser()
llm = ChatGroq(model = 'llama-3.3-70b-versatile')
chain = prompts | llm | output_parser

if __name__ == "__main__":
    st.title("🤖 AI-Assistant for general Q&A")
    input = st.text_input("Ask me anything 💬") 
    if input:
        st.markdown(chain.invoke({'question':input}))
