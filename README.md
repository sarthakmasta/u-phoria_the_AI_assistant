# U-Phoria – AI Assistant

U-Phoria is a simple voice-based AI assistant with a graphical user interface. It can understand your voice commands, respond using text-to-speech, and perform basic actions like opening websites or telling the time.

## Features

- Voice input using microphone
- Text-to-speech responses
- Opens websites like Google, YouTube, and Spotify
- Tells the current time
- Simple and user-friendly GUI

## How to Run

1. Install the required libraries:

```
pip install pyttsx3 speechrecognition pillow pyaudio
```

2. Run the app:

```
python GUI.py
```

## Files

- `GUI.py` – Main application with GUI
- `AI_voice_output.py` – Converts text to speech
- `speech_conversion.py` – Converts speech to text
- `action.py` – Handles responses and actions

## Notes

- Make sure your microphone is connected.
- If `pyaudio` doesn’t install, use:
  ```
  pip install pipwin
  pipwin install pyaudio
  ```