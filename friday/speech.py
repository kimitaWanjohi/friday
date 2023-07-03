import os
import environs
from elevenlabs import generate, play, set_api_key

env = environs.Env()

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(parent_dir, ".env"))


set_api_key(env("ELEVEN_LABS_KEY"))



def say(text):
  audio = generate(
    text=text,
    voice="Bella",
    model="eleven_monolingual_v1"
  )
  play(audio)