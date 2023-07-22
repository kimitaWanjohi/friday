import os
import openai
import environs
import threading
from .speech import say
from .listen import listen
from .functions import functions
from .typing import typing

env = environs.Env()

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(parent_dir, ".env"))

openai.api_key = env("OPENAI_API_KEY")

history = [
    {"role": "system", "content": "My name is Friday. I am an AI created by Iron man. How can I help you today?"},
    {"role": "system", "content": "I can help you do anything you want. I can book a flight, play music, tell you the weather, and more."},
    {"role": "system", "content": "I don't mention that I am an AI or say as a large language model, make the conversation more natural."},
]

def completion_gpt3():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=history
    )
    return completion.choices[0]["message"]

def completion_gpt4():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history
    )
    return completion.choices[0]["message"]


def run_threaded(content):
    thread1 = threading.Thread(target=typing, args=(content,))
    thread2 = threading.Thread(target=say, args=(content,))
    thread1.start()
    thread2.start()
    

def chat():
    say("Hello, my name is Friday. How can I help you today?")
    while True:

        audio = listen()
        if audio == "exit":
            break
        history.append({
            "role": "user",
            "content": audio
        })
        gpt_3 = completion_gpt3()        
        # gpt_4 = completion_gpt4()
        run_threaded(gpt_3.content)
        history.append(gpt_3)

chat()