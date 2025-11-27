from utils import text_splitter, embeddings
from langchain_community.vectorstores import FAISS

def generate_db(all_docs):

    split_docs = text_splitter.split_documents(all_docs)

    db = FAISS.from_documents(split_docs, embeddings)

    retriever = db.as_retriever()
    
    return retriever