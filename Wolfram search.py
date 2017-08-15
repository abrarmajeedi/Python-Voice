import wolframalpha as wa
import voice_recognizer as vr
import ttsIBM as tts
from ibmkeys import *

client = wa.Client(wolf_id)
searchitem = vr.voicerecog()
res = client.query(searchitem)
text = next(res.results).text
tts.tts(text)