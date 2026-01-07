from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpoint
from src.config import HF_TOKEN

def build_qa_chain(retriever):
    llm = HuggingFaceEndpoint(
        repo_id="google/flan-t5-base",  # lightweight model
        huggingfacehub_api_token=HF_TOKEN
    )
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    return qa
