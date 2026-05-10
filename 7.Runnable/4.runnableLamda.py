from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatOpenAI()


prompt1 = PromptTemplate(
    template='generate a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain the joke from text \n {text}',
    input_variables=['text']
)

parser=StrOutputParser()



explanation_gen_chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

parallel_chain = RunnableParallel(
    {
        'explanation': RunnablePassthrough(),
        'word_count':RunnableLambda(lambda text:len(text.split()))
    }
)

final_chain= RunnableSequence(explanation_gen_chain, parallel_chain)
result=final_chain.invoke({'topic':'Donald trump'})
print(result)
