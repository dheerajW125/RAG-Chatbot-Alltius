import gradio as gr
from chatbot import ask_question

def chat_interface(question):
    return ask_question(question)

iface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="Ask your question..."),
    outputs="text",
    title=" RAG Chatbot ",
    description="Ask questions based on your support documentation."
)

if __name__ == "__main__":
    iface.launch()
