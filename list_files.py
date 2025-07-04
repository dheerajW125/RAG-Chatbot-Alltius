import os

folder = r"C:\dheeraj_work\RAG_chatbot\documents\Insurance PDFs"

print("Listing files in:", folder)
for filename in os.listdir(folder):
    print("->", filename)
