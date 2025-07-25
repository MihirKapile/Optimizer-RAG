import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

from optimizer.retriever_wrapper import ContextBudgetRetriever

def setup_faiss_retriever():
    loader = TextLoader("E:\\context-budget-optimizer\\OFL.txt")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    faiss_retriever = FAISS.from_documents(docs, hf_embeddings)

    return faiss_retriever.as_retriever()

def main():
    retriever = setup_faiss_retriever()

    budget_retriever = ContextBudgetRetriever(retriever, token_budget=1000)

    query = "Explain the main points of the documents."

    docs = budget_retriever.get_relevant_documents(query)

    print(f"Retrieved {len(docs)} compressed chunks:")
    for i, doc in enumerate(docs):
        print(f"Chunk {i+1}:\n{doc.page_content}\n")

if __name__ == "__main__":
    main()