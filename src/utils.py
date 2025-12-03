from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
