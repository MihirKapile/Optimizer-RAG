import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import AutoTokenizer
import numpy as np

# Initialize HuggingFace tokenizer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Large documents
documents = [
    """LangChain is a powerful framework designed to simplify the development of applications that leverage large language models (LLMs). By offering composable abstractions and integrations for retrieval, agents, memory, and chains, LangChain allows developers to build robust applications rapidly. It supports popular LLM providers and enables the use of tools and external knowledge sources such as vector databases and APIs. LangChain also encourages best practices for working with prompts, including prompt templates, few-shot examples, and output parsers.""",

    """Token limits in LLMs can significantly hinder the performance of applications that require long context windows. For example, retrieving relevant passages from lengthy documents such as research papers or contracts can be challenging when token budgets are tight. Developers often use chunking and retrieval-based augmentation (RAG) to fit content within model limits. However, selecting which chunks to include requires careful scoring and sometimes compression to maximize the quality of context within the constraints of the model's input size.""",

    """Groq's custom-built LPU hardware and software stack has been engineered for ultra-low latency and high throughput. This makes Groq LLMs especially well-suited for use cases that require real-time responses, such as summarization, legal review, and live chat. Groq’s architecture avoids GPU memory bottlenecks and instead focuses on deterministic execution, enabling consistent inference times. This innovation opens up possibilities for interactive, high-speed AI applications that were previously infeasible with conventional LLM hosting solutions."""
]

query = "How to select and compress context chunks for RAG pipelines?"

def get_tfidf_scores(query: str, documents: List[str]) -> List[Tuple[str, float]]:
    """Score documents using TF-IDF relevance to the query."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents + [query])
    scores = (tfidf_matrix[:-1] @ tfidf_matrix[-1].T).toarray().flatten()
    return list(zip(documents, scores))

def compress_chunk(chunk: str, budget: int = 50) -> str:
    """Compress a chunk by selecting highest-value sentences within token budget."""
    sentences = chunk.split(". ")
    scored_sentences = [(s.strip(), len(tokenizer.encode(s.strip(), add_special_tokens=False))) for s in sentences]
    scored_sentences.sort(key=lambda x: x[1])  # Prefer shorter sentences first

    compressed = []
    total_tokens = 0
    for sentence, tokens in scored_sentences:
        if total_tokens + tokens <= budget:
            compressed.append(sentence)
            total_tokens += tokens
        else:
            break
    return ". ".join(compressed)

# Score and compress
scored_docs = get_tfidf_scores(query, documents)
sorted_docs = sorted(scored_docs, key=lambda x: x[1], reverse=True)
top_docs = [doc for doc, _ in sorted_docs]

# Run compression
for i, doc in enumerate(top_docs):
    original_tokens = len(tokenizer.encode(doc, add_special_tokens=False))
    compressed = compress_chunk(doc, budget=50)
    compressed_tokens = len(tokenizer.encode(compressed, add_special_tokens=False))

    print(f"\n--- Document #{i+1} ---")
    print(f"Original Token Count: {original_tokens}")
    print(f"Compressed Token Count: {compressed_tokens}")
    print("Compressed Text:\n", compressed)
    print("✅ Budget Respected" if compressed_tokens <= 50 else "❌ Budget Exceeded")