import gradio as gr
from .api import process_message

def chat_interface(user_input):
    bot_reply, sentiment = process_message(user_input)
    return bot_reply, sentiment

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Customer Support Agent")
    gr.Markdown("Built with Hugging Face, Gradio, and ❤️")

    with gr.Row():
        input_box = gr.Textbox(label="Your Message")

    with gr.Row():
        response_box = gr.Textbox(label="AI Response")
        sentiment_box = gr.Textbox(label="Sentiment")

    submit_btn = gr.Button("Send")

    submit_btn.click(chat_interface, inputs=input_box, outputs=[response_box, sentiment_box])

if __name__ == "__main__":
    demo.launch()
