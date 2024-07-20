from openai import OpenAI
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path(__file__).with_name('settings.cfg'))
openaiID = config.get('KEYS','openaiKey')

client = OpenAI(
    api_key=openaiID
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content":prompt}]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)