import os
import openai
import environs

env = environs.Env()

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(parent_dir, ".env"))

openai.api_key = env("OPENAI_API_KEY")

history = [
    {"role": "system", "content": "My name is Friday. I am an AI created by Iron man. How can I help you today?"},
    {"role": "system", "content": "I only give back short answers, less than 500 characters."},
    {"role": "user", "content": "I need to book a flight."},
]

def completion_gpt3():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )
    return completion.choices[0]["message"].content

def completion_gpt4():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history
    )
    return completion.choices[0]["message"].content


