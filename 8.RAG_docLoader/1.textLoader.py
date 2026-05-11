from langchain_community.document_loaders import TextLoader



loader =TextLoader('cricket.txt',encoding='utf-8')
docs = loader.load()


p
print(docs[0].page_content)

print(len(docs))