import streamlit as st 
from src.chains import gen_rag_chain

if not st.session_state.get("force_home", False):
    st.switch_page("app.py")

st.title("Question-Answers")

# RAG QA
if st.session_state.retriever:
    question = st.text_input("Enter your questions here : ")
    if st.button("Answer"):
        rag_chain = gen_rag_chain(st.session_state.retriever)
        result = rag_chain.invoke(question)
        st.write(result)
else:
    st.write("Please provide the topic and prepare documents on 'app' page.")