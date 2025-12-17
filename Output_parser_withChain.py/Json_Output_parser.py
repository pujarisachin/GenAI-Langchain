from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template="""Give me 5 funny facts about {topic} /n {format_instruction1}""",
    input_variables=['topic'],
    partial_variables={'format_instruction1' : parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'AI'})
print(result)