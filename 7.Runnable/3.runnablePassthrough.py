from langchain_openai import ChatOpenAI
from dotenv import  load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()
model=ChatOpenAI()
parser=StrOutputParser()

prompt1 =PromptTemplate(
    template='Generate a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain the joke from below \n {text}',
    input_variables=['text']
)

joke_gen_chain=RunnableSequence(prompt1, model, parser)
parallel_chain =RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation': RunnableSequence(prompt2, model, parser)
    }
)


final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
res=final_chain.invoke({'topic':'relationship'})
print(res)