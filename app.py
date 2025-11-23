import streamlit as st
from langchain_community.retrievers import WikipediaRetriever 
from langchain_core.documents import Document

retriever = WikipediaRetriever(load_max_docs=5)

st.title("QUIZIFY AI")
topic = st.text_input("Enter your topic : ")

choice = st.radio(
    "Do you want to provide any information?",
    options=['no', 'yes'],
    )

if choice=='yes':
    user_info = st.text_input("Please enter your information here : ")
    user_doc = Document(page_content=user_info, metadata={"source":"user provided info"})

if st.button("Submit"):
    wiki_doc = retriever.invoke(topic)
    st.write(user_doc.page_content[:400])