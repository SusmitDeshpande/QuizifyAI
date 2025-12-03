import streamlit as st

st.session_state.force_home = True

from src.load_api import load_api
load_api()

from src.docs import get_wiki_docs, get_user_doc
from src.vectordb import generate_db

st.set_page_config(page_title="Quizify AI", layout="wide")

st.title("Welcome to Quizify AI")

st.html('''
        <p>Quizify AI is an intelligent learning assistant designed to help you understand any topic quickly and interactively. Simply enter a subject, and the app automatically retrieves the top relevant information from Wikipedia, builds a custom RAG (Retrieval-Augmented Generation) knowledge base, and combines it with any additional text you provide.
        With this curated context, Quizify AI:</p>
        <ul>
        <li>Generates a clear, concise summary of the topic</li>
        <li>Answers your questions accurately using verified reference material</li>
        <li>Creates a personalized MCQ quiz to help you test your understanding</li>
        </ul>
        <p>
        Whether you're studying, revising, or exploring new topics, Quizify AI turns complex information into an easy and engaging learning experience.
        </p>
        ''')

topic = st.text_input("Enter your topic : ")

user_flag = st.radio(
    "Do you want to provide any information?",
    options=['no', 'yes'],
    )

wiki_flag = st.radio(
    "Search wikipedia for information?",
    options=['no', 'yes'],
)

user_info = st.text_input("Please enter your information here : ", disabled = user_flag=='no')

st.session_state.all_docs = []
st.session_state.retriever = None

if st.button("Prep", disabled=not (wiki_flag=='yes' or user_flag=='yes')):
    
    if user_flag=='yes':
        st.session_state.all_docs = [get_user_doc(user_info)]
        
    if wiki_flag=='yes':
        if st.session_state.all_docs != None:
            st.session_state.all_docs += get_wiki_docs(topic, 2)
        else:
            st.session_state.all_docs = get_wiki_docs(topic, 2)

    st.session_state.retriever = generate_db(st.session_state.all_docs)

