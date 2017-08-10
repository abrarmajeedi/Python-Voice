import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 0.7
r.energy_threshold = 400

with sr.Microphone() as source:
    try:
        audio = r.listen(source, timeout=5)
        message = str(r.recognize_bing(audio,key="BingKEY"))

        print(message)

    except sr.UnknownValueError:
        print("NO understand")

    except sr.RequestError:
        print("fail")
