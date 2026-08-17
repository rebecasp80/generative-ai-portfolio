import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Variables globales
llm = None
embeddings = None
rag_chain = None


def init_llm():
    global llm, embeddings

    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("La variable GROQ_API_KEY no está configurada.")

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.0,
        max_tokens=256,
        groq_api_key=groq_api_key
    )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def process_document(document_path):
    global rag_chain

    loader = PyPDFLoader(document_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=64
    )
    chunks = splitter.split_documents(docs)

    db = FAISS.from_documents(chunks, embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 6})

    prompt = ChatPromptTemplate.from_template(
        """
        Responde de forma breve y directa usando solo la información del documento.

        Pregunta:
        {question}

        Contexto:
        {context}
        """
    )

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )


def process_prompt(prompt):
    global rag_chain

    if rag_chain is None:
        return "Primero carga un PDF."

    response = rag_chain.invoke(prompt)
    return response.content.strip()


init_llm()
