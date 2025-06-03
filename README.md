# TARS Voice Assistant

TARS is a voice-activated AI assistant inspired by the character from Interstellar. It uses speech recognition, large language models, and text-to-speech to create a conversational, witty, and helpful experience.

---

## Features

- **Speech-to-Text:** Uses OpenAI Whisper to transcribe your voice.
- **Conversational AI:** Powered by a local LLM via Ollama, with TARS's personality.
- **Text-to-Speech:** Replies in a robotic voice using gTTS and pydub.
- **Customizable Personality:** Defined in the `ModelFile`.

---

## Installation

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd TARS
   ```

2. **Install Python dependencies**  
   It is recommended to use a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Install system dependencies**  
   - Make sure you have `ffmpeg` installed for audio playback:
     ```sh
     sudo apt-get install ffmpeg
     ```
   - For `sounddevice`, you may need portaudio:
     ```sh
     sudo apt-get install portaudio19-dev
     ```

4. **Install and run Ollama**  
   - Download and install Ollama from [https://ollama.com/download](https://ollama.com/download)
   - Start the Ollama server:
     ```sh
     ollama serve
     ```
   - Import or create the TARS model using the provided `ModelFile`:
     ```sh
     ollama create TARS -f ModelFile
     ```

---

## Usage

1. **Start the assistant**
   ```sh
   python main.py
   ```

2. **Interact**
   - Speak into your microphone when prompted.
   - TARS will transcribe your speech, generate a witty response, and reply with synthesized speech.
   - Say "exit", "quit", or "bye" to end the session.

---

## Files

- `main.py`: Main application logic.
- `requirements.txt`: Python dependencies.
- `ModelFile`: Ollama model definition and TARS's system prompt.

---

## Troubleshooting

- **Microphone not working:** Check your system's audio input settings.
- **No audio output:** Ensure `ffmpeg` is installed and your speakers are working.
- **Ollama errors:** Make sure the Ollama server is running and the TARS model is created.

---

## Credits

- Inspired by TARS from *Interstellar*.
- Uses [Whisper](https://github.com/openai/whisper), [Ollama](https://ollama.com/), [gTTS](https://pypi.org/project/gTTS/), and [pydub](https://github.com/jiaaro/pydub).
