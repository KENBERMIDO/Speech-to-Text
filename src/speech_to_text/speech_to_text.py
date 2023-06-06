# Turn speech into readable text

import whisper

model = whisper.load_model("small.en")
result=model.transcribe('output.wav', fp16=False)
print(result["text"])
