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
