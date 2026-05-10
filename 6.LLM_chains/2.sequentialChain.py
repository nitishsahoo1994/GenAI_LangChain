from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)




model1=ChatOpenAI()
model2= ChatHuggingFace(llm=llm)


prompt1=PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 =PromptTemplate(
    template='create a 5 point summary report on following \n {text}',
    input_variables=['text']
)


parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model1 | parser

result= chain.invoke({'topic':'How PM of India is elected'})

print(result)
