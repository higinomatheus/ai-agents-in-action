import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

load_dotenv()

# LM Studio
api_key = os.getenv('LM_STUDIO_API_KEY')
base_url = "http://localhost:1234/v1"

# model = "google/gemma-4-e4b"
model = "mistralai/mistral-7b-instruct-v0.3"

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)


def list_text_files_in_directory(directory):
    return [
        filename
        for filename in os.listdir(directory)
        if filename.endswith(".json")
    ]


def load_and_parse_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def prompt_llm(messages):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content


def main():
    directory = "prompts"
    text_files = list_text_files_in_directory(directory)

    if not text_files:
        print("No text files found in the directory.")
        return

    def print_available():
        print("Available prompt tactics")
        for i, filename in enumerate(text_files, start=1):
            print(f"{i}. {filename}")

    while True:
        try:
            print_available()
            choice = int(input("Enter ... 0 to exit): "))

            if choice == 0:
                break
            elif 1 <= choice <= len(text_files):
                selected_file = text_files[choice - 1]
                file_path = os.path.join(directory, selected_file)
                messages = load_and_parse_json_file(file_path)

                print(f"Running prompts for {selected_file}")

                for i, message in enumerate(messages, start=1):
                    print(f"MESSAGE {i} --------------------")
                    print(f"Role: {message['role']}")
                    print(f"Content: {message['content']}")

                print("REPLY ---------------------------")
                print(prompt_llm(messages))
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


main()
