import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import os
from optimizer.compressor import compress_chunk
from dotenv import load_dotenv

load_dotenv()

SAMPLE_CHUNKS = [
    "The mitochondria is the powerhouse of the cell. It converts glucose into ATP through cellular respiration.",
    "In 1492, Columbus sailed the ocean blue and discovered the New World, altering the course of history.",
    "Machine learning is a subset of AI that enables systems to learn patterns from data without being explicitly programmed.",
    "Water boils at 100 degrees Celsius and freezes at 0 degrees Celsius under normal atmospheric pressure.",
    "Python is a popular programming language known for its readability and large ecosystem."
]

QUERY = "How does machine learning work?"

TOKEN_BUDGET = 512

def test_compress_chunk():
    summaries = compress_chunk(
        chunks=SAMPLE_CHUNKS,
        query=QUERY,
        token_budget=TOKEN_BUDGET
    )
    print("\n--- Summaries ---")
    for i, summary in enumerate(summaries):
        print(f"\nSummary {i+1}:\n{summary}\n")


if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        print("❌ GROQ_API_KEY not found in environment.")
    else:
        test_compress_chunk()
