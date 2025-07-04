import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

if not os.path.exists("faiss_index"):
    print("Building FAISS index...")
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    with open("support_docs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    faiss_index = FAISS.from_texts(chunks, embedding_model)
    faiss_index.save_local("faiss_index")
else:
    faiss_index = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
