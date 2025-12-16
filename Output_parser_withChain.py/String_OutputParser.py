from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Write detailed report about {topic} in {number} lines',
    input_variables=['topic','number']
)

prompt2 = PromptTemplate(
    template='Give summary of following text /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'number' :20,'topic': 'GenAI'})

print(result)