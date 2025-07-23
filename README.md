<div align="center">
  <h1> 🦜🔗 LangChain & LangGraph Learnings Repository </h1>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/langgraph-008B8B?style=for-the-badge&logo=langgraph&logoColor=white" />
  <img src="https://img.shields.io/badge/-HuggingFace-FDEE21?style=for-the-badge&logo=HuggingFace&logoColor=black" />
  <img src="https://img.shields.io/badge/Groq-412991?style=for-the-badge&logo=groq&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-F0F8FF?style=for-the-badge&logo=openai&logoColor=black" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white" />
</div>
  
This repository contains hands-on implementations, guided notebooks, and architecture experiments from my journey learning and applying [LangChain](https://www.langchain.com/) and [LangGraph](https://www.langchain.com/langgraph/) for building modern LLM-powered applications.

---

## Repository Structure

| Folder | Description |
|--------|-------------|
| `01_LLM_Application/` | Simple LLM application examples (text generation, completions, etc.). |
| `02_Chatbots/` | Chatbot implementations using **Groq**, **Ollama**, and **OpenAI** models. |
| `03_Agents/` | Smart agents including autonomous search agents using LangGraph + Tavily. |
| `04_RAG_pipeline/` | Complete Retrieval-Augmented Generation pipelines: web/PDF loaders, chunking, embeddings (Chroma, FAISS), and query systems. |
| `05_APIs/` | FastAPI servers and Streamlit clients for LLM-based essay & poem generation. |
| `06_Chains_&_Retrievers/` | Advanced chain and retriever demos (QA bots, memory chains, etc.). |
| `Docs/` | Markdown notes explaining LangChain, LangGraph, and core components. |
| `Images/` | Diagrams and illustrations for internal pipelines and architecture references. |

---

## Highlights

- End-to-end **RAG pipeline** using HuggingFace embeddings and Chroma/FAISS.
- Chatbots with Streamlit frontends and support for multiple LLM providers.
- Smart agents powered by LangGraph and Tavily Search API.
- FastAPI-based API server and client apps for creative content generation.
- Step-by-step Jupyter notebooks covering ingestion → chunking → retrieval.

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mohanty-Hitesh-4495/Langchain-Learning-Series.git
   cd LangChain-Learnings-Series
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   Create a `.env` file and add necessary keys:

   ```env
   OPENAI_API_KEY=your_openai_key
   GROQ_API_KEY=your_groq_key
   ANTHROPIC_API_KEY=your_anthropic_key
   TAVILY_API_KEY=your_tavily_key
   ```

4. **Run notebooks or apps:**

   ```bash
   streamlit run 02_Chatbots/your_chatbot_app.py
   ```

---

## Concepts Covered

* LLMs with LangChain: PromptTemplates, LLMChain, ChatModels
* LangGraph agents & multi-step workflows
* Retrieval with Chroma, FAISS, and custom retrievers
* Tools: Tavily Web Search, DuckDuckGo, SerpAPI
* Frontends: Streamlit and FastAPI
* Model integration: OpenAI, Groq, Ollama, HuggingFace

---

## 🛠 Requirements

* Python 3.8+
* `LangChain`, `LangGraph`, `Streamlit`, `FastAPI`, `Uvicorn`, and other dependencies listed in `requirements.txt`

---

## License

This repository is intended for **educational and research** purposes.
Feel free to modify, expand, or fork it as needed.

---

## Connect

For any feedback, questions, or contributions, feel free to open an issue or connect via GitHub!

