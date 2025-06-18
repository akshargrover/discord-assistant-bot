from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from .vectorstore import get_vectorstore
import os

def get_qa_chain():
    retriever = get_vectorstore().as_retriever()
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
