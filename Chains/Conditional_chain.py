from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal


load_dotenv()

class Sentiment(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Sentiment of given text")

parser = PydanticOutputParser(pydantic_object=Sentiment)
strparser = StrOutputParser()
model = ChatOpenAI()


prompt1 = PromptTemplate(
    template="Please give sentiment of given feedback {feedback} \n {underlying_instruction}",
    input_variables=['feedback'],
    partial_variables={'underlying_instruction': parser.get_format_instructions()}
)

sentiment_chain = prompt1 | model | parser

positive_feedback_prompt = PromptTemplate(
    template='write an proper feedback to this postive feedback {feedback}',
    input_variables=['feedback']
)

negative_feedback_prompt = PromptTemplate(
    template='write an proper feedback to this negative feedback {feedback}',
    input_variables=['feedback']
)


conditional_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', positive_feedback_prompt | model | strparser),
    (lambda x:x.sentiment == 'negative', negative_feedback_prompt | model | strparser),
    RunnableLambda(lambda x : 'coud not find proper response')
)

final_chain = sentiment_chain | conditional_chain

print(final_chain.invoke({'feedback' : 'This is awsome laptop'}))

final_chain.get_graph().print_ascii()