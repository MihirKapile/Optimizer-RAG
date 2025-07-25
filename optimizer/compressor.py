import os
from dotenv import load_dotenv
from groq import Groq
from .token_utils import num_tokens_from_string
from .selector import select_chunks_within_budget

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_chunk_with_groq(chunk: str, query: str, model="llama-3.1-8b-instant") -> str:
    prompt = (
        f"Summarize the following document chunk focusing on answering this query:\n"
        f"Query: {query}\n"
        f"Chunk: {chunk}\n\n"
        f"Provide a concise but informative summary:"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=256,
    )

    return response.choices[0].message.content.strip()

def compress_chunk(chunks: list[str], query: str, token_budget: int):
    summarized_chunks = []
    for chunk in chunks:
        summary = summarize_chunk_with_groq(chunk, query)
        summarized_chunks.append(summary)

    chunk_token_pairs = [(chunk, num_tokens_from_string(chunk)) for chunk in summarized_chunks]

    chunk_token_pairs.sort(key=lambda x: x[1])

    selected_summaries = []
    total_tokens = 0
    for summary, tokens in chunk_token_pairs:
        if total_tokens + tokens <= token_budget:
            selected_summaries.append(summary)
            total_tokens += tokens
        else:
            break

    return selected_summaries