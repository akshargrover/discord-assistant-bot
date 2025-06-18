from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents_from_folder(folder_path: str):
    """Load .txt, .pdf, and .docx files from the specified folder."""
    docs = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        ext = os.path.splitext(filename)[-1].lower()

        try:
            if ext == ".txt":
                loader = TextLoader(file_path)
            elif ext == ".pdf":
                loader = PyPDFLoader(file_path)
            elif ext in [".doc", ".docx"]:
                loader = UnstructuredWordDocumentLoader(file_path)
            else:
                print(f"⚠️ Unsupported file type: {filename}")
                continue

            docs.extend(loader.load())
        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")

    return docs

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Split documents into chunks suitable for embedding."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)
