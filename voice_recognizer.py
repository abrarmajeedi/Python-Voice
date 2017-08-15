import speech_recognition as sr
from ibmkeys import *


def voicerecog():
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            message = str(r.recognize_bing(audio,key=bing_speech_key))

            return message

        except sr.UnknownValueError:
            print("NO understand")
            pass

        except sr.RequestError:
            print("fail")
            pass

