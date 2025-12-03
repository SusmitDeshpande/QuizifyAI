import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

api_key = None

if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
elif os.getenv("GOOGLE_API_KEY"):
    api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found in st.secrets or .env/env variables.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

from chains import gen_quiz_chain, gen_rag_chain, summarize_chain
from docs import get_wiki_docs, get_user_doc
from vectordb import generate_db


st.title("QUIZIFY AI")

topic = st.text_input("Enter your topic : ")

user_info = st.radio(
    "Do you want to provide any information?",
    options=['no', 'yes'],
    )

wiki_info = st.radio(
    "Search wikipedia for information?",
    options=['no', 'yes'],
)

user_info = st.text_input("Please enter your information here : ", disabled = user_info=='no')

infoStat = False
if wiki_info=='no' and user_info=='no':
    infoStat = True

st.session_state.all_docs = []

if st.button("Prep", disabled=infoStat):
    
    if user_info=='yes':
        st.session_state.all_docs = [get_user_doc(user_info)]
        
    if wiki_info=='yes':
        if st.session_state.all_docs != None:
            st.session_state.all_docs += get_wiki_docs(topic, 2)
        else:
            st.session_state.all_docs = get_wiki_docs(topic, 2)

    st.session_state.retriever = generate_db(st.session_state.all_docs)
    
    final_summary = summarize_chain.run(st.session_state.all_docs)
    
    st.write(final_summary)
    

# RAG QA

question = st.text_input("Enter your questions here : ")

if st.button("Answer"):

    rag_chain = gen_rag_chain(st.session_state.retriever)
    result = rag_chain.invoke(question)
    st.write(result)

# quiz generation

q_topic = st.text_input("Enter the subtopic to generate quiz : ")

if st.button("Generate Quiz"):

    quiz_chain = gen_quiz_chain(st.session_state.retriever)
    quiz = quiz_chain.invoke(q_topic)
    st.write(quiz)

