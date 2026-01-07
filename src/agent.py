from src.loaders import load_documents
from src.retriever import build_retriever
from src.qa_chain import build_qa_chain

def run_agent(file_path, query):
    docs = load_documents(file_path)
    retriever = build_retriever(docs)
    qa_chain = build_qa_chain(retriever)
    return qa_chain.run(query)

if __name__ == "__main__":
    answer = run_agent("sample.pdf", "Summarize this document in 3 bullet points")
    print(answer)
