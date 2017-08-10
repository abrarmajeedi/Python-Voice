import speech_recognition as sr


def voicerecog():
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            message = str(r.recognize_bing(audio,key="a2bb69efacd44fd896c01b797b4f3999"))

            return message

        except sr.UnknownValueError:
            print("NO understand")
            pass

        except sr.RequestError:
            print("fail")
            pass

