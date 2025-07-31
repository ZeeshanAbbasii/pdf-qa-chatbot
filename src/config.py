import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PDF_DIR = os.path.join(BASE_DIR, "data", "raw_pdfs")
CHUNKS_DIR = os.path.join(BASE_DIR, "data", "chunks")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "data", "vectorstore")