# 🎙️ Speech Recognition using Python

This simple Python project demonstrates how to convert spoken audio into text using the `speech_recognition` library and Google's Web Speech API.

## 📂 Project Structure
```
speech_recognition_project/
│
├── hello-278029.wav       # Sample audio file
├── main.py                # Main script to perform speech-to-text
└── README.md              # Project documentation
```

## 🛠️ Requirements

- Python 3.x
- `speechrecognition` library

### Install Dependencies
```bash
pip install SpeechRecognition
```

## 🚀 How It Works

1. Loads an audio file (`hello-278029.wav`).
2. Uses the `speech_recognition` module to convert the audio into text.
3. Prints the recognized text or handles errors if audio is unclear or API fails.

## 📄 Code Overview

```python
import speech_recognition as sr

AUDIO_FILE = ("hello-278029.wav")
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("The Text from the audio file is: " + r.recognize_google(audio))

except sr.UnknownValueError:
    print("Audio is not Clear")

except sr.RequestError as e:
    print("Try Again; {0}".format(e))
```

## ✅ Output

If the audio is clear, you'll see:

```
The Text from the audio file is: Hello, how are you?
```

Otherwise, appropriate error messages like:

```
Audio is not Clear
```

or

```
Try Again; [API request error]
```

## 🧠 Notes

- This example uses Google's free Web Speech API, which requires an internet connection.
- For offline speech recognition, you can explore libraries like `vosk`.

(Make sure to "pip install SpeechRecognition")
