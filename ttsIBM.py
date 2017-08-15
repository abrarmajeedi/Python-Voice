from watson_developer_cloud import TextToSpeechV1
import pyaudio
import wave
from ibmkeys import *


text_to_speech = TextToSpeechV1(
    username=IBM_TTS_un,
    password=IBM_TTS_pw,
    x_watson_learning_opt_out=True)  # Optional flag


def tts(message):
    with open('output.wav',
              'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(message, accept='audio/wav',
                                  voice="en-US_AllisonVoice"))

    chunk = 1024
    f = wave.open(r"output.wav","rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)

    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
