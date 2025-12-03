import streamlit as st 
from chains import gen_rag_chain


st.title("Question-Answers")

# RAG QA

question = st.text_input("Enter your questions here : ")

if st.button("Answer"):

    rag_chain = gen_rag_chain(st.session_state.retriever)
    result = rag_chain.invoke(question)
    st.write(result)