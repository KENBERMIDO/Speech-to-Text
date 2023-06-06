# Turn speech into readable text

import whisper

model = whisper.load_model("small.en")
result = model.transcribe("sample-0.mp3", FP16=False)
print(result["text"])
