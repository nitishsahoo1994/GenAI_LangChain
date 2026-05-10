from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embaddings=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about rohit'

doc_embad=embaddings.embed_documents(documents)
query_embad=embaddings.embed_query(query)

score=cosine_similarity([query_embad],doc_embad)[0]
index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(score)

print(documents[index])
