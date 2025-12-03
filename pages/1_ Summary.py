import streamlit as st 
from chains import summarize_chain

if not st.session_state.get("force_home", False):
    st.switch_page("app.py")

st.title("Summary")

if st.session_state.all_docs:
    final_summary = summarize_chain.run(st.session_state.all_docs)
    st.write(final_summary)
else:
    st.write("Please provide the topic and prepare documents on 'app' page.")