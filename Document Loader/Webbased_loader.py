from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()


url = "https://www.amazon.in/Samsung-Fully-Automatic-Ecobubble-WA80BG4441BGTL-Technology/dp/B0B8NK5HTH/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.1XALfXgJxk24Mo-mL4AuxD4GTFCTfOKeyLMSt5fuM1AGgTJDga4Ve0dXFrEzKc7KxlpPjBvC8clRxTxC16Po8U1GWDyKHdqd7gyt_SNkmKe_N_a8ERqjMxF0coKPMxeDs3oV0Y331xgYoBmnkCWYg5sFwQBm_EwrZIri0PDVsp86_xd5wAqRFj-mhVQT8V0BLAKR2y8X2uTzkvqU_wxm5oURyRaU-aIlXL3Bs1UhLR2M9UPHJubQz3jcKPh-fNjuKiG5s7vE-4bOk0RqAad4u8OuhpISh8UbAwb3KkAdnXM.hfk7YHxbAE5J7OMVN4KK44sZ1VaUfZ28-UyrHKSkvTk&dib_tag=se&pd_rd_r=e3497e81-2c1c-466c-8f16-cb3ade726a7a&pd_rd_w=LHE90&pd_rd_wg=6uNCw&qid=1765989375&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-1-spons&aref=FBb7Fu1oZK&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&th=1"

loader = WebBaseLoader(url)
doc = loader.load()

print(type(doc))

prompt = PromptTemplate(
    template = "anser {question} from {text}",
    input_variables=['question','text']
)
chain = prompt | model | parser

print(chain.invoke({'question': "what is the page talking about",'text': doc[0].page_content}))
