## Different components of Langchain

LangChain is a framework designed to build advanced AI applications that integrate large language models (LLMs) with various functionalities. 

![Components of Langchain](/Images/langchain_components.jpg  "Components of Langchain")

Here’s a breakdown of its key components:

**1.  Models**: LangChain relies heavily on models, with two main types:

-   **LLMs**: Accept string inputs and generate string outputs. These are the fundamental models used for tasks like NLP and SQL generation.
-   **ChatModels**: Tailored for conversation, these are designed for interactive tasks where maintaining context across exchanges is key.

**2. Prompts**: LangChain simplifies working with LLMs through prompt templates, which reduce the effort of writing prompts.

-   **Prompt Templates**: These templates are designed for LLM models, enabling easier input customization.
-   **ChatPrompt Templates**: Similar to Prompt Templates, but optimized for use with ChatModels, supporting conversational flows.

**3. Chains**: These are scripts that combine LLMs with external functions to perform more complex tasks, like Named Entity Recognition (NER), automatic SQL generation, or performing calculations using LLMs.

**4. Agents**: Agents take chains to the next level by integrating various tools and dynamic decision-making. They can choose actions based on inputs and work on more customizable tasks.

**5. Output Parsers**: These ensure that the output from LLMs comes in a desired format, such as lists or bullet points, which is useful when accuracy and consistency are needed in results.

**6. Memory**: Memory allows the LLM to remember past interactions, making it possible to maintain continuity across conversations, much like how ChatGPT works.

**7. Schema**:
These define data structures that flow between all other LangChain components.
- Text: Plain text inputs or outputs (for LLMs or chains).
- ChatMessages: Role-based messages (SystemMessage, HumanMessage, etc.) for ChatModels.
- Examples: Predefined input-output examples for few-shot prompting.
- Document: Structured representation of external data (like PDF, HTML, etc.) used in RAG and retrieval.

**8. Indexes (RAG / Search Related)**:
For loading, splitting, embedding, and storing documents.
- Document Loaders: Read data from external files like PDF, CSV, Websites, etc.
- Text Splitters: Break large documents into smaller manageable chunks.
- Retriever: Fetches relevant chunks from vector store using semantic similarity.
- Vectorstore: Stores and retrieves dense vector embeddings (Chroma, Pinecone, etc.)
