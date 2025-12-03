import streamlit as st 
from chains import summarize_chain


st.title("Summary")

final_summary = summarize_chain.run(st.session_state.all_docs)
    
st.write(final_summary)