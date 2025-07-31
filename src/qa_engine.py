from langchain_community.chat_models import ChatOllama
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOllama(model="mistral")

def ask_question(vectorstore, query):
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(query)

    context = "\n".join([doc.page_content for doc in docs])

    messages = [
        SystemMessage(content="You are a helpful assistant. Answer the user's question based ONLY on the context provided."),
        HumanMessage(content=f"Context:\n{context}\n\nQuestion: {query}")
    ]

    response = llm(messages)
    return response.content