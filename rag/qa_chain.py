from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from rag.vectorstore import get_vectorstore
import os

def get_qa_chain():
    """Returns a RetrievalQA chain using Gemini Flash and FAISS"""
    # Load your documents and create vectorstore
    vectorstore = get_vectorstore("data/faiss_docs")  

    # Use Gemini 2.0 Flash
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )

    # Create the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
        return_source_documents=True  # Set to True to show source chunks
    )

    return qa_chain
