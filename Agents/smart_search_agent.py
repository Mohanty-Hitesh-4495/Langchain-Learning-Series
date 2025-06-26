from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ["TAVILY_API_KEY"] = os.getenv('TAVILY_API_KEY')

model = ChatGroq(model="qwen-qwq-32b")
search = TavilySearch(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools)


st.title(" Smart Search Agent with LangChain and Tavily Search API ")
query = st.text_input("Tavily search:")

response = agent_executor.invoke(
    {
        "messages": [HumanMessage(content=query)]
    }
)
st.markdown(response['messages'][-1].content)