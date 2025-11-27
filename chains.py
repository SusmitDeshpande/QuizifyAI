from langchain_core.prompts import ChatPromptTemplate
from templates import quiz_msg_template, qa_template
from langchain_core.runnables import RunnablePassthrough
from models import llm, model
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.chains.summarize import load_summarize_chain

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

# summarize chain

summarize_chain = load_summarize_chain(
    llm,
    chain_type="map_reduce",
    verbose=True # helpful for tracking the recursive steps
    )

# rag chain

prompt = ChatPromptTemplate.from_template(qa_template)

def gen_rag_chain(retriever):

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser() # Parses the LLM output into a string
        )
    
    return rag_chain

# quiz chain

quiz_prompt_template = ChatPromptTemplate.from_messages(quiz_msg_template)

def gen_quiz_chain(retriever):

    quiz_chain = (
        {
            "context": retriever | format_docs,
            "topic": RunnablePassthrough()
        }
        | quiz_prompt_template
        | llm
        | StrOutputParser()
        )
    
    return quiz_chain