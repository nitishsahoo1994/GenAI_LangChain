from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()
model=ChatOpenAI()
parser=StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a joke on {topic}',
    input_variables=['topic']
)

prompt2 =PromptTemplate(
    template='Explain then below generated joke \n {text}',
    input_variables=['text']
)

chain =RunnableSequence(prompt1,model,parser , prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))