import os
from functools import lru_cache
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.document_loaders import UnstructuredFileIOLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis as RedisVectorStore
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import nltk
nltk.download('punkt')

load_dotenv()


class DocQAChatbot:
    """A chatbot for Document Question and Answer"""
    def __init__(self):
        self.open_ai_key = os.getenv("OPENAI_API_KEY")
        self.redis_url = os.getenv("REDIS_URL")

    def get_embeddings(self):
        """Return OpenAI Embeddings"""
        return OpenAIEmbeddings(openai_api_key=self.open_ai_key)

    def retrieve_answers(self, query: str, index_name="test_index"):

        embeddings = self.get_embeddings()
        vector_store = RedisVectorStore(redis_url=self.redis_url, index_name=index_name,
                                        embedding_function=embeddings.embed_query)

        qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=self.open_ai_key),
                                         retriever=vector_store.as_retriever())
        result = qa.run(query)
        print(f"-----------------------------> Result {result}")
        return result
