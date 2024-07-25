import argparse
import os
import nltk
import speech_recognition as sr
from detect_speech_errors import detect_errors


def recognize_speech_from_file(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            detect_errors(text)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
