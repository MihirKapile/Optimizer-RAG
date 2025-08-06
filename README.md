<<<<<<< HEAD
# Optimizer

Optimizer is a Python library for compressing large documents using LLMs like Groq. It provides functionality for summarizing document chunks based on a query, selecting the most relevant summaries, and managing token budgets effectively — ideal for RAG (Retrieval Augmented Generation) applications.

## Features

- Summarize document chunks using Groq models
- Select relevant summaries based on token limits
- Easily integrate with any RAG pipeline

## Installation

```bash
pip install optimizer-groq
```

## Requirements

Make sure the following packages are installed (handled automatically if installing via pip):

```text
langchain>=0.1.16
groq
tiktoken
numpy
scikit-learn
sentence-transformers
python-dotenv
```

## Usage

```python
from optimizer.compressor import compress_chunk

chunks = ["Paragraph 1...", "Paragraph 2...", "Paragraph 3..."]
query = "What are the benefits of renewable energy?"
token_budget = 512

selected = compress_chunk(chunks, query, token_budget)
print(selected)
```

You can also customize the model by injecting the model into the library functions like this.

```python
from openai import OpenAI
from optimizer.compressor import compress_chunk

client = OpenAI(api_key="your-openai-api-key")

chunks = ["Text A...", "Text B..."]
query = "Summarize risks."
token_budget = 400

summaries = compress_chunk(chunks, query, token_budget, client=client, model="gpt-4")
```


## Environment Setup

Set your Groq API key in a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```
=======
# Optimizer-RAG

A lightweight Python library to compress large documents using Groq LLMs and token-budgeted chunk selection. Ideal for RAG (Retrieval-Augmented Generation) workflows and agentic systems that need concise, informative summaries within context limits.

## Features

- 🔍 Query-focused summarization of document chunks  
- 📉 Token-based chunk selection for context fitting  
- 🧠 Integration with Groq’s LLMs (LLaMA-3.1)  
- ⚙️ Plug-and-play support for RAG pipelines, LangChain tools, or custom agents

---

## Installation

```bash
git clone https://github.com/your-username/optimizer.git
cd optimizer
pip install -e .
```

Make sure you have a `.env` file with your Groq API key:

```env
GROQ_API_KEY=your-groq-key
```

---

## Usage

### 1. Import the library

```python
from optimizer.compressor import compress_chunk, summarize_chunk_with_groq
```

### 2. Summarize a single chunk

```python
summary = summarize_chunk_with_groq(
    chunk="Large input text here...",
    query="What are the key responsibilities?",
    model="llama-3.1-8b-instant"
)
```

### 3. Compress and select relevant chunks within a token budget

```python
chunks = ["First chunk of text", "Second chunk of text", ...]
query = "Summarize benefits of using this product"
token_budget = 1024

compressed = compress_chunk(chunks, query, token_budget)

for i, chunk in enumerate(compressed):
    print(f"Chunk {i+1}: {chunk}")
```

---

## Project Structure

```
optimizer/
├── __init__.py
├── compressor.py          # Main logic for summarizing and compressing
├── token_utils.py         # Token counting utility
├── selector.py            # Budget-aware chunk selector
```

---

## Use Cases

- ✂️ **RAG Context Compression**: Reduce token size of retrieved docs  
- 🤖 **Agent Memory Management**: Keep only informative memory within limits  
- 📄 **Long Document Summarization**: Turn bulky PDFs into summaries  

---

## Requirements

- Python 3.8+
- `groq`
- `tiktoken`
- `python-dotenv`

Install via:

```bash
pip install -r requirements.txt
```

---

>>>>>>> 0849fa821b23bb23a8726701ddf77b598053902e
