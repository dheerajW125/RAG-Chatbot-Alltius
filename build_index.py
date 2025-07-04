from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load your document
with open("support_docs.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(text)

# Use LangChain embedding wrapper
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS index
faiss_index = FAISS.from_texts(chunks, embedding_model)
faiss_index.save_local("faiss_index")

print("✅ FAISS index built and saved.")
