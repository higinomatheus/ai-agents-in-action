import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# OpenAI
api_key = os.getenv('OPENAI_API_KEY')
base_url = None

# Groq
api_key = os.getenv('GROQ_API_KEY')
base_url = "https://api.groq.com/openai/v1"

# LM Studio
api_key = os.getenv('LM_STUDIO_API_KEY')
base_url = "http://localhost:1234/v1"

# LLM
model = "google/gemma-4-e4b"

if not api_key:
    raise ValueError("No API key found. Please check your .env file")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def ask_chatgpt(user_message):
    response = client.responses.create(
        model=model,
        instructions="You are a helpful assistant.",
        input=user_message
    )

    print(response.usage)

    return response.output_text

user = "What is the capital of France?"
response = ask_chatgpt(user)
print(response)
