from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)

#prompt = "<|system|>You are a helpful assistant.</s>\n<|user|>Give me top 10 text generation LLM models.</s>\n<|assistant|>"

result = model.invoke("Give me top 10 text generation LLM models")

print(result.content)