import argparse
import os
import nltk
import speech_recognition as sr
from detect_speech_errors import detect_errors


def recognize_speech_live():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Processing audio...")
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            detect_errors(text)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
