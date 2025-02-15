from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate

from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

server = FastAPI(
    title = "Langchain Server",
    version = "1.0",  
    description = "A simple API Server"
)

model1 = ChatOpenAI(model="gpt-4o-mini")
model2 = ChatAnthropic(model_name="claude-3.5-sonnet-20241022")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    server,
    prompt1|model1,
    path = "/essay"
)

add_routes(
    server,
    prompt2|model1,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run(server,host="localhost",port=8000)