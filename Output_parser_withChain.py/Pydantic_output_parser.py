from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Optional,Literal

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name : str = Field(description="name of the person")
    age : Optional[int] = Field(description="age of person")
    gender : Literal['male','Female'] = Field(description='Gender of person')


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate name,age and gender of {city} person \n {format_instruction}',
    input_variables=['city'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
    )

chain = template | model | parser

result = chain.invoke({'city' : 'china'})
print(result)