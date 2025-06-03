import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import ollama
import re
import time
import pyttsx3

# --- Whisper Setup ---
whisper_model = whisper.load_model("base")

def get_audio_input(duration=5, samplerate=16000):
    print("🎤 Listening for", duration, "seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    return recording, samplerate

def transcribe_audio():
    recording, samplerate = get_audio_input()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        write(f.name, samplerate, recording)
        result = whisper_model.transcribe(f.name)
        return result["text"]

# --- Chat Engine ---
def thinking_engine(user_response):
    response = ollama.chat(
        model="TARS",
        messages=[{"role": "user", "content": user_response}],
    )
    return response["message"]["content"]

# --- TTS Setup ---
engine = pyttsx3.init(driverName='espeak')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# --- Speak Handler ---
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import time
import re

def change_pitch_and_speed(audio, pitch_shift=-2.0, speed=0.95):
    # Lower pitch and slow down playback
    new_frame_rate = int(audio.frame_rate * speed)
    audio = audio._spawn(audio.raw_data, overrides={"frame_rate": new_frame_rate})
    audio = audio.set_frame_rate(44100)
    return audio

def interpret_and_speak(text):
    actions = {
        r"\(sigh\)": lambda: None,
        r"\(sighs\)": lambda: None,
        r"\(pause\)": lambda: time.sleep(1),
        r"\(pauses\)": lambda: time.sleep(1),
        r"\.\.\.": lambda: time.sleep(0.7)
    }

    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio = AudioSegment.from_mp3(fp.name)
        
        # Lower pitch + slow speed to sound more robotic like TARS
        audio = change_pitch_and_speed(audio, pitch_shift=-2.0, speed=1.1)
        
        play(audio)  # This blocks


# --- Main Loop ---
print("🔵 Initializing TARS.....")
while True:
    print("\nSay something to TARS or say 'exit' to quit.")
    user_input = transcribe_audio()
    print("USER:", user_input)

    if user_input.strip().lower() in ["exit", "quit", "bye"]:
        print("TARS: Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break

    response = thinking_engine(user_input)
    print("TARS:", response)
    interpret_and_speak(response)

    time.sleep(1)  # Small delay before next input
