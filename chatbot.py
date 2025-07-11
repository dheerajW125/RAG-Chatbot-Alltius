
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
import openai

load_dotenv()





embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load text chunks from support_docs.txt
with open("support_docs.txt", "r", encoding="utf-8") as f:
    support_text = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.create_documents([support_text])

# Build the FAISS index in memory
vectorstore = FAISS.from_documents(chunks, embedding_model)

# Configure Groq API 
openai.api_key = os.getenv("GROQ_API_KEY")


from openai import OpenAI

# Make sure to configure the base and API key once
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def call_groq(prompt):
    """
    Call Groq LLM with new OpenAI v1.x client.
    """
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You must only answer based on the provided context. If the context does not contain the answer, reply exactly with 'I don't know.'"

            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content


def ask_question(query):
    # Embed query
    query_embedding = embedding_model.embed_query(query)

    # Retrieve top 3 matching chunks
    docs_and_scores = vectorstore.similarity_search_with_score_by_vector(query_embedding, k=3)

    if not docs_and_scores or docs_and_scores[0][1] < 0.4:
        return "I don't know."

    context = "\n\n".join([doc.page_content for doc, _ in docs_and_scores])

    prompt = f"""
Context:
{context}

Question: {query}

Answer:
"""
    return call_groq(prompt).strip()
