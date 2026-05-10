from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
query="what i the capital of India?"
embad=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
res=embad.embed_query(query)
print(str(res))