from transformers import pipeline

# Load a conversational model (e.g., DialoGPT or Falcon)
chatbot = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", max_new_tokens=100)

def generate_response(prompt):
    response = chatbot(prompt)[0]['generated_text']
    return response[len(prompt):].strip()
