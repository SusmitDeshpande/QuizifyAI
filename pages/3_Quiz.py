import streamlit as st 
from chains import gen_quiz_chain

st.title("Quiz")

# quiz generation

q_topic = st.text_input("Enter the subtopic to generate quiz : ")

if st.button("Generate Quiz"):

    quiz_chain = gen_quiz_chain(st.session_state.retriever)
    quiz = quiz_chain.invoke(q_topic)
    st.write(quiz)