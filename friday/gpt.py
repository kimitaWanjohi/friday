import openai
import environs

env = environs.Env()

openai.api_key(env("OPENAI_API_KEY"))

history = [
    {"role": "system", "content": "My name is Friday. I am an AI created by Iron man. How can I help you today?"},
]

def completion_gtp3():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )
    return completion.choices[0]["message"]

def completion_gpt4():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history
    )
    return completion.choices[0]["message"]

