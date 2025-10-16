# PDF Q&A Chatbot with Mistral & Sentence Transformers

This project is a ChatGPT-style assistant that answers questions based on the contents of uploaded PDF files. It uses the Mistral 7B model (via Hugging Face) for generating responses and Sentence Transformers for document embedding and efficient semantic search.

⸻

### Features
	•	Ask context-based questions about your uploaded PDFs.
	•	Semantic search powered by sentence-transformers.
	•	Contextual answers generated using the Mistral language model.
	•	Built with Streamlit for an intuitive user interface.
	•	Runs locally without requiring the OpenAI API.

⸻

### How to Run

#### 1. Clone the Repository
git clone https://github.com/yourusername/pdf-qa-chatbot.git
cd pdf-qa-chatbot

#### 2. Install Requirements
It is recommended to use a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

#### 3. Add Your PDFs
Place your PDF files in the designated project folder (e.g., /pdfs or /data).

#### 4. Run the Application
streamlit run streamlit_app.py

### Tech Stack
	•	LLM: Mistral 7B (via Hugging Face Transformers)
	•	Embeddings: Sentence Transformers (e.g., all-MiniLM-L6-v2)
	•	Frontend: Streamlit
	•	Backend: Python
	•	PDF Parsing: PyMuPDF

⸻

### Example Usage:
You can ask your chatbot questions such as:
“What is the main argument discussed in Chapter 2 of this PDF?”

⸻

### To-Do
	•	Add multi-file PDF support
	•	Improve text chunking and retrieval logic
	•	Add a feedback/rating system
	•	Dockerize the project for easier deployment

⸻

### License
This project is open-source and available under the MIT License.

⸻

Author
Developed by Zeeshan Abbasi
