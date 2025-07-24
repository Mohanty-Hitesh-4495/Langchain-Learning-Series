from fastapi import FastAPI, HTTPException
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define request models
class TopicRequest(BaseModel):
    topic: str

class TopicResponse(BaseModel):
    content: str

server = FastAPI(
    title="Langchain Server",
    version="1.0",  
    description="A simple API Server for testing"
)

model1 = ChatGroq(model="llama-3.3-70b-versatile")
model2 = ChatGroq(model="gemma2-9b-it")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 500 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 years child with 100 words")

# Create chains
essay_chain = prompt1 | model1
poem_chain = prompt2 | model2

@server.post("/essay", response_model=TopicResponse)
async def generate_essay(request: TopicRequest):
    try:
        result = await essay_chain.ainvoke({"topic": request.topic})
        return TopicResponse(content=result.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@server.post("/poem", response_model=TopicResponse)
async def generate_poem(request: TopicRequest):
    try:
        result = await poem_chain.ainvoke({"topic": request.topic})
        return TopicResponse(content=result.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@server.get("/")
async def root():
    return {"message": "Langchain Server is running!"}

if __name__ == "__main__":
    uvicorn.run(server, host="localhost", port=8000)