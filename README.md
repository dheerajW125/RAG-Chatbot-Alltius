# Retrieval-Augmented Generation (RAG) Chatbot

This project implements a chatbot that can:

- Answer questions using customer support documents.
- Say "I don't know" if the answer is not found.
- Run locally or deploy to Hugging Face Spaces.

## Features

- Local vector search with FAISS
- Cloud LLM completions via Groq Llama3
- Gradio web interface

## Setup

1. Clone the repo:
    https://github.com/dheerajW125/RAG-Chatbot-Alltius.git


2. Install dependencies:
    pip install -r requirements.txt

3. Create a `.env` file with your API key:
    GROQ_API_KEY=your_groq_api_key_here

4. Start the app:
    python app.py


## Deployment

You can deploy to Hugging Face Spaces or any other cloud platform.


