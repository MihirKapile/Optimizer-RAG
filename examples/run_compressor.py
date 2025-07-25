import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from optimizer.compressor import compress_chunk

query = "What are the risks of the vendor contract?"
chunk = """The contract mentions liability up to $1M in case of breach. However, there is no mention of data privacy obligations under GDPR. Indemnity is restricted to direct damages only."""

summary = compress_chunk(chunk, query)
print("Compressed Output:\n", summary)