from elevenlabs import generate, play

def say(text):
  audio = generate(
    text=text,
    voice="Bella",
    model="eleven_monolingual_v1"
  )
  play(audio)