import fitz  # PyMuPDF
from docx import Document
import os




def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def save_combined_text(input_folder, output_file="support_docs.txt"):
    all_texts = []
    for filename in os.listdir(input_folder):
        path = os.path.join(input_folder, filename)
        if filename.endswith(".pdf"):
            print(f"Extracting {filename}...")
            all_texts.append(extract_text_from_pdf(path))
        elif filename.endswith(".docx"):
            print(f"Extracting {filename}...")
            all_texts.append(extract_text_from_docx(path))
    combined = "\n\n".join(all_texts)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(combined)
    print(f"\n Extracted text saved to {output_file}")

if __name__ == "__main__":
    # Replace this with your folder containing PDFs and DOCX files
    # folder = "documents"
    folder = r"C:\dheeraj_work\RAG_chatbot\documents\Insurance PDFs"
    save_combined_text(folder)
