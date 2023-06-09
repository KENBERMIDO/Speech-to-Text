import pyaudio
import wave
import keyboard
import whisper
import os
import openai

# Define constants for recording
CHUNK = 1024  # number of audio samples per frame
FORMAT = pyaudio.paInt16  # audio format
CHANNELS = 1  # mono audio
RATE = 44100  # sample rate in Hz


def record():
    # Create PyAudio object, place it in 'audio'
    audio = pyaudio.PyAudio()

    # Open audio stream from microphone
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording started...")

    # Collect audio data in chunks
    frames = []
    while keyboard.is_pressed('p'):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished...")

    # Stop and close audio stream
    stream.stop_stream()
    stream.close()

    # Save audio data to WAV file
    with wave.open("output.wav", "wb") as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(audio.get_sample_size(FORMAT))
        wav_file.setframerate(RATE)
        wav_file.writeframes(b"".join(frames))

    print("Saved audio to output.wav")


def transcribe():
    model = whisper.load_model("small.en")
    result = model.transcribe("output.wav", fp16=False)
    with open("transcript.txt", "w") as f:
        print("Captured: ", result["text"])
        f.write(result["text"])

def chatResponse():

    openai.api_key = "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"

    # "r" = read mode
    with open("transcript.txt", "r") as f:
        text = f.read()

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response)

if __name__ == "__main__":
    while True:
        keyboard.wait("p")
        record()
        transcribe()
        chatResponse()
