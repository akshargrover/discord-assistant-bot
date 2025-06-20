import os
from rag.qa_chain import get_qa_chain

def main():
    print("🎮 Assistant CLI Mode — Ask Anything from FAISS Docs + Gemini")
    print("Type 'exit' to quit.")
    
    qa_chain = get_qa_chain()

    while True:
        query = input("\\nYou: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        try:
            response = qa_chain.run(query)
            print(f"Assistant: {response.strip()[:2000]}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()