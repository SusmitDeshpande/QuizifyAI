import streamlit as st
from langchain_community.retrievers import WikipediaRetriever 

retriever = WikipediaRetriever(load_max_docs=5)

st.title("QUIZIFY AI")
topic = st.text_input("Enter your topic : ")

choice = st.radio(
    "Do you want to provide any information?",
    options=['no', 'yes'],
    )

if choice=='yes':
    user_info = st.text_input("Please enter your information here : ")



if st.button("Submit"):
    docs = retriever.invoke(topic)
    st.write(docs[0].page_content[:400])