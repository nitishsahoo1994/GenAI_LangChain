from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template="generate 5 frictional name,age and city of a {place}",
    input_variables=['place']
)
parser=StrOutputParser()
chain=prompt | model |parser
result= chain.invoke({'place':'sri lanka'})
print(result)