import os
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
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

def ask_chatgpt(message):
    system_message: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": "You are a helpful assistant."
    }

    user_message: ChatCompletionUserMessageParam = {
        "role": "user",
        "content": message
    }

    response = client.chat.completions.create(
        model=model,
        messages=[system_message, user_message],
        temperature=0.7
    )

    return response.choices[0].message.content

user = "What is the capital of France?"
chat_response = ask_chatgpt(user)
print(chat_response)
