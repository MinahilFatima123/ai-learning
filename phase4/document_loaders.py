from langchain_community.document_loaders import PyPDFLoader

# Load a PDF
loader = PyPDFLoader(r"phase4\my_file.pdf")
docs = loader.load()

for doc in docs[:2]:
    print(doc.page_content)
    print(doc.metadata)
    print("---")