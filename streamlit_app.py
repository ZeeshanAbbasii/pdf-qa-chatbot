import streamlit as st
from src.loader import load_and_chunk_pdfs
from src.vector_store import create_or_load_vectorstore
from src.qa_engine import ask_question

st.title("🧠 Your Personal AI Tutor)")

query = st.text_input("Ask any question about coding:")

if st.button("Process PDFs"):
    with st.spinner("Loading and chunking PDFs..."):
        chunks = load_and_chunk_pdfs()
        st.success(f"Loaded and chunked {len(chunks)} text segments!")

    with st.spinner("Building vectorstore..."):
        vectorstore = create_or_load_vectorstore(chunks)
        st.success("Vectorstore created and ready!")

if query:
    with st.spinner("Thinking..."):
        chunks = load_and_chunk_pdfs()
        vectorstore = create_or_load_vectorstore(chunks)
        answer = ask_question(vectorstore, query)
        st.write("### Answer:")
        st.write(answer)