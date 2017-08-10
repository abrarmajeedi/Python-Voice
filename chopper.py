import voice_recognizer as vr


text = vr.voicerecog()

if text is not None:
    list(text)
else:
    pass