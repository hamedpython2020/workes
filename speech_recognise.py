import speech_recognition as sr
import os
from gtts import gTTS


def speech_recognise():
    r = sr.Recognizer()
    with sr.Microphone() as sours:
        print('speak')
        audio = r.listen(sours)
    try:
        print("you said\n"+r.recognize_google(audio))
    except sr.UnknownValueError:
        print('no shit')
    except sr.RequestError:
        print('no')
    pass


def text_to_voice():
    tts = gTTS(text='hello ', lang='en')
    tts.save("good.mp3")
    os.system("good.mp3")
    pass


speech_recognise()