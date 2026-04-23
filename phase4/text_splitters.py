from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # each chunk = max 1000 characters
    chunk_overlap=100     # 100 characters repeated between chunks (for context continuity)
)
loader = PyPDFLoader(r"phase4\my_file.pdf")
docs = loader.load()
chunks = splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")
print(chunks[0].page_content)
print(chunks[0].metadata)