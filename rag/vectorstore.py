# rag/vectorstore.py

from langchain.vectorstores import FAISS
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import TextLoader
import os

def get_vectorstore(directory_path: str):
    embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv("GOOGLE_API_KEY"))
    loader = TextLoader(directory_path)
    documents = loader.load()
    return FAISS.from_documents(documents, embeddings)
