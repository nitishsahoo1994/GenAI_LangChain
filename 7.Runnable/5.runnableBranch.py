from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableSequence,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableBranch
)

load_dotenv()

model = ChatOpenAI()

report_prompt = PromptTemplate(
    template='Generate a detailed report on below:\n{topic}',
    input_variables=['topic']
)

summary_prompt = PromptTemplate(
    template='Generate a summary of 50 lines from below text:\n{text}',
    input_variables=['text']
)

parser = StrOutputParser()

# Report Generation Chain
report_gen_chain = RunnableSequence(
    report_prompt,
    model,
    parser
)

# Branch Chain
branch_chain = RunnableBranch(
    (
        lambda text: len(text.split()) > 300,
        RunnableSequence(summary_prompt, model, parser)
    ),
    RunnablePassthrough()
)

# Final Chain
final_chain = RunnableSequence(
    report_gen_chain,
    branch_chain
)

# Invoke
result = final_chain.invoke({
    'topic': 'USA vs Ukraine war'
})

print(result)