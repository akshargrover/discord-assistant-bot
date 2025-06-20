# rag/vectorstore.py

from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import TextLoader
import os

def get_vectorstore(directory_path: str):
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # or the latest model, see docs
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
    loader = TextLoader(directory_path)
    documents = loader.load()
    return FAISS.from_documents(documents, embeddings)
