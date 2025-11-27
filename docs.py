from langchain_core.documents import Document
from langchain_community.retrievers import WikipediaRetriever 

def get_wiki_docs(topic, no_of_docs):
    retriever = WikipediaRetriever(load_max_docs=no_of_docs)
    return retriever.invoke(topic)

def get_user_doc(user_info):
    return Document(page_content=user_info, metadata={"source":"user provided info"}) 
