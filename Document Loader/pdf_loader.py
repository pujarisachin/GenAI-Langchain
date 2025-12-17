from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:\\Users\\SachinPujari\\Downloads\\Sachin_Pujari.pdf")

doc = loader.load()

print(doc)