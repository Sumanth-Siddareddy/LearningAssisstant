# app/rag_engine.py

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.core import ServiceContext

# Setup Ollama LLM
def get_ollama_llm():
    return Ollama(model="mistral", request_timeout=60.0)

# Load and index documents
def build_index_from_data():
    documents = SimpleDirectoryReader("data/kb_docs").load_data()
    llm = get_ollama_llm()
    service_context = ServiceContext.from_defaults(llm=llm)
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    return index

# Query the index
def query_topic(index, query):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return str(response)
