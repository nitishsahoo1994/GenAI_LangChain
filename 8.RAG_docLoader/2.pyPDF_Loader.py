from langchain_community.document_loaders import PyPDFLoader



loader =PyPDFLoader('file-example_PDF.pdf')

docs =loader.load()

# print(docs)

print(len(docs))

for document in docs:
    print(document.metadata)

