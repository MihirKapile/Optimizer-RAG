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

