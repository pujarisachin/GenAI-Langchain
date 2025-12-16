from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text = """Hey this is how embedding workes"""

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

result = embedding_model.embed_query(text)

print(result)