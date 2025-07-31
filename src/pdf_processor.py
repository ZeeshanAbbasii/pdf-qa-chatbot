import os
import fitz  # PyMuPDF
import re
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from src.config import CHUNKS_DIR, PDF_DIR

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

def chunk_and_store_text(text, source_name, chunk_size=1000, chunk_overlap=200):
    if not text.strip():
        print(f"Warning: Empty text received for {source_name}")
        return []

    safe_source_name = re.sub(r'\W+', '_', source_name)
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = splitter.split_text(text)

    documents = [
        Document(
            page_content=chunk,
            metadata={"source": safe_source_name}
        )
        for chunk in chunks
    ]

    os.makedirs(CHUNKS_DIR, exist_ok=True)

    return documents

def process_all_pdfs():
    all_chunks = []
    for file in os.listdir(PDF_DIR):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, file)
            print(f"📄 Processing: {file}")
            text = extract_text_from_pdf(pdf_path)
            if not text.strip():
                print(f"⚠️ Skipped (empty text): {file}")
                continue
            chunks = chunk_and_store_text(text, source_name=file.rsplit('.', 1)[0])
            all_chunks.extend(chunks)
    return all_chunks