from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, this is a voice note generated using Python."

# Create a gTTS object
tts = gTTS(text)

# Save the generated speech as an audio file
tts.save("voice_note.mp3")

# Play the generated voice note
# os.system("mpg321 voice_note.mp3")  # On Linux
# os.system("afplay voice_note.mp3")  # On macOS
os.system("start voice_note.mp3")   # On Windows
