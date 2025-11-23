import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_community.retrievers import WikipediaRetriever 
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY") 

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

retriever = WikipediaRetriever(load_max_docs=5)

template = """Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:"""

prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

st.title("QUIZIFY AI")
topic = st.text_input("Enter your topic : ")

choice = st.radio(
    "Do you want to provide any information?",
    options=['no', 'yes'],
    )

if choice=='yes':
    user_info = st.text_input("Please enter your information here : ")
    user_doc = Document(page_content=user_info, metadata={"source":"user provided info"})



if st.button("Prep"):
    wiki_docs = retriever.invoke(topic)
    
    if choice=='yes':
        all_docs = wiki_docs + [user_doc]
    else:
        all_docs = wiki_docs
    
    split_docs = text_splitter.split_documents(all_docs)
    
    db = FAISS.from_documents(split_docs, embeddings)

    # docs_with_scores = db.similarity_search_with_score(question)

    retriever = db.as_retriever()

rag_chain = (
{"context": retriever | format_docs, "question": RunnablePassthrough()}
| prompt
| model
| StrOutputParser() # Parses the LLM output into a string
)
    

question = st.text_input("Enter your questions here : ")

if st.button("Answer"):

    result = rag_chain.invoke(question)
    st.write(result)
