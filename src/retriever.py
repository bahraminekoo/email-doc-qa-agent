from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import MODEL_NAME, HF_TOKEN

def build_retriever(docs):
    embeddings = HuggingFaceEmbeddings(
        model_name=MODEL_NAME,
        cache_folder="./models",
        model_kwargs={"token": HF_TOKEN}
    )
    vectordb = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")
    return vectordb.as_retriever()