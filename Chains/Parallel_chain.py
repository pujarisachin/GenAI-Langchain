from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

openAI_model = ChatOpenAI()

HF_llm = HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation")
HF_model = ChatHuggingFace(llm = HF_llm)

parser = StrOutputParser()

template1 = PromptTemplate(
    template= 'give me top 10 youtube to study {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='give me top 10 resources apart from youtube to study {topic}',
    input_variables=['topic']
)

template3 = PromptTemplate(
    template= 'Please combine youtube and non youtube recources {youtube},{nonyoutube}',
    input_variables=['youtube','nonyoutube']
)


parallel_chain = RunnableParallel({
    'youtube': template1 | openAI_model |parser,
    'nonyoutube' : template2 | openAI_model |parser
    }
)
#print(parallel_chain.invoke({'topic' : 'GenAI and Agentic AI'}))

merger_chain = template3 | openAI_model |parser

final_chain = parallel_chain | merger_chain 



print(final_chain.invoke({'topic' : 'GenAI and Agentic AI'}))

