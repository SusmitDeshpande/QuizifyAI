import streamlit as st 
from chains import gen_quiz_chain

if not st.session_state.get("force_home", False):
    st.switch_page("app.py")

st.title("Quiz")

# quiz generation
if st.session_state.retriever:
    q_topic = st.text_input("Enter the subtopic to generate quiz : ")
    if st.button("Generate Quiz"):
        quiz_chain = gen_quiz_chain(st.session_state.retriever)
        quiz = quiz_chain.invoke(q_topic)
        st.write(quiz)
else:
    st.write("Please provide the topic and prepare documents on 'app' page.")