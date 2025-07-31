# 🧠 PDF Q&A Chatbot with Mistral & Sentence Transformers
This is your very own ChatGPT-style assistant that can answer questions based on the contents of PDF files. It uses the Mistral 7B model (via HuggingFace) for responses and `sentence-transformers` to embed the documents for efficient semantic search.
---
## 🔍 Features

- Ask questions about your uploaded PDFs.
- Semantic search using `sentence-transformers`.
- Contextual answers generated via the Mistral model.
- Built with Streamlit for a user-friendly UI.
- Locally runs without needing OpenAI API.

---
## 🚀 How to Run
### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-qa-chatbot.git
cd pdf-qa-chatbot
```
2. Install Requirements

We recommend using a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Add Your PDFs
Put your PDF files into:

4. Run the App
streamlit run streamlit_app.py


🛠 Tech Stack
	•	LLM: Mistral 7B (via HuggingFace Transformers)
	•	Embedding: sentence-transformers (e.g., all-MiniLM-L6-v2)
	•	Frontend: Streamlit
	•	Backend: Python
	•	PDF Parsing: PyMuPDF

🙋‍♂️ Example Question

Ask your chatbot:
“What is the main argument discussed in Chapter 2 of this PDF?”

⸻
📌 To-Do
	•	Add multi-file PDF support
	•	Improve chunking logic
	•	Add feedback/rating system
	•	Dockerize for easier deployment

⸻
📄 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Built with 💻 by Zeeshan Abbasi
