from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5-chat-latest")

response = llm.invoke("I am learning Langchain,give me suggession")
print(response)

print(response.content)