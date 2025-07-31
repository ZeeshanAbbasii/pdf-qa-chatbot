import os
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from src.config import PDF_DIR, CHUNKS_DIR

def load_and_chunk_pdfs():
    os.makedirs(CHUNKS_DIR, exist_ok=True)

    all_chunks = []
    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, filename)
            loader = PyPDFLoader(pdf_path)
            pages = loader.load()

            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_documents(pages)

            chunk_data = [{"text": c.page_content, "metadata": c.metadata} for c in chunks]
            all_chunks.extend(chunk_data)

            # Save chunks for reference
            with open(os.path.join(CHUNKS_DIR, f"{filename}.json"), "w") as f:
                json.dump(chunk_data, f, indent=2)

    return all_chunks