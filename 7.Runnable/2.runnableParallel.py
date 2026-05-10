from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

model=ChatOpenAI()
parser = StrOutputParser()

tweet_Prompt=PromptTemplate(
    template='Generate a tweet on {topic}',
    input_variables=['topic']
)

linkedIn_Prompt=PromptTemplate(
    template='Generate a linkedIn post on {topic}',
    input_variables=['topic']
)

chain= RunnableParallel({
    'tweet':RunnableSequence(tweet_Prompt, model, parser),
    'linkedIn':RunnableSequence(linkedIn_Prompt, model,parser)
}
)


result=chain.invoke({'topic':'cricket'})

result_final =("this the tweet which is generated ==>{} \n and this the linkedIn post which is"
              "generated==>{} ".format(result['tweet'],result['linkedIn']))

print(result_final)