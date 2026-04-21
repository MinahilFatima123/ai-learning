import chromadb

# Option A — in-memory (data lost when script ends, good for testing)
client = chromadb.Client()

# Option B — persistent (saves to disk, use this for real projects)
client = chromadb.PersistentClient(path="./chroma_db")