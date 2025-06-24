# Building simple LLM application using chat models and prompt templetes

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

llm = ChatGroq(model = "llama-3.3-70b-versatile",)

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant."),
    ("user", "Answer this question: {question}"),
])

output_parser = StrOutputParser()

chain = prompt| llm | output_parser

if __name__ == "__main__":
    result = chain.invoke({"question": "give a brief about LangChain and its applications"})
    print(result)