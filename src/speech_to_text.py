# Turn speech into readable text

import whisper

model = whisper.load_model("small")
result = model.transcribe("output.wav", FP16=False)
print(result["text"])
