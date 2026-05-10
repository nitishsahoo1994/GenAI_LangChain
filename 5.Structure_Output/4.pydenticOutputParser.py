from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Optional, List
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name: str= Field(description='it should be any valid name')
    age: int = Field(gt=18, description='age of person')
    city: Optional[str] = Field(
        default=None,
        description='person belongs to this city'
    )


class Persons(BaseModel):
    people: List[Person]


parser = PydanticOutputParser(pydantic_object=Persons)

prompt = PromptTemplate(
    template='''
Generate 5 person from {place}.

{format_instructions}
''',
    input_variables=['place'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

chain = prompt | model | parser

result = chain.invoke({'place': 'Nepal'})

print(result)