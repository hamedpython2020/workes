###The project for Audio Book or playlist###

import pyttsx3, os
import sounddevice
from scipy.io.wavfile import write

engine = pyttsx3.init()


def audio_reader(file_1):
    file_1 = input('C:/Users/asus/OneDrive/Documents/recorder.txt')
    book = open(file_1, mode='r')
    book_text = book.readlines()
    for i in book_text:
        engine.say(i)
        engine.runAndWait()
        pass


def audio_recorder(second, file_2):
    engine.say('record start')
    engine.runAndWait()
    recording = sounddevice.rec((second*44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file_2, 44100, recording)
    engine.say('record finish')
    engine.runAndWait()
    print('recording finished')

    pass

audio_recorder(5,'C:/Users/asus/OneDrive/Documents/recorder.mp3')