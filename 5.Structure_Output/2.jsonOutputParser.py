from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
model=ChatOpenAI()

parser= JsonOutputParser()

prompt = PromptTemplate(
    template='give 5 fact abot {topic} with {format_instruction}format ',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = prompt | model | parser
result= chain.invoke({'topic':'flood in india'})
print(result)