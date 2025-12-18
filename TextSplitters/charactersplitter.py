from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import inspect

loader = PyPDFLoader("C:\\Users\\SachinPujari\\Downloads\\Sachin_Pujari.pdf")

doc = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
    separator= ''

)

result = text_splitter.split_documents(doc)

print(result)


for res in result:
    print(res.page_content)
    print("******************************************************* /n")

#print(inspect.signature(CharacterTextSplitter.__init__))
#help(CharacterTextSplitter)