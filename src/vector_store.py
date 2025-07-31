import os
import json
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from src.config import CHUNKS_DIR, VECTORSTORE_DIR

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_vectorstore(chunks):
    docs = [Document(page_content=chunk["text"], metadata=chunk["metadata"]) for chunk in chunks]

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory=VECTORSTORE_DIR
    )
    vectorstore.persist()
    return vectorstore

def load_vectorstore():
    if os.path.exists(VECTORSTORE_DIR):
        return Chroma(
            embedding_function=embedding_model,
            persist_directory=VECTORSTORE_DIR
        )
    return None

def create_or_load_vectorstore(chunks):
    if os.path.exists(VECTORSTORE_DIR) and os.listdir(VECTORSTORE_DIR):
        return load_vectorstore()
    return get_vectorstore(chunks)